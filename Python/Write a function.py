def is_leap(n):
    leap = False
    if ((n%4==0 and n%100!=0) or n%400==0):
        leap=True
    return leap

year = int(input())
print(is_leap(year))
