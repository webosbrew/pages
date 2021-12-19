Title: Luna service bus

# Undocumented services
* [`eim`]({filename}/pages/luna/eim.md) - External Input Manager

# Debugging
`ls-monitor` and `luna-send` can be used for various debugging purposes:

## Listing connected services
```sh
root@lgwebostv:~# ls-monitor -l | head
HUB CLIENTS:
PID             SERVICE NAME                    EXE                                     TYPE                    UNIQUE NAME
1173            com.webos.service.tv.teletext   /mnt/lg/tvservice/lgapp/tvservice       static                  /var/run/ls2/WFrhTp
1173            com.webos.service.tv.xpa        /mnt/lg/tvservice/lgapp/tvservice       static                  /var/run/ls2/QVmATO
2431            (null)                          /usr/sbin/MaliitServer                  unknown/client only     /var/run/ls2/SyKJDP
1400            com.webos.service.reclistmgr.list       /usr/sbin/rec-listmgr                   static                  /var/run/ls2/EpBqmE
1739            com.webos.service.nop           /usr/sbin/nopd                          static                  /var/run/ls2/PcgemZ
1173            com.webos.service.tv.program    /mnt/lg/tvservice/lgapp/tvservice       static                  /var/run/ls2/3Evy1i
```

## Listing available endpoints of a service
```sh
root@lgwebostv:~# ls-monitor -i com.webos.service.tv.teletext

METHODS AND SIGNALS REGISTERED BY SERVICE 'com.webos.service.tv.teletext' WITH UNIQUE NAME '/var/run/ls2/WFrhTp' AT HUB

  "/":
      "enableTeletext": {"provides":["private","tv.services","all"]}
      "setTeletext": {"provides":["private","tv.services","all"]}
      "getTeletextList": {"provides":["private","tv.services","all"]}
      "getTeletextState": {"provides":["private","tv.services","all"]}
      "getCurrentTeletext": {"provides":["private","tv.services","all"]}
      "isTimeAvailable": {"provides":["private","tv.services","all"]}
```

### Roles
List above contains `roles` that are allowed to call said endpoints. By default
all non-system applications can only access `public` endpoints. (and ones that
are part of its service - role names `some.service.name.group`)

`luna-send` command executed as root has access to all private and public APIs.
(`all` is a pseudo-role applied to all endpoints)

`luna-send-pub` command can only access `public` APIs - it has the same
interface as `luna-send`.

Roles/ACG summary is available in [webOS OSE
guide](https://www.webosose.org/docs/guides/development/configuration-files/acg-usage-guide/).

Dynamic role/service/client permission/api permission files on webOS TV are
stored in `/var/luna-service2` (for store-installed apps) and
`/var/luna-service2-dev` (for devmode-installed apps).

## Monitoring service/client calls
**Note:** Filtering is optional. Requests come in in chunks.

```sh
root@lgwebostv:~# ls-monitor --filter com.limelight.webosTime
Status  Prot    Type    Serial          Sender          Destination             Method                                  Payload
9938.819 TX  call       6               com.limelight.webos (/var/run/ls2/ttfuG6)       com.webos.settingsservice (/var/run/ls2/PwqnAM)         (null)          //getSystemSettings     «{"key": "localeInfo"}»
9938.832 RX call        6               com.webos.settingsservice (/var/run/ls2/PwqnAM) com.limelight.webos (/var/run/ls2/ttfuG6)               (null)          //getSystemSettings     «{"key": "localeInfo"}»
9938.837 TX  return     6               com.webos.settingsservice (/var/run/ls2/PwqnAM)         com.limelight.webos (/var/run/ls2/ttfuG6)       «{ "settings": { "localeInfo": { "clock": "locale", "keyboards": [ "en" ], "locales": { "AUD": "pl-PL", "AUD2": "en-GB", "FMT": "en-GB", "NLP": "pl-PL", "STT": "pl-PL", "TV": "en-GB", "UI": "en-GB" }, "timezone": "" } }, "subscribed": false, "method": "getSystemSettings", "returnValue": true }»
9938.838 RX return      6               com.limelight.webos (/var/run/ls2/ttfuG6)               com.webos.settingsservice (/var/run/ls2/PwqnAM) «{ "settings": { "localeInfo": { "clock": "locale", "keyboards": [ "en" ], "locales": { "AUD": "pl-PL", "AUD2": "en-GB", "FMT": "en-GB", "NLP": "pl-PL", "STT": "pl-PL", "TV": "en-GB", "UI": "en-GB" }, "timezone": "" } }, "subscribed": false, "method": "getSystemSettings", "returnValue": true }»
9939.289 TX  call       8               com.limelight.webos (/var/run/ls2/ttfuG6)       com.webos.applicationManager (/var/run/ls2/7PqtsE)              (null)          //registerNativeApp     «{"id" : "com.limelight.webos"}»
9939.291 RX call        8               com.webos.applicationManager (/var/run/ls2/7PqtsE)      com.limelight.webos (/var/run/ls2/ttfuG6)               (null)          //registerNativeApp     «{"id" : "com.limelight.webos"}»
9939.291 TX  return     8               com.webos.applicationManager (/var/run/ls2/7PqtsE)              com.limelight.webos (/var/run/ls2/ttfuG6)       «{"message":"registered","returnValue":true}»
9939.292 RX return      8               com.limelight.webos (/var/run/ls2/ttfuG6)               com.webos.applicationManager (/var/run/ls2/7PqtsE)      «{"message":"registered","returnValue":true}»
```

## Executing one-off call
```sh
root@lgwebostv:~# luna-send -n 1 -f 'luna://com.webos.applicationManager/getForegroundAppInfo' '{}'
{
    "appId": "com.limelight.webos",
    "returnValue": true,
    "windowId": "",
    "processId": ""
}
```

## Subscribing to a streaming call
```sh
root@lgwebostv:~# luna-send -i 'luna://com.webos.applicationManager/getForegroundAppInfo' '{"subscribe":true}'
{"appId":"com.limelight.webos","subscribed":true,"returnValue":true,"windowId":"","processId":""}
{"subscribed":true,"appId":"org.webosbrew.hbchannel","returnValue":true,"windowId":"","processId":""}
{"subscribed":true,"appId":"com.webos.app.hdmi3","returnValue":true,"windowId":"","processId":""}
```
