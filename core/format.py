<<<<<<< HEAD
def format_rx(rx, rx_type):
    """
    This function takes an rx, and rx type, and formats it in a string that is easily readable for user.
    Returns string for OD lens and OS lens separately.
    """
    #rx is list of 2 list; index 0 is right eye, index 1 is left.
    od_rx = rx[0]
    os_rx = rx[1]

    #Assign sph,cyl,axis vals accordingly.
    od_sph = od_rx[0]
    od_cyl = od_rx[1]

    os_sph = os_rx[0]
    os_cyl = os_rx[1]

    od_axis = int(od_rx[2])
    os_axis = int(os_rx[2])

    if rx_type == "mf":
        #If rx is a multifocal, also assign add val.
        od_add = od_rx[3]
        os_add = os_rx[3]

        #Create string in readable format.
        od_string = f"OD: {od_sph:+.2f}  {od_cyl:+.2f}  x  {od_axis} Add +{od_add:.2f}"
        os_string = f"OS: {os_sph:+.2f}  {os_cyl:+.2f}  x  {os_axis} Add +{os_add:.2f}"
    else:
        #Create string in readable format.
        od_string = f"OD: {od_sph:+.2f}  {od_cyl:+.2f}  x  {od_axis}"
        os_string = f"OS: {os_sph:+.2f}  {os_cyl:+.2f}  x  {os_axis}"

    return od_string, os_string

def validate_entry(rx_dict, rx_type):
    """
    This function validates the rx entry made by the user. It will check to make sure all fields are filled,
    and that entries for each input are appropriate.
    Returns True for a valid entry, False for invalid entry.
    """
    #Append values from rx dictionary into a list.
    values_list = []
    for entry in rx_dict:
        values_list.append(rx_dict[entry])

    #For single vision rxs...
    if rx_type == "sv":
        for index in range(len(values_list)):
            #Indices 0,2,5,7 (sign vals) should be either + or -
            if index in (0,2,5,7):
                if values_list[index] not in ("+", "-"):
                    return False
            #Indices 4 and 9 (axis vals) should be a numerical integer value between 1 and 180 (inclusive).
            elif index in (4,9):
                try:
                    int(values_list[index])
                except ValueError:
                    return False
                if float(values_list[index]) % 1 != 0 or float(values_list[index]) < 1 or float(values_list[index]) > 180:
                    return False
            #Indices 1,3,6,8 (sph and cyl vals) should be a numerical float value ending in .00, .25, .50, or .75
            elif index in (1,3,6,8):
                try:
                    float(values_list[index])
                except ValueError:
                    return False
                if (float(values_list[index]) * 100) % 100 != 0 and (float(values_list[index]) * 100) % 25 != 0 or float(values_list[index]) < 0:
                    return False

    #For multifocal rxs...
    else:
        for index in range(len(values_list)):
            #Indices 0,2,6,8 (sign vals) should be + or -
            if index in (0,2,6,8):
                if values_list[index] not in ("+", "-"):
                    return False

            #Indices 4 and 10 (axis vals) should be a numerical integer value between 1 and 180 (inclusive).
            elif index in (4,10):
                try:
                    int(values_list[index])
                except ValueError:
                    return False
                if float(values_list[index]) % 1 != 0 or float(values_list[index]) < 1 or float(values_list[index]) > 180:
                    return False

            #Indices 1,3,5,7,9,11 (sph, cyl, and add vals) should be a numerical float value ending in .00, .25, .50, or .75
            elif index in (1,3,5,7,9,11):
                try:
                    float(values_list[index])
                except ValueError:
                    return False
                if (float(values_list[index]) * 100) % 100 != 0 and (float(values_list[index]) * 100) % 25 != 0 or float(values_list[index]) < 0:
                    return False
    return True

