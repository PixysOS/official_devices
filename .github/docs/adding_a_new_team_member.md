# Adding a new team member #
There are different set of requirements for being the part of core team or maintainer's team.

#### Things you need to secure your stay in maintainers team ####
1. Before applying you must have done atleast one unoffical build for atleast one week.
2. You must own the device you wish to maintain. And you should test your builds properly before every release.
3. The device you maintain should following the agreement mentioned [here](adding_a_new_device.md).
4. You must have a good knowledge of using git, github, gerrit. Also ensure all commits you made or you are going to make after being the part should be properly authored and properly documented.
5. As a device maintainer, You should update your device regularly. And you hold the responsibilty to ensure every build is properly tested and is bug-free.
6. You must be a part of the telegram groups and channels.
7. You must be well mannered and co operative to your co-maintainers, administrators and most importantly to your users. Any instance of hateful speech or flame war comes under the notice of any administrator or team member then you may need to have a proper explaination to show that you did it for a valid reason to save your postion in the project, Excepting that PixysOS does not believe/support in any type of beheviour that involves hate or abuse.

#### Things you need to secure your stay in core team ####
1. You must follow the rule 6 & 7 from maintainers guideline.
2. You must have been the part of the project for a certain time.
3. You must have contributed to the project in anyway. Ex. it maybe community administrator, designer, main source helper or even maintainers moderator etc.
4. Most importantly the project lead should approve your/to-be designated position.

#### Adding your details to teams.json ####
The teams.json should be updated with all the needed informations as stated below.
To get started open teams.json and fill up these keys accordingly.

|key|description|type|example|needed|
--- | --- | --- | --- | ---
full_name|Your full name|string|Subins Mani|yes
country|The country you live in|string|IN|yes
github_username|Your github username|string|subinsmani|yes
telegram_username|Your telegram username|string|subinsmani|no
xda_url|Your XDA url|string|https://forum.xda-developers.com/member.php?u=7868666|no
devices[].bases[]|The bases you maintain for your device|string|eleven|yes
devices[].codename|The codename of device you maintain|string|avicii|yes

After adding the details you may need to verify if the JSON is syntactically correct or not. To do so copy the entire teams.json with your changes and paste it [here](https://jsonformatter.curiousconcept.com/), It will check and tell you if it is correct or it will suggesst you the changes to make it correct.

### How to push? ###
After adding all the device changes, Check if you want to make any changes in devices.json if yes then head into this [section](adding_a_new_device.md) or you can proceed to [How to push? guide](how_to_push.md).
