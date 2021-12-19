Title: Web development

# Official documentation
* [webOS
  TV](https://webostv.developer.lge.com/develop/overview/building-your-first-web-app-webos-tv/)

# Developer Toolbar
Web applications on webOS can be inspected using "Developer Toolbar", equivalent
to the one present in modern browsers.

This can be accessed using some different methods:

1. Running `ares-inspect APPID` with [SDK set up]({filename}/pages/sdk.md)
2. Directly accessing `http://TV_IP:9998` from a browser (equivalent to method
   1, but does not require SDK)
3. Adding `TV_IP:9998` as a "Remote Target" in `chrome://inspect` in Chrome-based
   browsers.

All these methods have some limitations in case of older webOS versions. For
example - on webOS 3.8 methods 1 and 2:

* Dev toolbar fails completely when opened in Chromium 96 (only top tab bar is
  rendered)
* "Console" is not scrollable and code cannot be injected when running in
  Firefox 94
* Works mostly fine in Midori 9.0 (webkitGTK-based browser on Linux)

Option 3 works fine, but code execution in "Console" tab does not work and
preview window seems corrupted. This also may trigger WAM crash sometimes for
some reason.

# Undocumented features

## Input/TV embedding

Web apps can embed connected inputs surface in their DOM:
```html
<video autoplay style="width:50%;height:50%">
  <source type="service/webos-external" src="ext://hdmi:1"></source>
</video>
```
Supported sources: `ext://hdmi:1`, `ext://hdmi:2`, `ext://hdmi:3`, `ext://hdmi:4`, `ext://comp:1`, `ext://av:1`, `ext://av:2`.
Additionally TV stream can be embedded with `src="tv://"` and `type="service/webos-broadcast"`

Seems like only a single external input can be displayed at the same time. (though, this may be a dependednt on used hardware)

This also works partially in system browser (content is cut off whenever status
bar is visible), but one probably should not rely on this.

## Userscripts in apps
Userscript present in [`webOSUserScripts/userScript.js`](https://github.com/webosose/wam/blob/f7c68dbeb744e8af66e4a83507b3d429dd692b2f/src/core/WebAppManagerConfig.cpp#L71-L73)
will be [loaded as a userscript](https://github.com/webosose/wam/blob/f7c68dbeb744e8af66e4a83507b3d429dd692b2f/src/core/WebPageBase.cpp#L476-L486)
in app webviews / frames, including frames in origins outside of app root.

Example application that uses this:
[webosbrew/youtube-webos](https://github.com/webosbrew/youtube-webos)
