# micron

Minimal replacement for cron in containers

`micron` is made to easily create scheduled-tasks containers,
with the following limits:

- 1 task per container
- 1 schedule per task (cron-compatible)
- one execution at a time
  (if the first execution is not finished in time
  for the next schedule, execution is skipped)

## Installation

```
pip install micron
```

## Usage

```
usage: micron [-h] [-x] [-q] schedule program [program ...]

positional arguments:
  schedule             a cron-like schedule
  program              the command line to run

optional arguments:
  -h, --help           show this help message and exit
  -x, --exit-on-error  exit if the program return-code is non-zero
  -q, --quiet          do not log micron actions
```

Example

```
micron '0 0 * * *' -- find /var/log -name '*.log' -mtime +30 -delete
```
