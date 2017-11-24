from ximea import xiapi
from decimal import Decimal
import PIL.Image
import cv2
import time

cam = xiapi.Camera()
cam.open_device()

cam.set_imgdataformat('XI_RGB32')
print(cam.get_shutter_type())
cam.enable_aeag() #enable automatic exposure
cam.enable_bpc() #enable correction of sensor defects
#cam.enable_auto_wb() #enable auto white-balance
print(cam.get_width_maximum()) #1280
print(cam.get_height_maximum()) #1024
print("Cooling Supported: " + str(cam.is_iscooled()))
print("Device Name: " + str(cam.get_device_name()))
print("Device Type: " + str(cam.get_device_type()))
print("Sensor Model: " + str(cam.get_sensor_model_id()))
print("Device Model ID: " + str(cam.get_device_sn()))
print("Alpha Channel of RGB32 Output Image Format: " + str(cam.get_imgdataformatrgb32alpha()))
print("Image Payload Size: " + str(cam.get_imgpayloadsize()))
#print("Maximum Image Payload Size: " + str(cam.get_imgpayloadsize_maximum()))
#print("Minimum Image Payload Size: " + str(cam.get_imgpayloadsize.minimum()))
print("Sensor Clock Frequency: " + str(cam.get_sensor_clock_freq_hz()))
print("Sensor Clock Frequency Maximum: " + str(cam.get_sensor_clock_freq_hz_maximum()))
print("Sensor Clock Frequency Minimum: " + str(cam.get_sensor_clock_freq_hz_minimum()))
print("Framerate: " + str(cam.get_framerate()))
print("Maximum Framerate: " + str(cam.get_framerate_maximum()))
print("Minimum Framerate: " + str(cam.get_framerate_minimum()))


img = xiapi.Image()

cam.start_acquisition()

print("Exposure: " + str(cam.get_exposure()))
print("Max Exposure: " + str(cam.get_exposure_maximum()))
print("Min Exposure: " + str(cam.get_exposure_minimum()))
print("Chip Temp: " + str(cam.get_chip_temp()))
print("Temp: " + str(cam.get_temp_maximum()))

try:
    while True:
        cam.get_image(img)
        #print(cam.get_exposure())
        data = img.get_image_data_numpy()
        cv2.imshow("XiaCam", data)
        #print(cam.get_trigger_source())
        cv2.waitKey(1)
except KeyboardInterrupt:
    cv2.destroyAllWindows()

cam.stop_acquisition()

cam.close_device()
