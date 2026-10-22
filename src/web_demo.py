"""Local demonstration API for the existing research controller (no CV inference)."""
from dataclasses import asdict
from http.server import SimpleHTTPRequestHandler
import json
from pathlib import Path
from urllib.parse import urlsplit

from .controller import Timing, replay

WEB = Path(__file__).resolve().parents[1] / 'web'
MAX_ROWS = 1800


def evaluate_payload(payload):
    if not isinstance(payload, dict) or set(payload) - {'rows', 'timing'}:
        raise ValueError('Expected an object with rows and optional timing')
    rows = payload.get('rows')
    if not isinstance(rows, list) or not 1 <= len(rows) <= MAX_ROWS:
        raise ValueError(f'Provide 1 to {MAX_ROWS} observations; reset to begin another run')
    timing = payload.get('timing', {})
    if not isinstance(timing, dict):
        raise ValueError('timing must be an object')
    timing = Timing(**timing)
    decisions = replay(rows, timing)
    return {'decision': decisions[-1], 'processed_rows': len(decisions),
            'timing': asdict(timing), 'source': 'synthetic_queue_inputs'}


class DemoHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(WEB), **kwargs)

    def json_response(self, code, body):
        encoded = json.dumps(body, allow_nan=False).encode()
        self.send_response(code)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(encoded)))
        self.send_header('Cache-Control', 'no-store')
        self.end_headers()
        self.wfile.write(encoded)

    def do_GET(self):
        if urlsplit(self.path).path == '/api/health':
            self.json_response(200, {'status': 'ready', 'controller': 'src.controller.Controller',
                                     'timing': asdict(Timing()), 'max_rows': MAX_ROWS})
        else:
            super().do_GET()

    def do_POST(self):
        if urlsplit(self.path).path != '/api/replay':
            self.json_response(404, {'error': 'Unknown endpoint'})
            return
        # Only the same local page may submit requests through a browser.
        origin = self.headers.get('Origin')
        allowed_hosts = {f'127.0.0.1:{self.server.server_port}', f'localhost:{self.server.server_port}'}
        if self.headers.get('Host') not in allowed_hosts or (origin and urlsplit(origin).netloc not in allowed_hosts):
            self.json_response(403, {'error': 'Use the local dashboard origin'})
            return
        try:
            length = int(self.headers.get('Content-Length', '0'))
            if not 0 < length <= 1_000_000:
                raise ValueError('Request must be between 1 byte and 1 MB')
            if self.headers.get_content_type() != 'application/json':
                raise ValueError('Content-Type must be application/json')
            def reject_constant(value):
                raise ValueError(f'Invalid JSON number: {value}')
            payload = json.loads(self.rfile.read(length), parse_constant=reject_constant)
            result = evaluate_payload(payload)
        except (ValueError, TypeError, UnicodeError) as exc:
            self.json_response(400, {'error': str(exc)})
            return
        self.json_response(200, result)

    def end_headers(self):
        self.send_header('X-Content-Type-Options', 'nosniff')
        super().end_headers()