def get_vals(request, rx_type):
    """
    This function takes a request and rx type and takes the prescription values from the request.
    Returns a dictionary with rx values.
    """
    #List of field names being taken from form in request.
    form_vals = ["sph_sign", "sph_val", "cyl_sign", "cyl_val", "axis"]
    rx_vals = {}

    #Add each OD value to dict
    for val in form_vals:
        rx_vals[f"od_{val}"] = request.form.get(f"od_{val}")

    #If multifocal, add "add" value to dict.
    if rx_type == "mf":
        rx_vals[f"od_add"] = request.form.get("od_add")

    #Add each OS value to dict
    for val in form_vals:
        rx_vals[f"os_{val}"] = request.form.get(f"os_{val}")

    #If multifocal, add "add" value to dict.
    if rx_type == "mf":
        rx_vals[f"os_add"] = request.form.get("os_add")

    return rx_vals

def entry_consolidate(rx_dict, rx_type):
    """
    This function consolidates from a dictionary into a list.
    Returns a list of 2 lists, index 0 being OD lens, index 1 being OS lens.
    """
    #Initialize lists for od, os, and list to return.
    rx_od_list = []
    rx_os_list = []
    od_os_consolidated = [[],[]]
    count = 0

    #If key starts with "OD", add to od list, otherwise add to os list.
    for k in rx_dict:
        if k[0:2] == "od":
            rx_od_list.append(rx_dict[k])
        else:
            rx_os_list.append(rx_dict[k])

    for eye in [rx_od_list,rx_os_list]:
        #Assigning variables to list item names for readability
        sph_sign = eye[0]
        sph_val = float(eye[1])
        cyl_sign = eye[2]
        cyl_val = float(eye[3])
        axis = float(eye[4])

        #Combine sign with numerical value for sph and cyl.
        if sph_sign == "+":
            sph = sph_val
        else:
            sph = sph_val * -1
        if cyl_sign == "+":
            cyl = cyl_val
        else:
            cyl = cyl_val * -1

        #Append each value.
        od_os_consolidated[count].append(sph)
        od_os_consolidated[count].append(cyl)
        od_os_consolidated[count].append(axis)

        if rx_type == "mf":
            add = float(eye[5])
            od_os_consolidated[count].append(add)

        #Increment count to add to list in index 1 of return list.
        count += 1
=======
def format_rx(rx, rx_type):
    """
    This function takes an rx, and rx type, and formats it in a string that is easily readable for user.
    Returns string for OD lens and OS lens separately.
    """
    #rx is list of 2 list; index 0 is right eye, index 1 is left.
    od_rx = rx[0]
    os_rx = rx[1]

    #Assign sph,cyl,axis vals accordingly.
    od_sph = od_rx[0]
    od_cyl = od_rx[1]

    os_sph = os_rx[0]
    os_cyl = os_rx[1]

    od_axis = int(od_rx[2])
    os_axis = int(os_rx[2])

    if rx_type == "mf":
        #If rx is a multifocal, also assign add val.
        od_add = od_rx[3]
        os_add = os_rx[3]

        #Create string in readable format.
        od_string = f"OD: {od_sph:+.2f}  {od_cyl:+.2f}  x  {od_axis} Add +{od_add:.2f}"
        os_string = f"OS: {os_sph:+.2f}  {os_cyl:+.2f}  x  {os_axis} Add +{os_add:.2f}"
    else:
        #Create string in readable format.
        od_string = f"OD: {od_sph:+.2f}  {od_cyl:+.2f}  x  {od_axis}"
        os_string = f"OS: {os_sph:+.2f}  {os_cyl:+.2f}  x  {os_axis}"

    return od_string, os_string

