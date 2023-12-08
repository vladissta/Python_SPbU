import string


def convert_to_upper(txt):
    convert_dict = str.maketrans(string.ascii_lowercase, string.ascii_uppercase)
    return txt.translate(convert_dict)


def convert_to_lower(txt):
    convert_dict = str.maketrans(string.ascii_uppercase, string.ascii_lowercase)
    return txt.translate(convert_dict)


def mirror_convert(txt):
    convert_dict = str.maketrans(string.ascii_uppercase + string.ascii_lowercase,
                                 string.ascii_lowercase + string.ascii_uppercase)
    return txt.translate(convert_dict)


if __name__ == '__main__':
    assert convert_to_upper('AbCdE') == 'ABCDE'
    print('1st test passed')
    assert convert_to_lower('AbCdE') == 'abcde'
    print('2nd test passed')
    assert mirror_convert('AbCdE') == 'aBcDe'
    print('3rd test passed\n')