from __future__ import annotations

import argparse
import math
import os
import subprocess
from typing import Sequence

def main(argv: Sequence[str] | None = None) -> int:
    print("Hello World")
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'filenames', nargs='*',
        help='Filenames pre-commit believes are changed.',
    )
    parser.add_argument(
        '--enforce-all', action='store_true',
        help='Enforce all files are checked, not just staged files.',
    )
    parser.add_argument(
        '--maxkb', type=int, default=500,
        help='Maximum allowable KB for added files',
    )
    args = parser.parse_args(argv)
    
    return 0

if __name__ == '__main__':
    raise SystemExit(main())