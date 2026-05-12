#!/usr/bin/env python3
import re, sys
AKIA = re.compile(rb'AKIA[0-9A-Z]{16}')
def main(argv):
    rc = 0
    for path in argv:
        if AKIA.search(open(path, 'rb').read()):
            print(f'possible aws key: {path}')
            rc = 1
    return rc
if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1:]))
