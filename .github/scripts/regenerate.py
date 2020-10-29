import os
import sys
import json
import requests
import operator

SUGGESTIONS = []
ALLOWED_BASES = ['eleven', 'ten']
DEVICES_KEYS = ['codename', 'brand', 'name', 'specs', 'supported_bases']
TEAMS_KEYS = ['full_name', 'country', 'github_username',
              'telegram_username', 'xda_url', 'donate_url', 'core_team', 'devices']


def test_integrity_devices():
    try:
        devices = json.loads(open('devices.json', 'r').read())
    except:
        SUGGESTIONS.append('devices.json is not a valid JSON.')
        return

    for device in devices:
        device_index = devices.index(device)
        if 'name' not in device:
            SUGGESTIONS.append(
                f"'name' key not found in devices.json for device index value {device_index}")

        if 'brand' not in device:
            SUGGESTIONS.append(
                f"'brand' key not found in devices.json for device index value {device_index}")

        if 'codename' not in device:
            SUGGESTIONS.append(
                f"'codename' key not found in devices.json for device index value {device_index}")

        if 'supported_bases' not in device:
            SUGGESTIONS.append(
                f"'supported_bases' key not found in devices.json for index value {device_index}")
            continue

        supported_bases = device['supported_bases']
        for supported_base in supported_bases:
            base_index = supported_bases.index(supported_base)
            if 'name' not in supported_base:
                SUGGESTIONS.append(
                    f"'name' key not found in devices.json for device index value {device_index} and base index value {base_index}")

            if supported_base['name'] not in ALLOWED_BASES:
                SUGGESTIONS.append(
                    f"'name' key has a value that is not allowed in devices.json for device index value {device_index} and base index value {base_index}")


def test_integrity_teams():
    try:
        teams = json.loads(open('teams.json', 'r').read())
    except:
        SUGGESTIONS.append('teams.json is not a valid JSON.')
        return

    for member in teams:
        member_index = teams.index(member)
        if 'full_name' not in member:
            SUGGESTIONS.append(
                f"'name' key not found in teams.json for member index value {member_index}")

        if 'country' not in member:
            SUGGESTIONS.append(
                f"'country' key not found in teams.json for member index value {member_index}")

        if 'github_username' not in member:
            SUGGESTIONS.append(
                f"'github_username' key not found in teams.json for member index value {member_index}")

        if 'devices' not in member:
            SUGGESTIONS.append(
                f"'devices' key not found in teams.json for member index value {member_index}")
            continue

        devices = member['devices']
        for device in devices:
            device_index = devices.index(device)
            if 'codename' not in device:
                SUGGESTIONS.append(
                    f"'codename' key not found in core.json for member index value {member_index} and device index value {device_index}")

            if 'bases' not in device:
                SUGGESTIONS.append(
                    f"'bases' key not found in core.json for member index value {member_index}")
                continue

            bases = device['bases']
            for base in bases:
                base_index = bases.index(base)

                if base not in ALLOWED_BASES:
                    SUGGESTIONS.append(
                        f"'bases' key has a value that is not allowed in teams.json for device index value {device_index} and base index value {base_index} and member index value {member_index}")


def format_json():
    # Load JSON's
    devices = json.loads(open('devices.json', 'r').read())
    teams = json.loads(open('teams.json', 'r').read())

    # Sort JSON alphabatically with selected keys
    devices = sorted(devices, key=operator.itemgetter('codename', 'brand'))
    teams = sorted(teams, key=operator.itemgetter('full_name', 'country'))

    # Filter the unwanted keys in devices.json
    for device in devices:
        ndevice = {}
        for key in DEVICES_KEYS:
            try:
                ndevice[key] = device[key]
            except:
                pass
        index = devices.index(device)
        devices[index] = ndevice

    # Filter the unwanted keys in teams.json
    for team in teams:
        nteam = {}
        for key in TEAMS_KEYS:
            try:
                nteam[key] = team[key]
            except:
                pass
        index = teams.index(team)
        teams[index] = nteam

    # Dump them
    devices = json.dumps(devices, indent=3, sort_keys=False)
    teams = json.dumps(teams, indent=3, sort_keys=False)

    # Open JSON's in write mode
    devices_json = open('devices.json', 'w')
    teams_json = open('teams.json', 'w')

    # Write dump's
    devices_json.write(devices + '\n')
    teams_json.write(teams + '\n')

    # Close JSON's
    devices_json.close()
    teams_json.close()
    return 0


def main():
    print('Running Integrity tests for all the JSON\'s.')
    test_devices = test_integrity_devices()
    test_team = test_integrity_teams()

    if len(SUGGESTIONS) > 0:
        print('Integrity test for one or more JSON\'s failed. Cannot proceed with JSON formatter.\n\n')
        print('Below might be the reasons for test failure:\n')
        for SUGGESTION in SUGGESTIONS:
            print('-', SUGGESTION)
        sys.exit(1)
    else:
        print('Integrity test passed successfully. Now formatting all the JSON\'s')
        format_json()
        print('Formatting JSON\'s completed.')
        sys.exit(0)


if __name__ == "__main__":
    main()
