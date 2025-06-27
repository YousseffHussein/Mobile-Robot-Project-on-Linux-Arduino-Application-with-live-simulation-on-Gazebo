import serial
import time

SerialObj = serial.Serial('/dev/ttyACM1') 

 
SerialObj.baudrate = 9600  # set Baud rate to 9600
SerialObj.bytesize = 8     # Number of data bits = 8
SerialObj.parity   ='N'    # No parity
SerialObj.stopbits = 1     # Number of Stop bits = 1

time.sleep(3)   # Only needed for Arduino,For AVR/PIC/MSP430 & other Micros not needed
                # opening the serial port from Python will reset the Arduino.
                # Both Arduino and Python code are sharing Com11 here.
                # 3 second delay allows the Arduino to settle down.

x = 6
for x in range(6):
  BytesWritten = SerialObj.write(b'A') 
  time.sleep(1)                                            # Declare A as a Byte (b'A')

print('BytesWritten = ', BytesWritten)

SerialObj.close() 