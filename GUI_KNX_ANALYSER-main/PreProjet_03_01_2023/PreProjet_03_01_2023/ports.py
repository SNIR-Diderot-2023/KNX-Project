# Description: List all serial ports

#Send a message to the serial port every 5 seconds
import serial
import time
ser = serial.Serial('COM3')
while True:
    time.sleep(5)
    ser.write(b'hello')
    print(ser.readline())
    

