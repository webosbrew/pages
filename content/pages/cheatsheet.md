Title: Commands Cheatsheet

This is a list of various commands commonly used during debugging/hacking.

```sh
# Monitor suspend / resume state
luna-send -i 'luna://com.webos.service.tvpower/power/getPowerState' '{"subscribe":true}'

# Check currently running application
luna-send -i 'luna://com.webos.applicationManager/getForegroundAppInfo' '{"subscribe":true}'

# Poke configd options (does not persist through reboots)
luna-send -n 1 -f luna://com.webos.service.config/setConfigs '{"configs": {"system.collectDevLogs": true}}'

# Disable 15 minute no-signal auto power off
luna-send -n 1 luna://com.webos.settingsservice/setSystemSettings '{"settings":{"autoOff15Min":"off"},"category":"time"}'

# Launch app
luna-send -n 1 -f luna://com.webos.service.applicationManager/launch '{"id":"com.webos.app.something", "params": {"key": "value"}}'

# Close app
luna-send -n 1 'luna://com.webos.service.applicationManager/closeByAppId' '{"id":"com.webos.app.hdmi3"}'

# Launch energy saving screen
luna-send-pub -f -n 1 luna://com.webos.service.applicationManager/launch '{"id":"com.webos.app.tvhotkey","params":{"activateType":"energy-saving-mode"}}'

# Screen backlight control
luna-send -n 1 "luna://com.webos.service.tvpower/power/turnOnScreen" '{}'
luna-send -n 1 "luna://com.webos.service.tvpower/power/turnOffScreen" '{}'
luna-send -n 1 'luna://com.webos.settingsservice/setSystemSettings' '{"category":"picture","settings":{"energySaving":"screen_off"}}'
```

## Screenshots
```sh
# Note: com.webos.service.tv.capture below has been renamed to com.webos.service.capture on some devices, call signature is the same.

luna-send -n 1 -f 'luna://com.webos.service.tv.capture/executeOneShot' '{"path":"/tmp/capture.png","method":"DISPLAY","format":"PNG"}'
# Supported formats: BMP, JPG, PNG, RGB, RGBA, YUV422
# Supported methods: SCREEN/DISPLAY (alias?), SCREEN_WITH_SOURCE_VIDEO, VIDEO, GRAPHIC, SOURCE/SCALER (alias?)
```

## Factorywin app (ezAdjust/inStart/inStop)
```sh
luna-send -n 1 -f luna://com.webos.service.applicationManager/launch '{"id":"com.webos.app.factorywin","params":{"id":"executeFactory","irKey":"inStart"}}'
# Alternative irKeys: powerOnly, inStart, ezAdjust, inStop, pCheck, sCheck, tilt

# ezAdjust is service menu 1
# inStart is service menu 2
# inStop is factory reset (?)
# pCheck will override some picture settings for lcd testing
# sCheck will boost sound to test audio
# tilt opens white screen that does nothing and locks remote buttons, goes away after a reboot

# Password: 0413
# Bang & Olufsen password: 1925
# "USB Log" (?) password: 1126
```
