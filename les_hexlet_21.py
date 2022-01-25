def encrypt(my_string):
    number = 0
    new_string =''
    my_len = len(my_string)
    if my_len % 2 == 0:
        while number < my_len:
          new_string = new_string + my_string[number + 1] + my_string[number]
          number += 2
        return new_string
    else:
        while number < my_len - 1:
          new_string = new_string + my_string[number + 1] + my_string[number]
          number += 2
        return new_string + my_string[-1]
