import os
import serial
import json

from modules import cbpi
from modules.core.hardware import SensorPassive
from modules.core.props import Property

ser = serial.Serial('/dev/ttymxc3', 115200)

@cbpi.sensor
class CurrentSensors(SensorPassive):
    def get_unit(self):
        return ""

    def init(self):
        pass

    def stop(self):
        pass

    # Passive Sensor:
    def read(self):
        ser.flushInput();
        rdata = ser.readline().strip('\t\n\r')
        jdata = json.loads(rdata)
        val = '240V: {0}A, 120V: {1}A'.format(jdata['CurrentSensors'][0]['240V'], jdata['CurrentSensors'][0]['120V'])
        self.data_received(val)

    ## Active Sensor:
    # def execute(self):
    #     print 'execute!'
    #     while self.is_running():
    #         print 'execute running!'
    #         ser.flushInput();
    #         rdata = ser.readline().strip('\t\n\r')
    #         jdata = json.loads(rdata)
    #         val = '240V: {0}A, 120V: {1}A'.format(jdata['CurrentSensors'][0]['240V'], jdata['CurrentSensors'][0]['120V'])
    #         print 'current sensor running!'
    #         print val
    #         self.data_received()
    #         self.sleep(1)

    # @classmethod
    # def init_global(cls):