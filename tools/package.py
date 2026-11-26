"""Write immutable SQLite page assets and a packed interior-page bundle."""

import argparse
import gzip
import hashlib
import json
import shutil
import sqlite3
import tempfile
import time
from pathlib import Path
from urllib.parse import urlsplit

from trail_pieces import NODES_PER_PIECE, write_trails
from prerender import render
from math_font import verify_math_font

PAGE = 32768
DEFAULT_PAGES_PER_PIECE = 4


def store_gzip(path, data):
    with (
        path.open("wb") as raw,
        gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=0, compresslevel=6) as stream,
    ):
        stream.write(data)


def origin(value):
    url = urlsplit(value)
    if (url.scheme != "https" or not url.hostname or url.username is not None
            or url.password is not None or url.path not in ("", "/") or url.query or url.fragment):
        raise argparse.ArgumentTypeError("Expected an HTTPS production origin")
    return value.rstrip("/")


def package(dbfile, out, discussion=None, base_url=None, preview_probe=False, *, pages_per_piece=DEFAULT_PAGES_PER_PIECE, database_source_docs=True):
    if pages_per_piece not in (1, 2, 4, 8):
        raise ValueError("Expected 1, 2, 4 or 8 SQLite pages per piece")
    start = time.monotonic()
    with sqlite3.connect(f"{dbfile.resolve().as_uri()}?mode=ro", uri=True) as db:
        if db.execute("PRAGMA page_size").fetchone()[0] != PAGE:
            raise ValueError("Expected 32 KiB pages")
        pages = db.execute("PRAGMA page_count").fetchone()[0]
        offset = db.execute("SELECT value FROM summary WHERE metric='fts_declaration_offset'").fetchone()[0]
        internal = [
            p for (p,) in db.execute("SELECT pageno FROM dbstat WHERE pagetype='internal' ORDER BY pageno")
        ]
    with dbfile.open("rb") as f:
        ident = "gzip-v1-" + hashlib.file_digest(f, "sha256").hexdigest()
    if pages_per_piece != 1:
        ident += f"-p{pages_per_piece}"
    out.parent.mkdir(parents=True, exist_ok=True)
    if out.exists():
        raise FileExistsError(f"Choose an empty deploy directory: {out}")
    with tempfile.TemporaryDirectory(dir=out.parent) as tmp:
        stage = Path(tmp) / "assets"
        shutil.copytree("site", stage)
        shutil.copytree("LICENSES", stage / "LICENSES")
        for source in sorted(Path("packages").glob("*/LICENSE")):
            terms = stage / "LICENSES" / source.parent.name
            terms.mkdir()
            shutil.copyfile(source, terms / "LICENSE.txt")
            notice = source.with_name("NOTICE")
            if notice.is_file():
                shutil.copyfile(notice, terms / "NOTICE.txt")
            attribution = source.with_name("ATTRIBUTION.md")
            if attribution.is_file():
                shutil.copyfile(attribution, terms / attribution.name)
        vendor = stage / "engine-tmp"
        vendor.mkdir()
        for name in ("sqlite3.wasm", "index.mjs", "sqlite3-opfs-async-proxy.js"):
            shutil.copyfile(Path("node_modules/@sqlite.org/sqlite-wasm/dist") / name, vendor / name)
        pako = Path("node_modules/pako")
        module = (pako / "dist/browser/pako_inflate.esm.min.mjs").read_bytes()
        license_text = (pako / "LICENSE").read_bytes()
        (vendor / "pako-inflate.mjs").write_bytes(b"/*!\n" + license_text + b"*/\n" + module)
        # Keep the engine and its relative imports together under a digest of all four files.
        engine_hash = hashlib.sha256()
        for asset in sorted(vendor.iterdir()):
            engine_hash.update(asset.name.encode() + b"\0" + hashlib.sha256(asset.read_bytes()).digest())
        engine = "vendor/" + engine_hash.hexdigest()
        (stage / "vendor").mkdir()
        vendor.rename(stage / engine)
        for script in ("directory.mjs", "page-reader.mjs", "query-thread.mjs", "console-worker.mjs"):
            path = stage / script
            path.write_text(path.read_text().replace("/vendor/", "/" + engine + "/"))
        directory = stage / "db" / ident
        (directory / "p").mkdir(parents=True)
        if pages_per_piece != 1:
            reader = stage / "page-reader.mjs"
            gzip_reader = reader.read_text().removesuffix("export {readGzip as readAsset};\n")
            template = Path("tools/templates/grouped-page-reader.mjs").read_text()
            reader.write_text(gzip_reader + template.replace("@PAGES_PER_PIECE@", str(pages_per_piece))
                              .replace("@TOTAL_PAGES@", str(pages)))
        internal_set = set(internal)
        bundle = bytearray()
        with dbfile.open("rb") as f:
            for first in range(1, pages + 1, pages_per_piece):
                count = min(pages_per_piece, pages - first + 1)
                buf = f.read(PAGE * count)
                if len(buf) != PAGE * count:
                    raise ValueError("Truncated SQLite input")
                store_gzip(directory / "p" / str((first - 1) // pages_per_piece + 1), buf)
                for index in range(count):
                    if first + index in internal_set:
                        bundle.extend(buf[index * PAGE:(index + 1) * PAGE])
            if f.read(1):
                raise ValueError("Page count disagrees with file size")
        store_gzip(directory / "interior", bundle)
        with sqlite3.connect(dbfile.resolve().as_uri() + "?mode=ro", uri=True) as db:
            write_trails(db, directory / "trails-v1", store_gzip)
        (stage / "proof.json").write_text(
            json.dumps(
                {
                    "buildId": ident,
                    "traceNodesPerPiece": NODES_PER_PIECE,
                    "pageCount": pages,
                    "pagesPerPiece": pages_per_piece,
                    "pageBytes": PAGE,
                    "interior": internal,
                    "ftsDeclarationOffset": offset,
                },
                separators=(",", ":"),
            )
            + "\n"
        )
        if not preview_probe:
            (stage / "app.mjs").unlink()  # The probe client has no production caller.
        if base_url:
            shutil.copyfile("assets/qed-codex-logo.png", stage / "qed-codex-logo.png")
        render(dbfile, stage, base_url, preview_probe, database_source_docs=database_source_docs)
        print("Packaged math font:", json.dumps(verify_math_font(stage), sort_keys=True))
        loader = ""
        widget_css = ""
        if discussion is not None:
            settings = json.loads(discussion.read_text())
            fields = {"repoId", "category", "categoryId"}
            if set(settings) != fields or not all(isinstance(v, str) and v.strip() for v in settings.values()):
                raise ValueError("Discussion settings require repoId, category and categoryId")
            (stage / "discussion.json").write_text(json.dumps(settings, sort_keys=True) + "\n")
            shutil.copyfile("tools/discussion.mjs", stage / "discussion.mjs")
            with (stage / "directory.mjs").open("a") as entry:
                entry.write('\nimport("/discussion.mjs").catch(() => {});\n')
            loader = " https://giscus.app"
            widget_css = " https://giscus.app/default.css"
        (stage / "_headers").write_text(
            "/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n"
            f"  Content-Security-Policy: default-src 'none'; script-src 'self' 'wasm-unsafe-eval'{loader}; style-src 'self'{widget_css}; "
            "worker-src 'self'; connect-src 'self' https://raw.githubusercontent.com; frame-src https://giscus.app; "
            "img-src 'self'; font-src 'self'; base-uri 'none'; object-src 'none'; frame-ancestors 'none'; form-action 'self'\n"
            "/assets/*\n  Cache-Control: public, max-age=31536000, immutable\n"
            "/vendor/*\n  Cache-Control: public, max-age=31536000, immutable\n"
            "/db/*\n  Cache-Control: public, max-age=31536000, immutable, no-transform\n  Content-Type: application/gzip\n"
        )
        if preview_probe:
            with (stage / "_headers").open("a") as headers:
                for path in ("/probe", "/probe.html"):
                    headers.write(f"{path}\n  X-Robots-Tag: noindex\n")
        files = [p for p in stage.rglob("*") if p.is_file()]
        if len(files) >= 20000:
            raise ValueError(f"Deployment has {len(files)} files")
        report = {
            "buildId": ident,
            "pageBytes": PAGE,
            "pageCount": pages,
            "databaseBytes": dbfile.stat().st_size,
            "pagesPerPiece": pages_per_piece,
            "interiorPages": len(internal),
            "interiorBytes": len(internal) * PAGE,
            "deployFiles": len(files),
            "deployBytes": sum(p.stat().st_size for p in files),
        }
        stage.rename(out)
    print(json.dumps(report, indent=2))
    print(f"Local static packaging: {time.monotonic() - start:.2f} seconds", flush=True)


if __name__ == "__main__":
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("database", type=Path)
    cli.add_argument("out", type=Path)
    cli.add_argument("--discussion", type=Path, help="Opt in to the giscus loader with public repository and category IDs")
    mode = cli.add_mutually_exclusive_group()
    mode.add_argument("--base-url", type=origin, help="Production origin for canonical links, social cards and sitemap")
    mode.add_argument("--preview-probe", action="store_true", help="Include the noindex database fixture page on a preview")
    mode.add_argument("--production", action="store_true", help="Use the production origin in site-settings.json")
    cli.add_argument("--database-source-docs", action=argparse.BooleanOptionalAction, default=True,
                     help="Read modules with only source documentation from SQLite")
    cli.add_argument("--pages-per-piece", type=int, choices=[1, 2, 4, 8], default=DEFAULT_PAGES_PER_PIECE,
                     help="Number of contiguous SQLite pages in each stored gzip file")
    a = cli.parse_args()
    if a.production:
        a.base_url = origin(json.loads(Path("site-settings.json").read_text())["base_url"])
    package(a.database, a.out, a.discussion, a.base_url, a.preview_probe,
            pages_per_piece=a.pages_per_piece, database_source_docs=a.database_source_docs)
