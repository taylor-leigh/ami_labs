if __name__ == '__main__':

    # get the input string
    string = input("Insert a string: ")

    # if the string has more than 2 chars, return only the first and the last 2
    if len(string) > 2:
        result = string[:2] + string[-2:]
    else:
        result = ""

    print("'" + string + "' yields '" + result + "'")