def validate_entry(rx_dict, rx_type):
    """
    This function validates the rx entry made by the user. It will check to make sure all fields are filled,
    and that entries for each input are appropriate.
    Returns True for a valid entry, False for invalid entry.
    """
    #Append values from rx dictionary into a list.
    values_list = []
    for entry in rx_dict:
        values_list.append(rx_dict[entry])

    #For single vision rxs...
    if rx_type == "sv":
        for index in range(len(values_list)):
            #Indices 0,2,5,7 (sign vals) should be either + or -
            if index in (0,2,5,7):
                if values_list[index] not in ("+", "-"):
                    return False
            #Indices 4 and 9 (axis vals) should be a numerical integer value between 1 and 180 (inclusive).
            elif index in (4,9):
                try:
                    int(values_list[index])
                except ValueError:
                    return False
                if float(values_list[index]) % 1 != 0 or float(values_list[index]) < 1 or float(values_list[index]) > 180:
                    return False
            #Indices 1,3,6,8 (sph and cyl vals) should be a numerical float value ending in .00, .25, .50, or .75
            elif index in (1,3,6,8):
                try:
                    float(values_list[index])
                except ValueError:
                    return False
                if (float(values_list[index]) * 100) % 100 != 0 and (float(values_list[index]) * 100) % 25 != 0 or float(values_list[index]) < 0:
                    return False

    #For multifocal rxs...
    else:
        for index in range(len(values_list)):
            #Indices 0,2,6,8 (sign vals) should be + or -
            if index in (0,2,6,8):
                if values_list[index] not in ("+", "-"):
                    return False

            #Indices 4 and 10 (axis vals) should be a numerical integer value between 1 and 180 (inclusive).
            elif index in (4,10):
                try:
                    int(values_list[index])
                except ValueError:
                    return False
                if float(values_list[index]) % 1 != 0 or float(values_list[index]) < 1 or float(values_list[index]) > 180:
                    return False

            #Indices 1,3,5,7,9,11 (sph, cyl, and add vals) should be a numerical float value ending in .00, .25, .50, or .75
            elif index in (1,3,5,7,9,11):
                try:
                    float(values_list[index])
                except ValueError:
                    return False
                if (float(values_list[index]) * 100) % 100 != 0 and (float(values_list[index]) * 100) % 25 != 0 or float(values_list[index]) < 0:
                    return False
    return True

def get_vals(request, rx_type):
    """
    This function takes a request and rx type and takes the prescription values from the request.
    Returns a dictionary with rx values.
    """
    #List of field names being taken from form in request.
    form_vals = ["sph_sign", "sph_val", "cyl_sign", "cyl_val", "axis"]
    rx_vals = {}

    #Add each OD value to dict
    for val in form_vals:
        rx_vals[f"od_{val}"] = request.form.get(f"od_{val}")

    #If multifocal, add "add" value to dict.
    if rx_type == "mf":
        rx_vals[f"od_add"] = request.form.get("od_add")

    #Add each OS value to dict
    for val in form_vals:
        rx_vals[f"os_{val}"] = request.form.get(f"os_{val}")

    #If multifocal, add "add" value to dict.
    if rx_type == "mf":
        rx_vals[f"os_add"] = request.form.get("os_add")

    return rx_vals

def entry_consolidate(rx_dict, rx_type):
    """
    This function consolidates from a dictionary into a list.
    Returns a list of 2 lists, index 0 being OD lens, index 1 being OS lens.
    """
    #Initialize lists for od, os, and list to return.
    rx_od_list = []
    rx_os_list = []
    od_os_consolidated = [[],[]]
    count = 0

    #If key starts with "OD", add to od list, otherwise add to os list.
    for k in rx_dict:
        if k[0:2] == "od":
            rx_od_list.append(rx_dict[k])
        else:
            rx_os_list.append(rx_dict[k])

    for eye in [rx_od_list,rx_os_list]:
        #Assigning variables to list item names for readability
        sph_sign = eye[0]
        sph_val = float(eye[1])
        cyl_sign = eye[2]
        cyl_val = float(eye[3])
        axis = float(eye[4])

        #Combine sign with numerical value for sph and cyl.
        if sph_sign == "+":
            sph = sph_val
        else:
            sph = sph_val * -1
        if cyl_sign == "+":
            cyl = cyl_val
        else:
            cyl = cyl_val * -1

        #Append each value.
        od_os_consolidated[count].append(sph)
        od_os_consolidated[count].append(cyl)
        od_os_consolidated[count].append(axis)

        if rx_type == "mf":
            add = float(eye[5])
            od_os_consolidated[count].append(add)

        #Increment count to add to list in index 1 of return list.
        count += 1
>>>>>>> fc25f871622db43c363b5748a77f54a75ba39ae8
    return od_os_consolidated