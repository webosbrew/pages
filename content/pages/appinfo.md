Title: appinfo.json

# Official documentation

 * [webOS
   TV](https://webostv.developer.lge.com/develop/references/appinfo-json) ([archive.org](https://web.archive.org/web/20230608040557/https://webostv.developer.lge.com/develop/references/appinfo-json))
 * [webOS OSE](https://www.webosose.org/docs/guides/development/configuration-files/appinfo-json/) ([archive.org](https://web.archive.org/web/20230510171556/https://www.webosose.org/docs/guides/development/configuration-files/appinfo-json/))

# Caching
SAM may cache the contents of `appinfo.json` at boot, and it is not possible to modify built-in apps before this occurs. Therefore, if you want to modify `appinfo.json` for built-in apps, you will likely have to restart `sam` for changes to take effect.

# Undocumented options
## `dialAppName` [string]
Default: none

Settings this option will expose an application available for launched via [DIAL Protocol](https://en.wikipedia.org/wiki/Discovery_and_Launch) (see: `/usr/palm/services/com.webos.service.dial`)

YouTube and Netflix apps have some special handling, but they still can be
overriden by an unofficial app.

Official YouTube app has `"dialAppName": "youtube"`. Installed apps are ordered
lexicographically based on their IDs - when multiple apps declare the same
`dialAppName` the last one will be the one triggered via DIAL.

## `noSplashOnLaunch` [boolean]
Default: `false`

Disables app splashscreen.

## `spinnerOnLaunch` [boolean]
Default: `true`

Shows a spinner if splashscreen is disabled. Set this to `false` to disable any
app launch indication.

## `defaultWindowType` [string]
Default: `card`; supported: `favoriteshows`, `favorateshows`, `floating`,
`minimal`, `popup`, `screenSaver`, `showcase`

When set to `overlay` an (web) app will be rendered above existing application.
Make sure its `background-color` is set to `transparent`.

An `overlay` app is automatically closed when opening home screen.

## `tileSize` [string]
Default: `normal`

When set to `large` tile on home screen will be twice the width.

## `visible` [boolean]
Default: `true`

Settings this to `false` will hide an application from home screen. Application
is still launchable via `com.webos.applicationmanager` calls and its services
are callablae.

## `supportGIP` [boolean]
Default: `false`

Allows application to be registered using as an [input
application]({filename}/pages/luna/eim.md).

## `trustLevel` [string]
Default: `default`

This option determines application runtime mode. By default for user-installed
applications only `default` (default) and `netcast` values are supported.

WebApps running as `netcast` have some of their APIs limited:

* `window.PalmServiceBridge` is missing
* `window.PalmSystem.launchParams` equivalent is exposed on
  `window.launchParams` instead

## `inspectable` [boolean]
Default: `true` for Developer Mode apps; `false` otherwise

Allows this app to be debugged using Chrome DevTools (`chrome://inspect`). Connect on port 9998 for non-system apps.

## `useCORSWhitelist` [string]
Specifies the name of a JSON file containing a
[CORS](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing)
whitelist configuration. A matching signature file (with the same filename
followed by `.sig`) is required. The signature is Base64-encoded, with the
underlying binary data being 256 bytes long. The signature algorithm is
currently unknown.

## `cloudgame_active` [boolean]
Default: `false`

This option allows application to handle game controller input. Since webOS 8.3.0 (FW 03.30.60), game controller input 
becomes recognized as navigation and volume control. For applications that handle game controller input, this causes
double input. Setting this option to `true` will disable this behavior.

## `vendorExtensions` [object]

### `vendorExtensions.userAgent` [string]
**Supported only in `netcast` mode**

This replaces `User-Agent` WebAppMgr browser uses. Certain dynamic replacements
are suported:

* `$browserName$` - `LG Browser`
* `$browserVersion$` - `8.00.00`
* `$platformName$` - `webOS.TV`
* `$platformVersion$` - `2016`, `2017`, ...
* `$chipSetName$` - `K3LP`, `M16`, `O20N`, ...
* `$firmwareVersion$` - `03.00.20`, ...
* `$modelName$` - `OLED48C14LB`, ...
* `$networkMode$` - `wireless`/`wired`

### `vendorExtensions.allowCrossDomain` [boolean]
**Supported only in `netcast` mode**; default: `false`

Disables HTTP CORS request validation.
