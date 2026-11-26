"""Time local Wrangler readiness, including a successful static manifest fetch."""

import argparse
import json
import os
import signal
import subprocess
import time
from pathlib import Path
from urllib.error import URLError
from urllib.request import urlopen


def time_preview(site, port):
    expected = (site / "proof.json").read_bytes()
    started = time.monotonic()
    args = [
        "node_modules/.bin/wrangler",
        "pages",
        "dev",
        str(site),
        "--ip",
        "127.0.0.1",
        "--port",
        str(port),
        "--inspector-port",
        str(port + 1000),
        "--persist-to",
        "inputs/timing",
    ]
    proc = subprocess.Popen(
        args,
        start_new_session=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.STDOUT,
        env={**os.environ, "WRANGLER_SEND_METRICS": "false"},
    )
    try:
        for _ in range(600):
            if proc.poll() is not None:
                raise RuntimeError("Wrangler exited before serving the preview")
            try:
                with urlopen(f"http://127.0.0.1:{port}/proof.json", timeout=2) as response:
                    if response.read() == expected:
                        return round(time.monotonic() - started, 3)
            except (URLError, TimeoutError):
                pass
            time.sleep(0.05)
        raise TimeoutError("Wrangler readiness timed out")
    finally:
        os.killpg(proc.pid, signal.SIGTERM)
        proc.wait(timeout=15)


if __name__ == "__main__":
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("site", type=Path)
    cli.add_argument("--port", type=int, default=18744)
    a = cli.parse_args()
    print(json.dumps({"localReadySeconds": time_preview(a.site, a.port)}))
