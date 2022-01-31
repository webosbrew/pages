title: Glossary

<style>dt { margin-top: 1em; font-weight: bold; }</style>

This page contains common terms used in webOS hacking community and other
various uncategorized information...

NetCast / LGNC / NC
: LG's "legacy" Linux-based Smart TV platform, original target of OpenLGTV
research.

WAM / WebAppMgr
: Service responsible for running "web apps" on webOS - essentially a wrapper
around WebKit/Chrome/Blink rendering engine customized for running webOS apps.

Developer Mode / devmode
: Mode in which unsigned applications can be installed onto the system.
Developer Mode is enabled by creating `/var/luna/preferences/devmode_enabled`
path.

: This can also mean an official "Developer Mode" application that provides
limited SSH shell used for development on non-rooted devices.

Application Paths
: webOS applications are stored in:
: * `/usr/palm/applications` (default system apps),
  * `/mnt/ot*cabi/usr/palm/applications` (per-region preloaded apps),
  * `/media/cryptofs/apps/usr/palm/applications` (content store apps),
  * `/media/developer/apps/usr/palm/application` ("homebrew"/developer mode apps),
  * `/media/system/apps/usr/palm/applications` (on webOS 4.x+, a path where system application updates are installed)

Services
: Services are processes running "in the background" exposing methods/endpoints
on Luna bus. The only officially supported technology for third-party app
services development in webOS [is
NodeJS](https://webostv.developer.lge.com/develop/js-services/webos-tv-service-basics/).

Elevated Service / Service Elevation
: A non-system (homebrew) service running as root, with Luna bus permission
limitations lifted. `elevate-service` shipped with Homebrew Channel can be used
to patch up system permissions for a specific homebrew service by calling:
```sh
/media/developer/apps/usr/palm/services/org.webosbrew.hbchannel.service/elevate-service your.service.name
```

NCG
: An encryption/authentication/DRM scheme used by LG for Content Store apps.
Applications installed in `/media/cryptofs` *need* to contain a file that is
NCG-encrypted to be launchable.

Micom
: An always-on microprocessor responsible for power-on, watchdog, IR remote
handling and other similar TV features.

`tvservice`/`RELEASE`
: Before webOS 5.x a process responsible for various TV-related functionalities.
(screenshot capture, micom communication, input state monitoring...) Naming
comes from main NetCast binary. Since webOS 5.x all `tvservice` functionality
has been extracted into separate services. (eg. `micomservice`)

SDP / `lgtvsdp.com`
: LG "smart services" backend API, responsible for Content Store communication.
This is also a service that is used for TV time synchronisation. Various mock
implementations of that service has been released to keep time synchronization
working properly:
[wisq/lgtv-sdp](https://github.com/wisq/lgtv-sdp),
[zopieux/lgtv-tbc](https://github.com/zopieux/lgtv-tbc)...

`sdx`
: TV-side daemon responsible for communicating with SDP API.

`rdxd`
: TV-side "Diagnostics" daemon responsible for sending crash logs and system
logs to LGs backend.

SNU / NSU / `update`
: Networked System Update service. Queries LGs backend services for available
firmware updates. Firmware update packages are signed for a specific use - ie. a
package downloaded from SNU can't be used when provided on a USB drive and vice
versa.

SSAP / LG Connect Apps / Thinq API
: WebSocket-based API exposed on TCP port 3000/3001 by the TV, granting limited
access to Luna bus. Commonly used by home automation projects. Clients for this
protocol are available in various languages and technologies, eg:
[NodeJS](https://github.com/hobbyquaker/lgtv2),
[Python](https://github.com/bendavid/aiopylgtv),
[Web](https://github.com/Informatic/webos-ssap-web)...

Surface Manager
: Wayland compositor used by webOS - responsible for rendering of various system
overlays (eg. volume bar, cursor) and (before webOS 4.x) Home Screen.

`mrcu`
: Magic Remote Control Unit - LG's Bluetooth Low Energy-based remote control
featuring IMU-based on-screen cursor control.

GetMeIn
: webOS root exploit released in 2019 leveraging misconfigured `/dev/mem`
permissions in app jails. See [official xda-developers
thread](https://forum.xda-developers.com/t/getmein-one-time-rooting-jailbreaking-tool-for-webos-lg-tvs.3887904/). Underlying bug has been patched.

RootMyTV
: A one-click exploit released in early 2021. See [official RootMyTV
README](https://github.com/RootMyTV/RootMyTV.github.io).
