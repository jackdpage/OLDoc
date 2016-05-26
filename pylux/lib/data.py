import os

LOCATIONS = {
        'home' : os.path.expanduser('~/.pylux'),
        'root' : os.path.abspath('/usr/share/pylux')}

# Priority of data locations, high to low
PRIORITY = ['home', 'root']

def get_data(path, location='auto'):
    # If location is auto, return the data from the directory with 
    # the highest priority. The general rule is the the closer to 
    # home the file is, the greater the priority
    if location == 'auto':
        for loc in PRIORITY:
            if os.path.isfile(os.path.join(LOCATIONS[loc], path)):
                return os.path.join(LOCATIONS[loc], path)
        return False
    elif location == 'all':
        paths = []
        for loc in PRIORITY:
            if os.path.isfile(os.path.join(LOCATIONS[loc], path)):
                paths.append(os.path.join(LOCATIONS[loc], path))
        return paths
    elif location in LOCATIONS:
        if os.path.isfile(os.path.join(LOCATIONS[location], path)):
            return os.path.join(LOCATIONS[location], path)
        else:
            return False
    else:
        return False
