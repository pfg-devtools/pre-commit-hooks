#!/usr/bin/env python3
import sys
def main(argv):
    rc = 0
    for path in argv:
        data = open(path, 'rb').read()
        if b'\t' in data:
            print(f'tabs found: {path}')
            rc = 1
    return rc
if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1:]))
