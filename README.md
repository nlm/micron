# micron

Minimal replacement for cron in containers

## Usage

```
micron '* * * * *' -- find /var/log -name '*.log' -mtime +30 -delete
```
