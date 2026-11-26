import json
from pathlib import Path
import subprocess
import tarfile
import tempfile
import unittest

from check_informalization_pr import InvalidInformalization, read_note
from import_lean_docs import source_surface
from lean_selection import select_archive


class SelectionTests(unittest.TestCase):
    def test_import_closure_and_explicit_wrapper(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            folder = repo / "lean"
            folder.mkdir()
            for name, text in {"Root":"import Dep\n/-\nimport Outside\n-/","Dep":"import Mathlib",
                               "Wrapper":"import Root Outside","Outside":""}.items():
                (folder / (name + ".lean")).write_text(text)
            subprocess.run(["git","init","-q",repo],check=True)
            subprocess.run(["git","-C",repo,"add","lean"],check=True)
            tree = subprocess.check_output(["git","-C",repo,"write-tree"],text=True).strip()
            cfg = dict(folder="lean",commit=tree,roots=["Root.lean"],extraModules=["Wrapper.lean"])
            archive = repo / "input.tar"
            groups = select_archive(cfg, repo, archive, source_surface)
            self.assertEqual(groups["Root.lean"], {"Root.lean", "Dep.lean"})
            with tarfile.open(archive) as stream:
                self.assertEqual([Path(s).name for s in stream.getnames()], ["Dep.lean","Root.lean","Wrapper.lean"])
            (folder / "Dep.lean").write_text("changed")
            with self.assertRaisesRegex(ValueError, "Git blob differs"):
                select_archive(cfg, repo, archive, source_surface)

    def test_absence_requires_pinned_import_configuration(self):
        cfg = dict(commit="a"*40,repository="https://example.org/repo",folder="lean",
                   license="Apache-2.0",copyrightStatus="absent")
        fields = dict(module="M.lean",writer="Writer",author="submitter",declarations=[],
                      source_commit=cfg["commit"],license=cfg["license"],origin="other-author",
                      entry_type="source-documentation",copyright_status="absent",
                      source=f"{cfg['repository']}/blob/{cfg['commit']}/lean/M.lean")
        content = ("---\n"+json.dumps(fields)+"\n---\nBody").encode()
        self.assertEqual(read_note(content, maintainer=True, import_config=cfg).meta["copyright_status"], "absent")
        for config in (None, {**cfg,"commit":"b"*40}, {**cfg,"copyrightStatus":"present"}):
            with self.assertRaises(InvalidInformalization):
                read_note(content, maintainer=True, import_config=config)
        with self.assertRaises(InvalidInformalization):
            read_note(content, import_config=cfg)
