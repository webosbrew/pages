Title: Filesystem overlays

**This article assumes your TV is rooted.**

Most of webOS filesystem is read-only. All read-only partitions are stored as
**signed squashfs images**, and thus can't be "rw remounted" like it is common
on Android devices.

In order to apply system config-level changes on read-only partitions we need
to apply these at runtime.

## Replacing files/whole directories
A simple method of replacing/modifying single files is using `mount --bind`,
like so:
```sh
# Create sample override file on writable partition (/tmp is cleaned on boot so
# good for random tests...)
echo 'Hello world!' > /tmp/motd

# Replace read-only file with our customized one
mount --bind /tmp/motd /etc/motd
```

This also works for replacing whole directories, just use:
```sh
mount --bind /tmp/my-example-directory /etc/ssl/certs
```

An example of an app that uses this method is [custom screensaver](https://github.com/webosbrew/custom-screensaver/blob/main/assets/apply.sh).

## Adding files to an existing directory
If one needs to create a file that doesn't already exist, `overlayfs` may be used. The little
example here will add an additional service to the SSAP server:

```sh
# Create config overrides directory on writable partition
mkdir -p /home/root/extra-interfaces

# Create config override/addition manifest file
echo '{"service": "com.webos.service.acb","methods": [{"path": "/getForegroundAppInfo","description": "get foreground lol","requiredPermissions": ["LAUNCH"]}]}' > /home/root/extra-interfaces/com.webos.service.acb.interface

# Enable config override - this will make files present in /home/root/extra-interfaces
# show up together with existing files in /usr/palm/services/com.webos.service.secondscreen.gateway/interfaces
mount -t overlay overlay -olowerdir=/usr/palm/services/com.webos.service.secondscreen.gateway/interfaces:/home/root/extra-interfaces /usr/palm/services/com.webos.service.secondscreen.gateway/interfaces

# For this specific example - restart ssap service (it is restarted
# automatically when killed) - the name changes randomly because of [reasons]
pkill -9 -f ss.apiadapter ; pkill -9 -f ss.gateway
```

See the Linux kernel
[Overlay Filesystem documentation](https://docs.kernel.org/filesystems/overlayfs.html)
for more information. Note that `overlayfs` is not available on webOS 1, as the
kernel is too old.

## Making a whole directory writable
It is possible to make a whole directory writable by creating a writable
overlay. This is generally discouraged for homebrew use, since underlying files
may change unexpectedly on system update. However, for quick hacking/testing
this is feasible method, and, currently, the only one that allows removal of
files.

An example on how to do this, together with a handy indempotent "make sure this
directory is overlaid/writable" helper is available here:
[https://gist.github.com/Informatic/d7bcdd59eac16ffbffd3a5b5c24b4195](https://gist.github.com/Informatic/d7bcdd59eac16ffbffd3a5b5c24b4195)

## Keeping overlays persistent
Any changes we make using methods listed above **are not persistent** across
reboots by default. In order to make them such, we need to apply these on every
boot. This can be achieved by putting these commands in a script in
`/var/lib/webosbrew/init.d` directory. Executable script from that directory are
ran on startup by `run-parts` shell tool.

**Filenames of executable scripts there may only contain `a-zA-Z0-9-_` characters.**
Scripts are always ran in an ordered manner. (sorted alphabetically/
lexicographically)

Symlinks are also supported. If you are a homebrew developer **it is highly
advised** to only symlink (and **not copy**) your scripts from
application/service directory into `/var/lib/webosbrew/init.d`, to properly
handle situation when user removes said homebrew application. Symlink filename
shall consist of a two digit number prefix (used for script ordering) and a
unique app name/identifier.

Additionally `/var/lib/webosbrew/init.d` itself is not guaranteed to exist,
since it was not created by default on some Root exploits (namely RootMyTV v1).

In order to [indempotently](https://en.wikipedia.org/wiki/Idempotence) ensure
a startup script symlink exists, this snippet can be used:
```sh
mkdir -p /var/lib/webosbrew && ln -sf /media/developer/apps/usr/palm/applications/your.app.id/our-startup-script.sh /var/lib/webosbrew/init.d/50-yourappid
```

In order to remove it indempotently:
```sh
rm -rf /var/lib/webosbrew/init.d/50-yourappid
```

A practical example of how this should be handled in apps can be seen in [custom
screensaver](https://github.com/webosbrew/custom-screensaver/blob/31b95ab228d1fb0574406553f47f975f251723d3/frontend/views/MainPanel.js#L92-L96).
