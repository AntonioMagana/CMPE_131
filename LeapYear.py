year = float(input("What year would you like to check"))

if year%4 == 0:
    print("Is leap year")
    if year%100 == 0 and year%400 == 0:
    print("Is leap year")
else:
    print("Is not leap year")
