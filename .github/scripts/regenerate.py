import json
import sys

api = []
print(sys.argv)
branch = sys.argv[1]
devices = json.loads(open('master/devices.json', 'r').read())
teams = json.loads(open('master/teams.json', 'r').read())

for device in devices:
    common = {}
    common['name'] = device['name']
    common['brand'] = device['brand']
    common['codename'] = device['codename']

    for supported_base in device['supported_bases']:
        collection = common
        base = supported_base['name']

        if base != branch:
            continue

        try:
            collection['xda_thread'] = supported_base['xda_thread']
        except:
            collection['xda_thread'] = ''

        mname = []
        mgithub = []

        for team in teams:
            for mdevice in team['devices']:
                if base not in mdevice['bases'] or mdevice['codename'] != common['codename']:
                    continue
                mname.append(team['full_name'])
                mgithub.append(team['github_username'])

        collection['maintainers_name'] = ', '.join(mname)
        collection['maintainers_github'] = ', '.join(mgithub)
        api.append(collection)

api = json.dumps(api, indent=3, sort_keys=False)
devices_json = open(f"{branch}/devices.json", "w")
devices_json.write(api + "\n")
devices_json.close()
