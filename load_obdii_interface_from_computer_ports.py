import serial
import platform

def scanSerial():
    """Scan for available serial ports and return a list of serial port names."""
    available_ports = []
    
    # Scan for standard ttyS* ports (Linux)
    for i in range(256):
        try:
            s = serial.Serial(i)
            available_ports.append(s.portstr)
            s.close()  # Close the port to release the resource
        except serial.SerialException:
            pass  # If the port can't be opened, ignore and continue
    
    # Scan for USB ttyACM* ports (Linux)
    for i in range(256):
        try:
            s = serial.Serial("/dev/ttyACM" + str(i))
            available_ports.append(s.portstr)
            s.close()
        except serial.SerialException:
            pass
    
    # Scan for USB ttyUSB* ports (Linux)
    for i in range(256):
        try:
            s = serial.Serial("/dev/ttyUSB" + str(i))
            available_ports.append(s.portstr)
            s.close()
        except serial.SerialException:
            pass
    
    # Scan for ttyd* ports (Linux)
    for i in range(256):
        try:
            s = serial.Serial("/dev/ttyd" + str(i))
            available_ports.append(s.portstr)
            s.close()
        except serial.SerialException:
            pass
    
    # macOS specific scan for tty.usbmodemXXXX ports
    if platform.system() == "Darwin":  # Check if the system is macOS
        for i in range(65535):
            extension = hex(i).replace("0x", "", 1)
            try:
                s = serial.Serial("/dev/tty.usbmodem" + extension)
                available_ports.append(s.portstr)
                s.close()
            except serial.SerialException:
                pass
    
    return available_ports

available_ports = scanSerial()
if available_ports:
    print("Available serial ports:", available_ports)
else:
    print("No serial ports found.")
