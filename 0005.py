import math
windSpeed=float(input("Enter wind speed in kilometers/hour: "))
airTemperature=float(input("Enter air temperature in degrees Celsius:   "))
windChillIndex=( 13.12 + 
0.6215*airTemperature - 
11.37*math.pow(windSpeed,0.16) + 
0.3965*airTemperature*math.pow(windSpeed,0.16))
windChillIndex=round(windChillIndex,0)
print("The wind chill index is ",windChillIndex)