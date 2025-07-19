import SystemVariables

def take_picture():
    pass

def take_video():
    pass

def increase_volume(amt):
    SystemVariables.volume = min(amt + SystemVariables.volume, 1.0)

def decrease_volume(amt):
    SystemVariables.volume = min(amt + SystemVariables.volume, 1.0)
