letters = 'acdegilmnoprstuw'


def hash(string):
    """
    compute hash of string
    :param string:
    :return:
    """
    h = 7
    for i in string:
        h = h * 37 + letters.index(i)
    return h


def reverse_hash(string):
    count = 0
    while True:
        hash_string = letters[0] * (count + 1)
        new_hash = hash(hash_string)
        if len(str(new_hash)) > len(string):
            break
        count += 1
    result_list = []
    try:
        for i in range(count):
            old_char = None
            for char in letters:
                hash_string = ''.join(result_list) + char + letters[0] * (count - i - 1)
                new_hash = hash(hash_string)
                if new_hash == int(string):
                    return hash_string
                elif new_hash > int(string):
                    result_list.append(old_char or letters[0])
                    break
                else:
                    old_char = char
    except:
        print "error"
    print result_list

if __name__ == '__main__':
    string = raw_input("please enter string")
    print reverse_hash(string)

