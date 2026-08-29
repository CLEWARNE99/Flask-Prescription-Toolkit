<<<<<<< HEAD
import format
import math

def power_at(entry_dict, meridian):
    """
    This function takes a dictionary of rx values, and finds the power at the specified meridian.
    Returns power at specified meridian in list of two lists, index 0 being OD lens power, index 1 being OS lens power.
    """
    count = 0
    od_os_power = []

    #Format into 2 lists (one for OD one for OS) from dictionary
    rx_list = format.entry_consolidate(entry_dict,"sv")
    for eye in rx_list:
        # Assigning variables for readability
        sph = eye[0]
        cyl = eye[1]
        axis = eye[2]

        #Calculate power at specified meridian.
        power_calculated = round(((math.sin(math.radians(meridian - axis)) ** 2) * cyl) + sph, 2)
        od_os_power.append(power_calculated)
        count += 1
=======
import format
import math

def power_at(entry_dict, meridian):
    """
    This function takes a dictionary of rx values, and finds the power at the specified meridian.
    Returns power at specified meridian in list of two lists, index 0 being OD lens power, index 1 being OS lens power.
    """
    count = 0
    od_os_power = []

    #Format into 2 lists (one for OD one for OS) from dictionary
    rx_list = format.entry_consolidate(entry_dict,"sv")
    for eye in rx_list:
        # Assigning variables for readability
        sph = eye[0]
        cyl = eye[1]
        axis = eye[2]

        #Calculate power at specified meridian.
        power_calculated = round(((math.sin(math.radians(meridian - axis)) ** 2) * cyl) + sph, 2)
        od_os_power.append(power_calculated)
        count += 1
>>>>>>> fc25f871622db43c363b5748a77f54a75ba39ae8
    return od_os_power