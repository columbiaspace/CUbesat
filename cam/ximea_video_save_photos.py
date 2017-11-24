"""
video + takes a photo every ten seconds and saves it to computer
"""

from ximea import xiapi
from decimal import Decimal
import PIL.Image
import cv2
import time

cam = xiapi.Camera()
cam.open_device()

cam.set_imgdataformat('XI_RGB24') 
#cam.set_exposure(500000)
cam.enable_aeag()
cam.enable_bpc()

img = xiapi.Image()

cam.start_acquisition()

try:
    t0 = time.time()
    image_count = 3000
    while True:
        cam.get_image(img)
        data = img.get_image_data_numpy()
        data1 = img.get_image_data_numpy(invert_rgb_order=True)
        time_format = Decimal(('% 6.0f' % float(time.time() - t0)))
        if time_format % 2 == 0: #the code inside the if statement saves the photo
            img1 = PIL.Image.fromarray(data1, 'RGB')
            img1.save('xi_image_' + str(image_count) + '.bmp')
            print("Photo taken")
            image_count += 1
        cv2.imshow("XiCam", data)
        cv2.waitKey(1)
except KeyboardInterrupt:
    cv2.destroyAllWindows()

cam.stop_acquisition()

cam.close_device()
