## Adding a new device ###

#### For preserving/adding the official support of a device, It should qualify the below prerequisite: ####

1. The device must be stable and should have full hardware and software compatibility.
2. The device trees should not have any external dependency and all dependencies should be ready to be opened for public.
3. The device trees should be made available to public repositories of PixysOS devices organization(s).
4. The device trees should have all the commits with proper authorship and should be ready for random inspection.
5. The device should be updated bi-weekly or monthly depending on the features update or monthly security releases.
6. You must make use of all the opt-in features and device additions which can be found [here](opt-in_features.md).
7. You should avoid making source changes through any scripts from device sources. and all the tracked repos must be from PixysOS ( contact core team members for exceptions)

#### Adding the device details to devices.json ####
The devices.json should be updated with all the needed informations as stated below. To get started open devices.json and fill up these keys accordingly.

|key|description|type|example|needed|
--- | --- | --- | --- | ---
codename|The codename of the device|string|X00TD|yes
name|The full name of the device|string|Zenfone Max Pro M1|yes
brand|The brand of the device|string|Asus|yes
fastboot| Whether your device supports fastboot builds|string|true|no
specs.battery|Battery information of the device|integer|5000|yes
specs.camera|Camera information of the device|string|13Mpx 5Mpx + 5Mpx|yes
specs.cpu|CPU information of the device|string|Snapdragon 636|yes
specs.display|Display information of the device|string|IPS 5.99\" 1080p|yes
specs.ram|RAM of the device|string|3/4GB LPDDR4X|yes
supported_bases[].name|Name of base the device supports|string|eleven|yes
supported_bases[].xda_thread|XDA thread URL of base the device supports|string|https://forum.xda-developers.com/showthread.php?t=4109811|no
supported_bases[].supported_edition|Supported build types (thirteen only supports gapps)|string|gapps|yes
status|The status to reflect of website|string|beta|no

After adding the details you may need to verify if the JSON is syntactically correct or not. To do so copy the entire devices.json with your changes and paste it [here](https://jsonformatter.curiousconcept.com/), It will check and tell you if it is correct or suggest changes to make it correct.

### How to push? ###
After adding all the device changes, Check if you want to make any changes in teams.json if yes, refer to this [section](adding_a_new_team_member.md) Alternatively, proceed to the[How to push? guide](how_to_push.md).
