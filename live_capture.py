import obd
import obd_io
import serial
import platform
import obd_sensors
from datetime import datetime
import time

from obd_utils import ScanSerial

class OBD_Capture():
    def __init__(self):
        self.port = None
        localtime = time.localtime(time.time())

        def connect(self):
            portnames = ScanSerial
            for port in portnames:
                self.port = obd_io.OBDPort(port, None, 2, 2)