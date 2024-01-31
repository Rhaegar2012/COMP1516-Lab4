# Author: Jose Tellez


def generate_password(first_name, last_name, bcit_id):
    """
    Returns the default login password
    :param first_name: user first name , as string
    :param last_name: user last name as string
    :param bcit_id: BCIT ID, alphanumeric
    :return:
    """
    formatted_first_name = str(first_name).lower().capitalize()
    formatted_last_name = str(last_name).lower().capitalize()
    first_name_initial_characters = extract_first_three_characters_from_string(formatted_first_name)
    last_name_initial_characters = extract_first_three_characters_from_string(formatted_last_name)
    bcit_id_last_characters = extract_last_three_characters_from_string(bcit_id)
    default_password = first_name_initial_characters + last_name_initial_characters + bcit_id_last_characters
    return default_password


def change_password():
    """

    :return:
    """
    password_meets_specifications = False

    while password_meets_specifications == False:
        new_password = input("Enter new password: ")
        password_length = len(new_password)

        if password_length > 7:
            password_length_complies = True
        else:
            password_length_complies = False

        has_uppercase = any(char.isupper() for char in new_password)
        has_lowercase = any(char.islower() for char in new_password)
        has_digit = any(char.isdigit() for char in new_password)

        if password_length_complies == True and has_uppercase == True and has_lowercase == True and has_digit == True:
            password_meets_specifications = True

        else:
            print("New password does not meet specifications\n"
                  "Password should be at least 7 characters long \n"
                  "Password should contain at least one uppercase character \n"
                  "Password should contain at least one lowercase character \n"
                  "Password should contain at least one digit ")

    return new_password


def extract_first_three_characters_from_string(string):
    """
    Extracts the first three letters of a string , if the string length is less than 3 characters , returns
    the full string
    :param string:
    :return: tree letters of complete string
    """
    string_length = len(string)
    return_string = None
    if string_length < 3:
        return_string = string
    else:
        return_string = string[:3]
    return return_string


def extract_last_three_characters_from_string(string):
    """
    Extracts the last three characters of a string , if the string length is less than 3 characters , returns the full
    string
    :param string:
    :return:
    """
    string_length = len(string)
    return_string = None
    if string_length < 3:
        return_string = string
    else:
        return_string = string[-3:]
    return return_string
