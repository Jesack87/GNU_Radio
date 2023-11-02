import time

outputFileName = "myTempReadings.txt"

# If this doesn't work, try changing it to thermal_zone0, thermal_zone1, thermal_zone3, etc
inputFileName = "/sys/class/thermal/thermal_zone2/temp"

f_out = open(outputFileName, "w")

for i in range(1, 12+1):    # Take a specified number of temperature readings
    f_temp = open(inputFileName, "r")
    contents = f_temp.read()
    f_temp.close()
    T = int(contents)/1000   # Convert T from millidegrees to deg. Celsius.
    print(T)
    f_out.write(str(T) + ", ")
    time.sleep(0.2)

f_out.close()
