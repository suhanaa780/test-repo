n=int(input("Enter a year:"))
year=int(n)
if((year%400==0) or((year%4==0) and (year%100 !=0))):

    print("Given year is a leap year", year)
else:
    print("Given year is not a leap year",year)
