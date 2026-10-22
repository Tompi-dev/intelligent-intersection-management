"""Repeatable pre-defense checks and interactive local Python controller dashboard."""
from http.server import ThreadingHTTPServer
import argparse
import json
from pathlib import Path
import subprocess
import sys

from src.controller import replay
from src.web_demo import DemoHandler

ROOT = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--serve', action='store_true', help='Run the interactive dashboard and Python API after checks')
    parser.add_argument('--port', type=int, default=8766)
    args = parser.parse_args()
    if sys.version_info < (3, 10):
        parser.error('Python 3.10+ is required; on this Mac use ./run_demo.command')
    print('RESEARCH PROTOTYPE — synthetic queue data; no video inference or traffic-effectiveness result.', flush=True)
    print(f'Python: {sys.version.split()[0]} | executable: {sys.executable}', flush=True)
    check = subprocess.run([sys.executable, '-m', 'unittest', 'discover', '-s', 'tests', '-v'], cwd=ROOT)
    if check.returncode:
        raise SystemExit(check.returncode)
    rows = json.loads((ROOT / 'prototype/sample_observations.json').read_text())
    decisions = replay(rows)
    expected = json.loads((ROOT / 'prototype/expected_output.json').read_text())
    if decisions != expected:
        raise SystemExit('Replay differs from the checked-in expected output. Inspect before presenting.')
    print('\nCONTROLLER REPLAY (simulation time, not elapsed wall-clock time)')
    print(f'{"t(s)":>6} {"stage":<9} {"group":<6} {"mode":<16} reason')
    for d in decisions:
        print(f'{d["time_s"]:6.0f} {d["stage"]:<9} {str(d["group"]):<6} {d["mode"]:<16} {d["reason"]}')
    print('\nPASS: replay matches prototype/expected_output.json', flush=True)
    if not args.serve:
        return
    try:
        server = ThreadingHTTPServer(('127.0.0.1', args.port), DemoHandler)
    except OSError as exc:
        parser.error(f'Cannot start local dashboard: {exc}. Stop the previous server or try --port 8767.')
    with server:
        print(f'\nInteractive dashboard: http://127.0.0.1:{args.port}/', flush=True)
        print('Synthetic queue inputs connected to the Python controller. Stop with Ctrl+C.', flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print('\nDemo server stopped.')


if __name__ == '__main__':
    main()
