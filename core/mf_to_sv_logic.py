<<<<<<< HEAD
import format

def mf_to_sv(entry_dict, convert_type):
    """
    This function takes a dictionary of multifocal rx values, and converts them into a single vision prescription
    depending on convert_type.
    Returns converted rx in a list of 2 lists, index 0 being OD lens, index 1 being OS lens.
    """
    #If convert type is dr_svd (Distance/Reading to Single Vision Distance)...
    if convert_type == "dr_svd":
        od_os_converted = [[],[]]
        count = 0
        #Format into 2 lists (one for OD one for OS) from dictionary
        rx_list = format.entry_consolidate(entry_dict,"mf")
        for eye in rx_list:
            #Assigning variables for readability.
            sph = eye[0]
            cyl = eye[1]
            axis = eye[2]

            #Sph, cyl, axis values stay the same for this type of conversion.
            od_os_converted[count].append(sph)
            od_os_converted[count].append(cyl)
            od_os_converted[count].append(axis)

            count += 1
        return od_os_converted

    #If convert type is dr_svi (Distance/Reading to Single Vision Intermediate)...
    elif convert_type == "dr_svi":
        od_os_converted = [[], []]
        count = 0

        #Format into 2 lists (one for OD one for OS) from dictionary
        rx_list = format.entry_consolidate(entry_dict, "mf")
        for eye in rx_list:
            #Assigning variables for readability
            sph = eye[0]
            cyl = eye[1]
            axis = eye[2]
            add = eye[3]
            add_halved = add / 2
            dec_add_halved = float(abs(add_halved) - abs(int(add_halved)))
            #If half of add doesn't round to 2 decimal points (for add powers ending in .25 or .75), round up.
            if len(str(dec_add_halved)) == 5:
                add_halved += 0.125

            #Perform intermediate conversion (adding half of add power to SPH)
            od_os_converted[count].append(sph + add_halved)
            od_os_converted[count].append(cyl)
            od_os_converted[count].append(axis)

            count += 1

        return od_os_converted

    #If convert type is dr_svr (Distance/Reading to Single Vision Reading)...
    elif convert_type == "dr_svr":
        od_os_converted = [[], []]
        count = 0
        rx_list = format.entry_consolidate(entry_dict, "mf")
        for eye in rx_list:
            #Assigning variables for readability.
            sph = eye[0]
            cyl = eye[1]
            axis = eye[2]
            add = eye[3]

            #Perform reading conversion (adding add power to SPH value)
            od_os_converted[count].append(sph + add)
            od_os_converted[count].append(cyl)
            od_os_converted[count].append(axis)

            count += 1

=======
import format

def mf_to_sv(entry_dict, convert_type):
    """
    This function takes a dictionary of multifocal rx values, and converts them into a single vision prescription
    depending on convert_type.
    Returns converted rx in a list of 2 lists, index 0 being OD lens, index 1 being OS lens.
    """
    #If convert type is dr_svd (Distance/Reading to Single Vision Distance)...
    if convert_type == "dr_svd":
        od_os_converted = [[],[]]
        count = 0
        #Format into 2 lists (one for OD one for OS) from dictionary
        rx_list = format.entry_consolidate(entry_dict,"mf")
        for eye in rx_list:
            #Assigning variables for readability.
            sph = eye[0]
            cyl = eye[1]
            axis = eye[2]

            #Sph, cyl, axis values stay the same for this type of conversion.
            od_os_converted[count].append(sph)
            od_os_converted[count].append(cyl)
            od_os_converted[count].append(axis)

            count += 1
        return od_os_converted

    #If convert type is dr_svi (Distance/Reading to Single Vision Intermediate)...
    elif convert_type == "dr_svi":
        od_os_converted = [[], []]
        count = 0

        #Format into 2 lists (one for OD one for OS) from dictionary
        rx_list = format.entry_consolidate(entry_dict, "mf")
        for eye in rx_list:
            #Assigning variables for readability
            sph = eye[0]
            cyl = eye[1]
            axis = eye[2]
            add = eye[3]
            add_halved = add / 2
            dec_add_halved = float(abs(add_halved) - abs(int(add_halved)))
            #If half of add doesn't round to 2 decimal points (for add powers ending in .25 or .75), round up.
            if len(str(dec_add_halved)) == 5:
                add_halved += 0.125

            #Perform intermediate conversion (adding half of add power to SPH)
            od_os_converted[count].append(sph + add_halved)
            od_os_converted[count].append(cyl)
            od_os_converted[count].append(axis)

            count += 1

        return od_os_converted

    #If convert type is dr_svr (Distance/Reading to Single Vision Reading)...
    elif convert_type == "dr_svr":
        od_os_converted = [[], []]
        count = 0
        rx_list = format.entry_consolidate(entry_dict, "mf")
        for eye in rx_list:
            #Assigning variables for readability.
            sph = eye[0]
            cyl = eye[1]
            axis = eye[2]
            add = eye[3]

            #Perform reading conversion (adding add power to SPH value)
            od_os_converted[count].append(sph + add)
            od_os_converted[count].append(cyl)
            od_os_converted[count].append(axis)

            count += 1

>>>>>>> fc25f871622db43c363b5748a77f54a75ba39ae8
        return od_os_converted