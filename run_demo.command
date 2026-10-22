#!/bin/zsh
set -eu
cd -- "${0:A:h}"
typeset demo_python=''
for candidate in "${DIPLOMA_PYTHON:-python3}" "$HOME/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3" python3.13 python3.12 python3.11 python3.10; do
  if "$candidate" -c 'import sys; sys.exit(0 if sys.version_info >= (3,10) else 1)' 2>/dev/null; then
    demo_python="$candidate"
    break
  fi
done
if [[ -z "$demo_python" ]]; then
  print 'Python 3.10+ is required. Install Python from python.org, then run this file again.'
  exit 1
fi
if (( $# == 0 )); then
  exec "$demo_python" -u demo.py --serve
else
  exec "$demo_python" -u demo.py "$@"
fi
