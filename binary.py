"""This function converts a decimal number to a binary number"""
def int_to_bin(num: int) -> str:
    binary = ""
    i = 128
    remainder = num

    while i >= 1:
        binary += str(remainder // i)
        remainder = remainder%i
        i = i // 2

    return(int(binary))


"""This function converts a binary number to a decimal number"""
def bin_to_int(binary: str) -> int:
    number = 0
    divisible = 1
    binary = str(binary)
    length = len(binary)
    i = length - 1
    
    while i >= 0:
        number += (divisible * int(binary[i]))
        
        divisible *= 2
        i -= 1

    return(number)
