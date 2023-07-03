# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

AB = int(input())
BC = int(input())
MAC = math.degrees(math.atan(AB/BC))
print(round(MAC),chr(176),sep = '')
