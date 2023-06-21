def get_initials(first_name, second_name, last_name):
    second_name_holder = ''

    if second_name:
        second_name_holder = second_name + ' '

    return f"{first_name.capitalize()} {second_name_holder.capitalize()}{last_name.capitalize()[0]}."
