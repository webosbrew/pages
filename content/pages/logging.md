Title: Logging

Logging on webOS TV is handled by `PmLogDaemon` service. It is similar to most
other system logging daemons. Most log messages are dumped into
`/var/log/messages` (though some are routed into different paths - see
configuration in `/etc/pmlog.d/`)

By default, on retail software, only messages of certain types from specific
sources are logged into a file - configured in `/etc/PmLogDaemon/whitelist.txt`.

In order to disable log whitelisting certain luna calls need to be executed.
```sh
# webOS 4.x+
luna-send -n 1 -f luna://com.webos.service.config/setConfigs '{"configs": {"system.collectDevLogs": true}}'

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

Then logs can be viewed by running:
```sh
tail -F /var/log/messages
```

Keep in mind `/var/log/messages` file is rotated, thus setting too high logging
level may cause it to drop messages (even when using `-F` flag)

## PmLogLib stub
Alternatively (on non-rooted devices) a
[PmLogLib library stub](https://github.com/webosbrew/meta-lg-webos-ndk#system-library-logging) can be used that will print out logs into standard output.

## Crashlogs
Crash logs are dumped into `/var/log/reports/librdx/` or
`/tmp/faultmanager/crash/`. These are gzipped text files containing process
information, memory maps, backtrace and some memory dumps. These *are*
automatically reported to LG unless `rdxd` is locked up (like what
rootmy.tv/homebrew channel does on startup)

Crashes may also cause alert popups on screen if system is running in DEBUG
mode.

Crashlog dumping can be disabled by settings `SEGFAULT_SIGNALS` to empty string
before launch, like so:
```sh
SEGFAULT_SIGNALS= ./buggy-binary
```
