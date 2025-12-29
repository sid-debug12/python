year = input("Enter the year : ")
year = int(year)
period = (year % 4)

if period == 0:
    print(str(year) + "Is a leap year")

else:
    print(str(year) + "is not a leap year")
