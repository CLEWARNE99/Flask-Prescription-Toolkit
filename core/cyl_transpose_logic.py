import format

def cyl_convert(entry_dict, convert_type):
    """
    This function takes a dictionary of rx value, and converts the rx from plus to minus cyl or vice versa
    depending on convert_type.
    Returns converted rx in a list of 2 lists, index 0 being OD lens, index 1 being OS lens.
    """
    if convert_type == "to_plus":
        #Format into 2 lists (one for OD one for OS) from dictionary
        rx_list = format.entry_consolidate(entry_dict, "sv")
        count = 0
        od_os_converted = [[],[]]
        for eye in rx_list:
            #Assigning variables for readability
            sph = eye[0]
            cyl = eye[1]
            axis = eye[2]

            #If cyl is already plus or 0, simply copy values over.
            if cyl >= 0:
                od_os_converted[count].append(sph)
                od_os_converted[count].append(cyl)
                od_os_converted[count].append(axis)

            #Otherwise, perform cyl transposition.
            else:
                new_sph = sph - (cyl * -1)
                new_cyl = cyl * -1
                if axis > 90:
                    new_axis = axis - 90
                else:
                    new_axis = axis + 90
                od_os_converted[count].append(new_sph)
                od_os_converted[count].append(new_cyl)
                od_os_converted[count].append(new_axis)
            count += 1
        return od_os_converted

    elif convert_type == "to_minus":
        #Format into 2 lists (one for OD one for OS) from dictionary
        rx_list = format.entry_consolidate(entry_dict, "sv")
        count = 0
        od_os_converted = [[], []]
        for eye in rx_list:
            # Assigning variables for readability
            sph = eye[0]
            cyl = eye[1]
            axis = eye[2]

            #If cyl is already minus or 0, simply copy values over.
            if cyl <= 0:
                od_os_converted[count].append(sph)
                od_os_converted[count].append(cyl)
                od_os_converted[count].append(axis)

            #Otherwise, perform transposition.
            else:
                new_sph = sph + cyl
                new_cyl = cyl * -1
                if axis > 90:
                    new_axis = axis - 90
                else:
                    new_axis = axis + 90
                od_os_converted[count].append(new_sph)
                od_os_converted[count].append(new_cyl)
                od_os_converted[count].append(new_axis)
            count += 1
        return od_os_converted