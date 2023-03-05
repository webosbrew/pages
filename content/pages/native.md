Title: Native development

## Toolchain
Native application development is not officially supported.

An unofficial toolchain is maintained here: [webosbrew/meta-lg-webos-ndk](https://github.com/webosbrew/meta-lg-webos-ndk)

Native APIs are reverse engineered here: [webosbrew/tv-native-apis](https://github.com/webosbrew/tv-native-apis)

## Libraries
Some common Linux-world libraries and services are present on webOS devices:

 * SDL
 * OpenGL ES
 * Qt/QML
 * PulseAudio

## `argv` handling
Native apps receive a JSON object in `argv[1]` looking similar to this one:
```json
{"@system_native_app":true,"nid":"com.retroarch"}
```

When porting existing software, this probably needs to be ignored.

## Running native apps in root shell
`jailer` is an internal tool used to contain applications in their own jails.
(chroot-based containers)

In order to properly launch a native application in a root shell to see its
`stdout`/`stderr` streams, the following command needs to be executed:
```sh
# Replace my.app.id with your app id and adjust main binary path accordingly
XDG_RUNTIME_DIR=/tmp/xdg /usr/bin/jailer -t native_devmode -i my.app.id -p /media/developer/apps/usr/palm/applications/my.app.id /media/developer/apps/usr/palm/applications/my.app.id/main-binary-name '{"@system_native_app":true,"nid":"my.app.id"}' --my-extra-options
```

## Native Services
While not officially supported, Native Services can be implemented in homebrew
apps. For docs on how to achieve this check [webOS OSE documentation](https://www.webosose.org/docs/tutorials/native-services/developing-external-native-services/).

**Native services are only properly supported since webOS 4.x.** On earlier
versions service premissions are not set up properly, leading to applications
being unable to contact the service. (in these cases a service is started up,
but no method can be called) On these platforms Homebrew Channel
`elevate-service` script can be used to fixup these permissions.

For an example homebrew application that contains a Native Service check
[PicCap](https://github.com/TBSniller/piccap)/[hyperion-webos](https://github.com/webosbrew/hyperion-webos).

## Porting tips

### SDL

SDL appliactions are fairly straightforward to port. One such application is
RetroArch - see [relevant
commit](https://github.com/libretro/RetroArch/commit/20ef0667b0b59a24d54b61d7401adbca58d3cb58)
with roughly all the changes that needed to be applied for sensible port.

* For correct rendering window should be set to 1920x1080 and fullscreen
  borderless.
* Remote buttons are visible as keyboard key presses.
* Magic remote cursor is visible as a mouse, magic remote scrollwheel is visible
  as mouse wheel *with reversed orientation* to usual scrollwheels.
* It is customary to hide magic remote cursor when remote keys are pressed.
  `SDL_webOSCursorVisibility` symbol present on webOS 4.x+ can be used to set
  its visibility. On older versions cursor disable + enable presents similar
  behaviour. This usually is done via `dlsym` magic to prevent crashes on older
  versions.
* For proper behaviour `SDL_WINDOW_INPUT_FOCUS` shall be used instead of
  `SDL_WINDOW_MOUSE_FOCUS` - otherwise focus is not reenabled on non-magic
  remotes.
* In order to receive BACK and EXIT keys,
  `SDL_HINT_WEBOS_ACCESS_POLICY_KEYS_BACK` and
  `SDL_HINT_WEBOS_ACCESS_POLICY_KEYS_EXIT` hints need to be set to `true`
  apropriately.

### Wayland

Porting Wayland-native applications is a little less straightforward.

* An app needs to use `wl_webos_shell_surface_set_property` to set `appId`
  property to its application ID - otherwise surface manager/compositor will
  close the window after a couple of seconds, or not show it at all when
  launched from home screen. [See relevant webOS OSE
example](https://www.webosose.org/docs/tutorials/native-apps/developing-external-native-apps/#step-1-implement-a-native-app).
  This depends on webOS TV wayland protocol extensions. [webOS OSE
ones](https://github.com/webosose/webos-wayland-extensions/tree/9f4298a28043732dbaa5c5ca04bd766b85fad683) are not
  exactly the same, but are mostly matching what we have available on webOS
  TV. Keep in mind while `wl_webos_shell` interface seems somewhat stable,
  others have various backwards-incompatible changes introduced between
  different webOS versions and can't be relied on. Specific interfaces shall be
  inspected in `libwayland-webos-client.so` before use. [The following Ghidra
script](https://gist.github.com/Informatic/e28acada58e502540315b51b84a6f996)
  could be used for autogeneration of protocol definition for a specific
  webOS version.
* `wl_pointer_set_cursor` shall not be used since it breaks native system cursor
  and prevents mouse events from getting delivered to the application.
* `wl_output` `done` event is never emitted to the application on webOS 3.x.
  `mode` is the final event delivered and should be used as such.
* 1198 and 1199 keycode presses are delivered in `wl_keyboard` `key` event on
  native cursor show/hide (and are never released) - these should probably be
  ignored by the application.
