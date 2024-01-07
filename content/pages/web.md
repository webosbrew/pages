Title: Web development

# Official documentation
* [webOS
  TV](https://webostv.developer.lge.com/develop/overview/building-your-first-web-app-webos-tv/)

# DevTools
Web applications on webOS can be inspected using Chromium [DevTools](https://developer.chrome.com/docs/devtools/), equivalent
to the functionality present in modern browsers.

This can be accessed using various methods:

1. Running `ares-inspect APPID` with [SDK set up]({filename}/pages/sdk.md)
2. Directly accessing `http://TV_IP:9998` from a browser (equivalent to method
   1, but does not require SDK)
3. Adding `TV_IP:9998` as a "Remote Target" in `chrome://inspect` in Chromium-based
   browsers.

All these methods have some limitations on older webOS versions. For
example, using methods 1 and 2 on webOS 3.8:

* DevTools fails completely when opened in Chromium 96 (only top tab bar is
  rendered)
* "Console" is not scrollable and code cannot be injected when running in
  Firefox 94
* Works mostly fine in Midori 9.0 (WebKitGTK-based browser on Linux)

Option 3 works fine, but code execution in the "Console" tab does not work and the
preview window seems corrupted. This also may sometimes trigger a WAM crash for
unknown reasons.

## Chromium versions
Some of the issues encountered using DevTools on older webOS versions may be
resolved by using an older release of Chromium. Specifically, according to
[LG's App Debugging documentation](https://webostv.developer.lge.com/develop/getting-started/app-debugging),
the supported versions are:  
* webOS 1&ndash;3: Chrome 38
* webOS 4&ndash;5: Chrome 68
* webOS 6+: latest version

The LG documentation links to these Chrome builds:  
* Chrome 38
  * [Windows](https://commondatastorage.googleapis.com/chromium-browser-snapshots/index.html?prefix=Win/290006/)
    ([archived `chrome-win32.zip`](https://web.archive.org/web/20240107004449/https://www.googleapis.com/download/storage/v1/b/chromium-browser-snapshots/o/Win%2F290006%2Fchrome-win32.zip?generation=1408138291841000&alt=media))
  * [macOS](https://commondatastorage.googleapis.com/chromium-browser-snapshots/index.html?prefix=Mac/306948/)
    ([archived `chrome-mac.zip`](https://web.archive.org/web/20240107004731/https://www.googleapis.com/download/storage/v1/b/chromium-browser-snapshots/o/Mac%2F306948%2Fchrome-mac.zip?generation=1417744721002000&alt=media))
  * [Linux (64-bit)](https://commondatastorage.googleapis.com/chromium-browser-snapshots/index.html?prefix=Linux_x64/320008/)
    ([archived `chrome-linux.zip`](https://web.archive.org/web/20240107004029/https://www.googleapis.com/download/storage/v1/b/chromium-browser-snapshots/o/Linux_x64%2F320008%2Fchrome-linux.zip?generation=1426035118231000&alt=media))
* Chrome 68
  * [Windows](https://commondatastorage.googleapis.com/chromium-browser-snapshots/index.html?prefix=Win/561747/)
    ([archived `chrome-win32.zip`](https://web.archive.org/web/20240107003242/https://www.googleapis.com/download/storage/v1/b/chromium-browser-snapshots/o/Win%2F561747%2Fchrome-win32.zip?generation=1527218007950356&alt=media))
  * [macOS](https://commondatastorage.googleapis.com/chromium-browser-snapshots/index.html?prefix=Mac/561749/)
    ([archived `chrome-mac.zip`](https://web.archive.org/web/20240107004529/https://www.googleapis.com/download/storage/v1/b/chromium-browser-snapshots/o/Mac%2F561749%2Fchrome-mac.zip?generation=1527219878121130&alt=media))
  * [Linux (64-bit)](https://commondatastorage.googleapis.com/chromium-browser-snapshots/index.html?prefix=Linux_x64/561747/)
    ([archived `chrome-linux.zip`](https://web.archive.org/web/20240107004029/https://www.googleapis.com/download/storage/v1/b/chromium-browser-snapshots/o/Linux_x64%2F320008%2Fchrome-linux.zip?generation=1426035118231000&alt=media))

# Undocumented features

## Input/TV embedding

Web apps can embed connected external input sources in their DOM:
```html
<video autoplay style="width:50%;height:50%">
  <source type="service/webos-external" src="ext://hdmi:1"></source>
</video>
```
Supported sources: `ext://hdmi:1`, `ext://hdmi:2`, `ext://hdmi:3`, `ext://hdmi:4`, `ext://comp:1`, `ext://av:1`, `ext://av:2`.
Additionally, a TV stream can be embedded with `src="tv://"` and `type="service/webos-broadcast"`

It seems like only a single external input can be displayed at the same time
(though this may be hardware-dependent).

This also partially works in the system browser (content is cut off whenever the
status bar is visible), but one probably should not rely on this.

## Userscripts in apps
JavaScript present in [`webOSUserScripts/userScript.js`](https://github.com/webosose/wam/blob/f7c68dbeb744e8af66e4a83507b3d429dd692b2f/src/core/WebAppManagerConfig.cpp#L71-L73)
will be [loaded as a userscript](https://github.com/webosose/wam/blob/f7c68dbeb744e8af66e4a83507b3d429dd692b2f/src/core/WebPageBase.cpp#L476-L486)
in app webviews / frames, including frames in origins outside of app root.

Example application that uses this:
[webosbrew/youtube-webos](https://github.com/webosbrew/youtube-webos)

## Inspecting non-developer apps
Apps installed from the Content Store (generally found under `/media/cryptofs`)
are not inspectable by default. You can make an app inspectable by adding
`"inspectable":true` to its `appinfo.json`.

## Inspecting system apps
It is possible to inspect system apps (i.e., those found in
`/usr/palm/applications`) on port 9999. However, this is not enabled by
default. While creating the file `/var/luna/preferences/debug_system_apps`
should enable it, our current method of maintaining root access creates issues
that require additional workarounds.
