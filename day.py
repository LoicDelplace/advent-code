def one(input):
    result = 0
    i = 0 # While loop var
    string = ""
    first = ""
    last = ""
    final = ""
    alldigits = []

    lines = input.splitlines()
    for line in lines:
        first = ""
        last = ""
        while i < len(line):
            if (first == "") & (str.isdigit(line[i])):
                first = line[i]
            if str.isdigit(line[i]):
                last = line[i]
            i = i + 1
        i = 0
        final = first + last
        first = ""
        last = ""
        alldigits.append(final)
    for number in alldigits:
        result = result + int(number)
    return print("Input calculation : " + str(result))