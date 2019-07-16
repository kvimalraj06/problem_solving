year=int(input())
if((year%400==0)or((year%4==0) and (year%100==0))):
    print(year,"is leap year")
else:
    print('not a leap year')