Title: Rooting Your webOS TV
save_as: rooting/index.html

## Should I Root or Not?

Before rooting your TV, please think about what you would like to do with a rooted TV.

Use Kodi? That doesn't require root.

Stream PC games with Moonlight? That doesn't require root either.

For many uses, like installing some useful homebrew applications, root is **NOT** required.
Using developer mode is enough most of the time and not hard to set up either.
It requires an account though, and you'll have to renew the developer mode every
1000 hours.

However, an ambilight setup with
[PicCap](https://github.com/TBSniller/piccap)/[Hyperion](https://github.com/webosbrew/hyperion-webos)/[HyperHDR](https://github.com/webosbrew/hyperhdr-webos-loader)
*will* require root.

Remapping remote control buttons with [lginputhook](https://github.com/Simon34545/lginputhook) requires root.

Keeping Kodi's `.kodi` directory on a USB drive also requires root.

### Benefits of Rooting

* No developer mode needed anymore - No need to worry about the dev mode timer or an LG account
* Gain more control over your TV - Block ads and auto-updates
* Increase privacy - Disable telemetry
* More modifications - Custom wallpaper, screensaver, ambient lighting, etc.
* Access webOS internals - Useful for researching and exploring the Linux system underlying webOS

### Caveats of Rooting

* Methods may get patched by LG - If you apply firmware updates, you may lose any homebrew apps and mods you've installed
* Rooting is safe, but reckless changes are not - You could brick your TV if you don't have proper knowledge and ignore **[warnings](https://rootmy.tv/warning)**

## How Do I Use Homebrew Apps Without Root?

Using [dev-manager-desktop](https://github.com/webosbrew/dev-manager-desktop) makes this pretty easy.

<img src="https://user-images.githubusercontent.com/830358/215523117-0fdbde24-a503-4eed-8e2f-50a3486ce7f7.png" alt="Install from webOS Homebrew repo" title="Install from webOS Homebrew repo" width="70%">

## I Want Root Anyway!

As of February 2024, LG has released multiple patches for the vulnerabilities we found.
Depending on the firmware and model, there are multiple approaches to rooting a webOS TV.

- [RootMy.TV](https://rootmy.tv/) - For webOS 3.4 and up, but very likely patched (read the [README](https://github.com/RootMyTV/RootMyTV.github.io?tab=readme-ov-file#readme) first!)
- [crashd](https://gist.github.com/throwaway96/e811b0f7cc2a705a5a476a8dfa45e09f) - For webOS 4.0 and up; patches being rolled out
- [WTA](https://gist.github.com/throwaway96/b171240ef59d7f5fd6fb48fc6dfd2941) - For webOS 5 and up; patches being rolled out
- [DEBUG via
  NVM](https://gist.github.com/throwaway96/827ff726981cc2cbc46a22a2ad7337a1) - Works on all webOS versions prior to 4.0 (plus NetCast/GP) but requires opening up the TV (no permanent hardware modifications)
- GetMeIn - May work on webOS up to 3.4 on certain models, but don't use the original binary from the XDA thread
