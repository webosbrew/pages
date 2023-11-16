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
