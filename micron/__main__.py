#!/usr/bin/env python3
import argparse
import subprocess
import sys
import time

from crontab import CronTab

PROGNAME = 'micron'

def main():
    parser = argparse.ArgumentParser(PROGNAME)
    parser.add_argument('-x', '--exit-on-error',
                        action='store_true', default=False,
                        help='exit if the program return-code is non-zero')
    parser.add_argument('-q', '--quiet', action='store_true', default=False,
                        help='do not log micron actions')
    parser.add_argument('schedule', type=CronTab,
                        help='a cron-like schedule')
    parser.add_argument('program', nargs='+',
                        help='the command line to run')
    args = parser.parse_args()

    while True:
        if not args.quiet:
            print(f'[{PROGNAME}] next run in '
                  f'{args.schedule.next(default_utc=True):.02f}s',
                  file=sys.stderr)
        time.sleep(args.schedule.next(default_utc=True))
        try:
            subprocess.run(
                args.program,
                stdout=sys.stdout,
                stderr=sys.stderr,
                check=True
            )
        except subprocess.CalledProcessError as err:
            if not args.quiet:
                print(f'[{PROGNAME}] error: {err}', file=sys.stderr)
            if args.exit_on_error:
                return False


if __name__ == '__main__':
    main()
