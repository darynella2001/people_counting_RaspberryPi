import threading

from gps_module import GPSModuleWrapper
from magnetic_module import MagneticModuleWrapper
from camera_module import CameraModuleWrapper


def main():
    gps_module_wrapper = GPSModuleWrapper()
    magnetic_module_wrapper = MagneticModuleWrapper()
    camera_module_wrapper = CameraModuleWrapper()

    thread1 = threading.Thread(target=gps_module_wrapper.run)
    thread2 = threading.Thread(target=magnetic_module_wrapper.run, args=(camera_module_wrapper, ))
    thread3 = threading.Thread(target=camera_module_wrapper.run, )
    
    thread1.start()
    thread2.start()
    thread3.start()

if __name__ == "__main__":
    main()