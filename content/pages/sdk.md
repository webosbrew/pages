Title: Configuring SDK
status: hidden

# Development TV setup

Recommended tooling for webOS TV development is
[@webosose/ares-cli](https://www.npmjs.com/package/@webosose/ares-cli) NPM
package. It provides all the basic tools without needing to install them
globally.

**If your TV is rooted** You *shall not* use "Developer Mode" app - all of its
functionality is accessible via root SSH server exposed by Homebrew Channel, and
installing it will probably break root startup sequence.

## Configuring @webosose/ares-cli with Developer Mode App
This is partially based on: https://webostv.developer.lge.com/develop/app-test/using-devmode-app/

1. Install Developer Mode app from Content Store
2. Enable developer mode, enable keyserver
3. Download TV's private key: `http://TV_IP:9991/webos_rsa` and save under `$HOME/.ssh`
4. As with any SSH key, restrict its access rights: `chmod 600 ~/.ssh/webos_rsa`
5. You can test the key with: `ssh-keygen -y -P "PASSPHRASE" -f ~/.ssh/webos_rsa`
6. Configure the device using `ares-setup-device` (`-a` may need to be replaced with `-m` if device named `webos` is already configured)
    * `PASSPHRASE` is the 6-character passphrase printed on screen in developer mode app
```sh
ares-setup-device -a webos -i "username=prisoner" -i "privatekey=webos_rsa" -i "passphrase=PASSPHRASE" -i "host=TV_IP" -i "port=9922"
```

## Configuring @webosose/ares-cli with rooted TV
1. Enable sshd in Homebrew Channel app
2. Generate ssh key on developer machine (`ssh-keygen`)
3. Copy the public key (`id_rsa.pub`) to `/home/root/.ssh/authorized_keys` on TV
4. Configure the device using `ares-setup-device` (`-a` may need to be replaced with `-m` if device named `webos` is already configured)
```sh
ares-setup-device -a webos -i "username=root" -i "privatekey=id_rsa" -i "passphrase=SSH_KEY_PASSPHRASE" -i "host=TV_IP" -i "port=22"
```

**Note:** @webosose/ares-cli doesn't need to be installed globally - you can use a package installed in a local project directory by just prefixing above commands with local path, like so: `node_modules/.bin/ares-setup-device ...`

## Configuring VSCode Extension
1. Load https://marketplace.visualstudio.com/items?itemName=webOSOSESDK.webosose into your VSCode
2. The Extension will prompt you to install needed npm Packages. This will probably fail depending on your VSCode setup due to permissions - run the commands manually in a root shell (```npm install @webosose/ares-cli```)
3. Setup Key auth with your TV
4. run ``` ares-setup-device ``` and use your VSCode terminals ssh private key (`id_rsa`)
5. refresh the Known Devices Tab, you should see your new TV listed.

## Using SSH without SDK on unrooted devices
Public key fetched using the method above can be used to connect to the TV using
plain SSH client:
```sh
ssh -i webos_rsa -p 9922 prisoner@TV_IP
```

Note: non-rooted prisoner user does not have access to PTS, and thus `bash` will
behave strangely
