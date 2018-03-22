""" Running this script will prompt the user to select from a list of detected microphones.
    The selected device fill be logged in a file 'config.ini'"""

import pyaudio
import configparser
import os
from pathlib import Path

_path = Path(os.path.dirname(os.path.abspath( __file__ )))


def load_ini():
    """ Returns the saved device from config.ini or `None`

            Returns
            -------
            Union[dict, None]
                {name : device name,
                 index: device index from config prompt}"""
    config = configparser.ConfigParser()

    # This returns an empty array if no config file was found
    if config.read(str(_path / 'config.ini')) != []:
        return config['input device']
    else:
        return None


def get_input_devices():
    """ Use pyaudio to detect available mic-devices.

        Returns
        -------
        List[dict]
            Device logs - each is a dictionary containing the name and default-config details of
            the device."""
    p = pyaudio.PyAudio()
    devices = [p.get_device_info_by_index(index) for index in range(0, p.get_device_count())]
    inputDevices = [device for device in devices if device['maxInputChannels'] > 0]
    return inputDevices


def present_menu(devices, savedDevice=None):
    """ Format the menu of selectable microphones and receive selection from user.

        Parameters
        ----------
        devices : List[dict]
            Device logs for detected microphones

        savedDevice : Optional[dict]
             The device log for the saved device - used to indicate on the menu the current
             saved device.

        Returns
        -------
        dict
            The device log for the user-selected device."""
    # Print the menu
    menuIndex = 0
    for device in devices:
        # If the user previously saved a device, indicate that in the menu with an asterisk
        isSavedSelection = int(savedDevice['index']) == device['index'] if savedDevice is not None else False
        savedSelectionText = '*' if isSavedSelection else ' '
        
        print('{}) {} {}'.format(str(menuIndex), savedSelectionText, device['name']))
        menuIndex = menuIndex + 1

    # Get the user's input and select the input device
    inputValid = False
    menuSelection = 0
    while not inputValid:
        menuInput = input(" >> ").strip()
        if menuInput.isdecimal():
            menuSelection = int(menuInput)
            if menuSelection <= menuIndex:
                inputValid = True
            else:
                print("invalid input")
        else:
            print("invalid input")
    return devices[menuSelection]


def save_ini(selectedDevice):
    """ Saves device to songfp/mic_config/config.ini

        Parameters
        ----------
        selectedDevice : dict
            {name : device name,
             index: device index from config prompt}"""
    config = configparser.ConfigParser()
    config['input device'] = {
        'name': selectedDevice['name'],
        'index': selectedDevice['index']
    }
    with open(os.path.join(_path, 'config.ini'), 'w') as configfile:
        config.write(configfile)


if __name__ == '__main__':
    # Prompt user to select mic
    savedDevice = load_ini()
    inputDevices = get_input_devices()
    selectedDevice = present_menu(inputDevices, savedDevice)
    print("'{}' selected as input device".format(selectedDevice['name']))
    save_ini(selectedDevice)
