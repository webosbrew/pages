Title: Home
URL:
save_as: index.html
hide_title: True

<!-- Use HTML tag to skip permalink -->
<h1>webOS Homebrew Project</h1>

Welcome to webOS Homebrew Project!

We are a community centered around homebrew (unofficial software)
development for LG webOS Smart TV platform.

## What Does It Do?

Our main points of interest are:

* Building [an unofficial native app toolchain](https://github.com/webosbrew/meta-lg-webos-ndk)
* Reverse engineering and documenting [native system APIs](https://github.com/webosbrew/tv-native-apis) and other
  undocumented features
* Maintaining an independent [repository of unofficial applications](https://github.com/webosbrew/apps-repo) and
  development tools
* Building, porting and maintaining pieces of software for the platform, for example:
    - [webos-homebrew-channel](https://github.com/webosbrew/webos-homebrew-channel) - homebrew "application store"
    - [youtube-webos](https://github.com/webosbrew/youtube-webos) - YouTube TV app with extended functionalities (
      adblocking, sponsorblock)
    - [hyperion-webos](https://github.com/webosbrew/hyperion-webos) - Hyperion.NG ambilight clone video capture
    - [RetroArch](https://github.com/webosbrew/RetroArch) - console emulator frontend
    - ...and [more](https://github.com/webosbrew)

Our community has some overlap with [RootMyTV](https://rootmy.tv) and [OpenLGTV](https://openlgtv.github.io) teams, but
each has its distinct purpose (root access exploitation and low level hardware reversing, respectively).

Our main points of contact are [#homebrew channel on OpenLGTV Discord](https://discord.gg/nKQW6FPWeM)
and [#openlgtv:netserve.live](https://matrix.to/#/#openlgtv:netserve.live) Matrix channel.

## Getting Started

Currently, the easiest method of enjoying homebrew software on webOS is using Homebrew Channel, which is automatically
installed when using the [RootMyTV](https://rootmy.tv)
exploit. [Homebrew Channel](https://github.com/webosbrew/webos-homebrew-channel)
is a user friendly unofficial "application store".

If your TV is not vulnerable to the RootMyTV exploit chain, you can still
[enable Developer Mode](https://webostv.developer.lge.com/develop/app-test/using-devmode-app/) on a TV and then use
our [Device Manager app](https://github.com/webosbrew/dev-manager-desktop).

Keep in mind this has the downside of requiring "Developer Mode Session" renewal in the "Developer Mode" app every 1000 hours.
Alternatively, if you are technically profficient, a machine in a local network can periodically refresh the token for you
using a script [like one of these](https://github.com/webosbrew/dev-goodies/blob/main/reset-devmode-timer.sh).

## Find Apps

The repository of webOS homebrew applications can be viewed on the web at
[repo.webosbrew.org](https://repo.webosbrew.org). The same repository is also accessible in the Homebrew Channel app
by default.

## For Developers

* [Configuring SDK]({filename}/pages/sdk.md)
* [Native development]({filename}/pages/native.md)
* [Web development]({filename}/pages/web.md)
* Hacking
    * [Filesystem overlays]({filename}/pages/hacking/overlays.md)
    * [Hidden system settings]({filename}/pages/hacking/settings.md)
    * [Glossary]({filename}/pages/hacking/glossary.md)
* Common
    * [Logging]({filename}/pages/logging.md)
    * [Luna service bus]({filename}/pages/luna.md)
    * [appinfo.json app manifests]({filename}/pages/appinfo.md)
    * [Commands Cheatsheet]({filename}/pages/cheatsheet.md)
