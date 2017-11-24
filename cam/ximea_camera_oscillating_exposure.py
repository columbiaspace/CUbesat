from ximea import xiapi
from decimal import Decimal
import PIL.Image
import cv2
import time

cam = xiapi.Camera()
cam.open_device()
cam.set_imgdataformat('XI_RGB24')
cam.set_exposure(250000)
img = xiapi.Image()
cam.start_acquisition()
step_count = 7 #how many steps to reach exposure limit
incr_exposure = True #whether to incr or decr
print(cam.get_exposure_minimum())
try:
    t0 = time.time()
    image_count = 0
    while True:
        time_format = Decimal(('% 6.1f' % float(time.time() - t0)))
        if time_format % 2 == 0 and time_format >= 2:
            data_save = img.get_image_data_numpy(invert_rgb_order=True)
            img_save = PIL.Image.fromarray(data_save, 'RGB')
            img_save.save('xi_image_' + str(image_count) + '.bmp')
            image_count += 1
            print("photo taken")
            cam.stop_acquisition()
            print(step_count)
            if incr_exposure:
                new_exposure = int(cam.get_exposure() * 1.25)
                step_count -= 1
            else:
                new_exposure = int(cam.get_exposure() // 1.25)
                step_count += 1
            if step_count == 0:
                incr_exposure = False
            elif step_count == 13:
                incr_exposure = True
            print(new_exposure)
            cam.set_exposure(new_exposure)
            cam.start_acquisition()

        cam.get_image(img)
        data = img.get_image_data_numpy()
        data_save = img.get_image_data_numpy(invert_rgb_order=True)
        cv2.imshow("XiaCam", data)
        cv2.waitKey(1)
except KeyboardInterrupt:
    cv2.destroyAllWindows()

cam.stop_acquisition()

cam.close_device()
     
