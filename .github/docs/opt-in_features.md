## These are the features maintainers should opt in unless its unsupported by their device ##

1. New gen assitant
```
TARGET_SUPPORTS_NEXT_GEN_ASSISTANT := true
```
2. Google Recorder
```
TARGET_SUPPORTS_GOOGLE_RECORDER := true
```
3. Google live wallpapers
```
TARGET_INCLUDE_LIVE_WALLPAPERS := true
```
4. Quick Tap Gesture
```
TARGET_SUPPORTS_QUICK_TAP := true
```
6. AR core
```
TARGET_INCLUDE_STOCK_ARCORE := true
```

## These are the features maintainers could opt in if its supported by their device ##

1. audio panel location to left by default (SystemUI)

```
<bool name="config_audioPanelOnLeftSide">true</bool>
```
2. Max visible notification icons  (SystemUI)
```
<integer name="config_maxVisibleNotificationIcons"></integer>
<integer name="config_maxVisibleNotificationIconsOnLock"></integer>
```
3. device specific key handlers (Framework)
```
<string-array name="config_deviceKeyHandlerLibs" translatable="false"></string-array>
<string-array name="config_deviceKeyHandlerClasses" translatable="false"></string-array>
```
4. Alert slider (Framework)
```
<bool name="config_hasAlertSlider">true</bool>
```
5. Boost framework from CLO  (Framework)
```
<bool name="config_supportsBoostFramework">true</bool>
```
6. Min/Max Refresh Rate (Settings)
```
<bool name="config_show_refresh_rate_controls">true</bool>
```

## Additional Rules ##

1. All the above mentioned overlays should be defined in respective dir with pixys suffix
2. All the flags should be kept in pixys_$(device).mk
3. For additional changes you need for device additions push to gerrit or contact team members
4. For authorship it is recommened to stick to the author of the feature (check source for info)
5. Avoid overriding any build fingerprint/description unless cts is broken by default
6. Inherit updatable apex for all the supported devices ( we supports play system updates)
7. Only one camera app is permitted to be shipped (e.g., Google Camera or the camera app from the device manufacturer), and it must be tracked from Pixys GitLab. Additionally, the below flag could be set to exclude Aperture. (For devices such as OnePlus/Nothing Camera, separate flags are required , refer to the platform for more information).

```
TARGET_INCLUDE_OEM_CAMERA := true
```
