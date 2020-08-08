import json, sys, time

# const
device_keys = ['name', 'brand', 'codename', 'specs']
team_keys = ['full_name', 'country', 'github_username']

try:
    devices = json.loads(open('../../devices.json').read())
except:
    print('Cannot load devices.json properly, Try again after correcting the format.')
    time.sleep(5)
    sys.exit(1)

try:
    teams = json.loads(open('../../teams.json').read())
except:
    print('Cannot load teams.json properly, Try again after correcting the format.')
    time.sleep(5)
    sys.exit(1)

for device in devices:
    keys = list(device.keys())
    check = all(x in keys for x in device_keys) and len(device_keys)<len(keys)
    if not check:
        print('Cannot find the needed key params in the below json')
        print(json.dumps(device))
        print('\nThe needed keys are ' + str(device_keys))
        time.sleep(5)
        sys.exit(1)

for team in teams:
    keys = list(team.keys())
    check = all(x in keys for x in team_keys) and len(team_keys)<len(keys)
    if not check:
        print('Cannot find the needed key params in the below json')
        print(json.dumps(team))
        print('\n\nThe needed keys are ' + str(team_keys))
        time.sleep(5)
        sys.exit(1)

print('Validator process completed, Both the json\'s seem to be correct as per requested format and needed syntax.')
time.sleep(2)
sys.exit(0)