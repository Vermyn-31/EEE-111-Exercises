
def is_valid_input(x):
    """Check if the input provided is valid"""
    # TODO: Uncomment the next two lines once you've filled it out
    # if <insert condition here>:
    #     return False
    if x != 1 and x != 2:
        return False
    else:
        return True


def hexToDecimal(hex):
    exponent = len(hex)-1
    # TODO: Add conditions here for your base case/s
    # if <insert condition here>:
    # Do something here
    hexDatabase={"0" : 0, "1": 1,"2": 2, "3": 3, "4" : 4, "5": 5, "6": 6, "7": 7, "8" : 8, "9": 9, "A" : 10,"B" : 11, "C" : 12, "D" : 13, "E" : 14, "F" : 15}
    if len(hex) ==1:
        return int(hexDatabase[hex])

    # TODO: Add conditions here for your recursive case/s
    # else:
    # Do something
    # return something

    else:
        return int(hexDatabase[hex[0]])*16**(exponent) + int(hexToDecimal(hex[1:]))


def decimalToHex(decimal):
    remainder = decimal % 16
    hexDatabase= { 0: "0", 1 : "1" , 2 : "2", 3: "3", 4 : "4", 5 : "5", 6 : "6", 7 : "7", 8 : "8" , 9 : "9", 10: "A" ,11 : "B" , 12 : "C", 13 : "D", 14 : "E" , 15 : "F"}
    # TODO: Add conditions here for your base case/s
    # if <insert condition here>:
    # Do something here
    if decimal < 16:
        return str(hexDatabase[remainder])

    # TODO: Add conditions here for your recursive case/s
    # else:
    # Do something
    # return something
    else:
        return decimalToHex(int((decimal - remainder)/16)) + str(hexDatabase[remainder])

if __name__ == "__main__":
    x = int(input(
        "Enter (1) to convert from decimal to hex, (2) to convert from hex to decimal: "))
    print(x)

    while not is_valid_input(x):
        print("Invalid input.")
        x = int(input(
            "Enter (1) to convert from decimal to hex, (2) to convert from hex to decimal: "))
        print(x)

    if x == 1:
        # TODO: Ask and print decimal input, convert using decimalToHex(), print decimal equivalent
        decimal = int(input())
        print(f"Enter a decimal value: {decimal}")
        print(f"The hexadecimal equivalent of {decimal} is {decimalToHex(decimal)}.")
    elif x == 2:
        # TODO: Ask and print hex input, convert using hexToDecimal(), print hex equivalent
        hex = input()
        print(f"Enter a hexadecimal value: {hex}")
        print(f"The decimal equivalent of {hex} is {hexToDecimal(hex)}.")