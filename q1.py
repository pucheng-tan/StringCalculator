def Add(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return sum([ int(integer) for integer in numbers.split(',')])

if __name__ == "__main__":

    print("Testing start.")

    if Add("1,2,5") != 8:
        print("Error: expected Add('1,2,5') to be 8, got: ", Add("1,2,5") )

    if Add("0,8,9") != 17:
        print("Error: expected Add('0,8,9') to be 17, got: ", Add("0,8,9") )

    print("Testing finished.")