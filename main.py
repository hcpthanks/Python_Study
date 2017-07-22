

def get_formatted_name(first, last):
    full_name = '{} {}'.format(first, last)
    return full_name.title()


print(get_formatted_name('tom', 'lee'))