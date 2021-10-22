from time import sleep
from accelgyro import getGyro
from tempHumidity import getTemp
from pressure import getPressure
import csv
from datetime import datetime

if __name__ == '__main__':
    while(True):
        gyroVals = getGyro()
        tempVals = getTemp()
        pressureVals = getPressure()
        # print(gyroVals)
        results = []
        # add time
        results.append(str(datetime.utcnow()))
        # add magvals
        for i in range(0, len(gyroVals[0])):
            results.append(str(gyroVals[0][i]))
        # add accvals
        for i in range(0, len(gyroVals[1])):
            results.append(str(gyroVals[1][i]))
        # add gyrovals
        for i in range(0, len(gyroVals[2])):
            results.append(str(gyroVals[2][i]))
        # add temp
        results.append(str(getTemp()))
        # add pressure
        results.append(str(getPressure()))
        # add yaw, pitch, raw
        for i in range(0, len(gyroVals[3])):
            results.append(str(gyroVals[3][i]))
        # print(results)
        file_object = open('data.csv', 'a')
        file_object.write(",".join(results)+"\n")
        file_object.close()
        print(results)
        sleep(1)
