title: Hidden system settings

`com.webos.settingsService` is responsible for persistent user-facing system
configuration. There are multiple configuration variables which are not
available anywhere in the UI.

Settings are split up into "categories", and thus will be presented like that
below.

In order to get specific setting keys this command can be used:
```sh
luna-send -f -n 1 'luna://com.webos.settingsservice/getSystemSettings' '{"category":"general", "keys": ["noSignalScreenSaver"]}'
```

In order to get all settings of a specific category:
```sh
luna-send -f -n 1 'luna://com.webos.settingsservice/getSystemSettings' '{"category":"general"}'
```

In order to set a single or multiple settings:
```sh
luna-send -f -n 1 'luna://com.webos.settingsservice/setSystemSettings' '{"category":"general", "settings": {"noSignalScreenSaver":"off"}}'
```

## Settings list

* `general`
    * `noSignalScreenSaver` [string] - `"on"`/`"off"` (default: `on`) - whether to show no signal "gallery" pictures
* `network`
    * `allowMobileDeviceAccess` [boolean] - `true`/`false` (default: `true`) - whether to expose SSAP/LG Connect Apps protocol (port 3000/3001)
* `time`
    * `autoOff15Min` [string] - `"on"`/`"off"` (default: `on`) - whether to enable auto power off after 15 minutes of inactivity on No Signal screen
