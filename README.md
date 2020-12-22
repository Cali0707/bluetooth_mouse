# bluetooth_mouse
Python and arduino code to interface a bluetooth IMU with a computer to control the mouse

# Hardware
This project was assembled from an Arduino MKR 1010 Wifi and an Adafruit BNO055 sensor. 
These were wired together following the [instructions](https://learn.adafruit.com/adafruit-bno055-absolute-orientation-sensor/assembly) 
on the Adafruit website.

# Arduino Code
Code from the Adafruit BNO055 library was used to read acceleration off of the sensor, and an 
[example](https://create.arduino.cc/editor/dpajak/e7af8e95-0aff-4ce1-b2f7-4e7b446c2577/preview)
was modified to stream the data over BLE.

# Python Code
The [Bleak Library](https://pypi.org/project/bleak/) was used to connect the computer to the Arduino board,
and read in the sensor data. A running average was used to filter out xyz components of gravitational acceleration,
and a low-pass butterworth filter was used from the [SciPy library](https://pypi.org/project/scipy/) to filter noise.
The data was then integrated into a displacement, which was used with the [PyAutoGUI library](https://pypi.org/project/PyAutoGUI/)
to move the mouse.

# Next Steps
Buttons for right/left click should be added. Additionally, Quaternions should be read off of the BNO055 to provide a more accurate
displacement. 


