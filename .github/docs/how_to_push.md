## How to push ##
If you have reached this page means you have made certain changes and now you want to push it for review. At this stage we assume you have gone though the terms and condtions mentioned in agreements of modfying devices.json ([agreement](adding_a_new_device.md)) or teams.json ([agreement](adding_a_new_team_member.md)). If not then you may check those first.

#### Gerrit setup ####
If its your first time dealing with gerrit then you can find the docs for gerrit setup [here](https://github.com/PixysOS/Pixys_doc/blob/eleven/gerrit-config.md).

#### Next step ####
If you are ready with all your changes and your gerrit setup then you are ready for your next step i.e pushing.
1. Stage your changes
```
git add devices.json
git add teams.json
```
2. Commit and hook your commit
```
gitdir=$(git rev-parse --git-dir)
scp -p -P 29418 <YourGerritUsername>@gerrit.pixysos.com:hooks/commit-msg ${gitdir}/hooks/
git commit -m "official_devices: <your message>"
```
3. Push your changes
```
git push ssh://<YourGerritUserName>@gerrit.pixysos.com:29418/PixysOS/official_devices HEAD:refs/for/master
```
