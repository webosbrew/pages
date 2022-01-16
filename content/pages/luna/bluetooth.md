Title: Luna service - com.webos.service.bluetooth

Service responsible for bluetooth connectivity. Reversed on webOS 3.8. For equivalent
service on webOS 4.x and newer see `com.webos.service.bluetooth2`

"HID" here generally means Sony DualShock4 controllers.

# Methods
## `luna://com.webos.service.bluetooth/service/disconnect`
Disconnect Bluetooth device. Returns immediately

**Required permissions**: `devices`, `private`
### Request
 * [`string`] **`service`** - Service type to disconnect (supported values: `audio`, `hid`)
 * [`string`] **`address`** - Device address

### Response
 * *No information...*

## `luna://com.webos.service.bluetooth/service/connect`
Connect Bluetooth device. Returns immediately

**Required permissions**: `devices`, `private`
### Request
 * [`string`] **`service`** - Service type to disconnect (supported values: `audio`, `hid`)
 * [`string`] **`address`** - Device address

### Response
 * *No information...*

## `luna://com.webos.service.bluetooth/service/subscribeNotifications`
Subscribe to connect/disconnect events

**Required permissions**: `devices`, `private`
### Request
 * [`boolean`] **`subscribe`** - Needs to be set to true

### Response
 * [`string`] `listType` - *missing description* (supported values: `bonded`)
 * [`string`] `service` - Device service (supported values: `hid`, `audio`)
 * [`string`] `state` - Device state (supported values: `connecting`, `connected`, `disconnecting`, `disconnected`, `(null)`)
 * [`string`] `address` - Device address
 * [`string`] `name` - Device name

## `luna://com.webos.service.bluetooth/gap/getTrustedDevices`
Lists trusted devices

**Required permissions**: `devices`, `private`
### Request
 * [`string`] **`service`** - Device type category (supported values: `hid`, `audio`, `audio_sink`, `hid_kbd`, `headset`, `opc`, `ops`, `led`, `onekey`, `heartrate`, `all`)

### Response
 * [`number`] `count` - Trusted devices count
 * [`array`] `device` - Devices list
 * [`string`] `device[].name` - Device name
 * [`string`] `device[].address` - Device address
 * [`number`] `device[].deviceClass` - *missing description* (supported values: `5`)
 * [`string`] `device[].state` - *missing description* (supported values: `connected`, `disconnected`)

## `luna://com.webos.service.bluetooth/gap/findDevices`
Scan for devices

**Required permissions**: `devices`, `private`
### Request
 * [`number`] `deviceClass` - Device class to search for - 4 = audio, 5 = hid, 6 = POPO (photo printer) (supported values: `4`, `5`, `6`)
 * [`number`] `seconds` - Scan duration

### Response
 * [`string`] `scanState` - *missing description* (supported values: `device`, `done`)
 * [`object`] `device` - Found device description, only when scanState = device
 * [`string`] `device.name` - Device name
 * [`string`] `device.address` - Device address
 * [`number`] `device.deviceClass` - Device class, see above
 * [`number`] `device.rssi` - Device RSSI/link quality

## `luna://com.webos.service.bluetooth/gap/removeTrustedDevice`
Removes trusted/bonded device

**Required permissions**: `devices`, `private`
### Request
 * [`string`] **`service`** - Service type to disconnect (supported values: `audio`, `hid`)
 * [`string`] **`address`** - Device address

### Response
 * *No information...*

