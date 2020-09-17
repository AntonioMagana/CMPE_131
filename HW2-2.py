while True:
    val1 = float(input("Enter the first number:"))
    val2 = float(input("Enter the second number:"))
    op = input("Enter the operation (** for exponents):")

    if op == "+":
        print(val1 + val2)
    elif op == "-":
        print(val1 - val2)
    elif op == "*":
        print(val1 * val2)
    elif op == "/":
        print(val1 / val2)
    elif op == "**":
        print(val1 ** val2)
    else:
        break
    
    con = input("Do you wish to exit? (y or n)")

    if con != "n":
              break
