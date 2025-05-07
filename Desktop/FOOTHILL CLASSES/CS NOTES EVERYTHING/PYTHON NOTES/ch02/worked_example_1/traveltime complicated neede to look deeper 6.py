from math import sqrt

xDistance = float(input("x-distance to target: "))
yDistance = float(input("y-distance to target: "))
segment1Length = float(input("Length of first segment: "))
segment1Speed = float(input("Speed along first segment: "))
segment2Speed = float(input("Speed along second segment: "))

segment1Time = segment1Length / segment1Speed
segment2Length = sqrt((xDistance - segment1Length) ** 2 + yDistance ** 2)
segment2Time = segment2Length / segment2Speed
totalTime = segment1Time + segment2Time

print("Total travel time: ")
print(totalTime) 

