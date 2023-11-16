Title: Logging

Logging on webOS is handled by the `PmLogDaemon` service. It is similar to most
other system logging daemons. Most log messages are dumped into
`/var/log/messages` or `/var/log/legacy-log`, though some are routed into different paths&mdash;see
configuration in `/etc/pmlog.d/`.

By default on production webOS, only messages of certain types from specific
sources may be logged to a file. Allowed messages are configured in `/etc/PmLogDaemon/whitelist.txt`.

You can disable log whitelisting by executing certain luna calls:
```sh
# webOS 4.x+
luna-send -n 1 -f luna://com.webos.service.config/setConfigs '{"configs":{"system.collectDevLogs":true}}'

# webOS 3.x and older
luna-send -n 1 -f 'luna://com.webos.pmlogd/setdevlogstatus' '{"recordDevLogs":true}'
```

Then log levels can be adjusted using `PmLogCtl`:
```sh
# List all contexts. These only show up after a first message on a specific
# context.
PmLogCtl show

# Adjust log level
PmLogCtl set WAM debug

# Bulk adjust
PmLogCtl set '*' none
```

Logs can be viewed by running:
```sh
tail -F /var/log/messages
```

Keep in mind that most log files (including `/var/log/messages`) are rotated,
and therefore setting too high of a logging level may cause you to miss
messages (even when using the `-F` flag).

## PmLogLib stub
Alternatively (on non-rooted devices) a
[PmLogLib library stub](https://github.com/webosbrew/meta-lg-webos-ndk#system-library-logging) can be used that will print out logs to standard output.

## Crash logs
Crash logs are dumped into `/var/log/reports/librdx/` or
`/tmp/faultmanager/crash/`. These are gzipped text files containing process
information, memory maps, backtraces, and some memory dumps. These *are*
automatically reported to LG unless `rdxd` is blocked (as
Homebrew Channel does on startup).

Crashes may also cause alert popups on screen if the system is running in DEBUG
mode.

Crash log dumping can be disabled by setting the `SEGFAULT_SIGNALS` environment
variable to an empty string before launch, like so:
```sh
SEGFAULT_SIGNALS= ./buggy-binary
```
