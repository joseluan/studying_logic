


def valid(value):
    open_char = ['(', '[', '{']
    close_char = [')', ']', '}']

    chars_temp = []

    for c in value:
        if c in open_char:
            chars_temp.append(c)
            continue

        if c in close_char:
            if c == ')':
                if chars_temp:
                    if chars_temp[-1] == '(':
                        chars_temp.pop()
                    else:
                        return False
                else:
                    return False
            elif c == ']':
                if chars_temp:
                    if chars_temp[-1] == '[':
                        chars_temp.pop()
                    else:
                        return False
                else:
                    return False
            elif c == '}':
                if chars_temp:
                    if chars_temp[-1] == '{':
                        chars_temp.pop()
                    else:
                        return False
                else:
                    return False
            else:
                return False
    

    if chars_temp != []:
        return False

    return True
        