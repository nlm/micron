# micron

Minimal replacement for cron in containers

## Usage

```
micron '0 0 * * *' -- find /var/log -name '*.log' -mtime +30 -delete
```
