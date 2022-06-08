import RPi.GPIO as GPIO
import time

NO_SIGNAL_MAX_COUNTER = 10
MAGNETIC_SENSOR_PIN = 21 # todo:read from config

class MagneticModuleWrapper():
    def __init__(self, camera_module):
        self.no_signal_counter = 0
        self.pin = MAGNETIC_SENSOR_PIN
        self.delay = 500
        self.no_signal_counter = 0
        self.prev_pin_state = 0
        self.state = False

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)


    def run(self):
        while True:
            pin_state = GPIO.input(self.pin)

            if pin_state == 0 and self.camera.is_disabled():
                self.camera.enable()
            elif self.no_signal_counter >= NO_SIGNAL_MAX_COUNTER:
                self.camera.disable()
            
            time.sleep(1)