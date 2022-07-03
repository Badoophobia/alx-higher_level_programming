#!/usr/bin/python3
def no_c(my_string):
    string_list = list(my_string)
    for i in range(len(string_list)):
        if string_list[i] == 'c' or string_list[i] == 'C':
            string_list[i] = ""
    my_string = "".join(string_list)
    return my_string
