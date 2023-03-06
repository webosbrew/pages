Title: Luna service - com.webos.service.eim

# Methods
## `luna://com.webos.service.eim/addDevice`
Registers an application as an input. `"supportGIP": true` needs to be set in application manifest for this to work.

**Required permissions**: `devices`, <u>`public`</u>, `private`
### Request
 * [`string`] **`appId`** - Application to be registered as an input device. Does not need to be equal to calling application.
 * [`string`] **`pigImage`** - Image rendered in "Input Hub" app, relative to main application directory. Can be set to empty string. eim crashes when this field is missing.
 * [`string`] **`mvpdIcon`** - ???; Required before webOS 3.x, can be set to empty string.
 * [`string`] `type` - *missing description* (supported values: `MVPD_IP`, `MVPD_RF`)
 * [`boolean`] `showPopup` - Show a popup notification that an application has been registered.
 * [`string`] `label` - Application name used in notification popup.
 * [`string`] `description` - Description rendered in Input Hub

### Response
 * *No information...*

## `luna://com.webos.service.eim/deleteDevice`
Removes an application from inputs list.

**Required permissions**: `devices`, <u>`public`</u>, `private`
### Request
 * [`string`] **`appId`** - Application to be removed from inputs list.

### Response
 * *No information...*

