import accimage
import numpy
import cv2
from PIL import Image
import time
import numpy as np


img = cv2.imread("chicago.jpg", 0)
img512 = cv2.resize(img, (512,512))
img256 = cv2.resize(img, (256,256))
cv2.imwrite("chicago256.jpg", img256)
cv2.imwrite("chicago512.jpg", img512)

print('-- 512x512 --')

acc_s_time = time.time()
for i in range(1000): 
    acc_image = accimage.Image("chicago512.jpg")
acc_e_time = time.time()

cv_s_time = time.time()
for i in range(1000):
    cv_image = cv2.imread("chicago512.jpg")
cv_e_time = time.time()

pil_s_time = time.time()
for i in range(1000):
    pil_image = Image.open("chicago512.jpg")
    pil_image = pil_image.convert('L')
pil_e_time = time.time()

print('acc time: ', acc_e_time-acc_s_time)
print('cv time: ', cv_e_time-cv_s_time)
print('pil time: ', pil_e_time-pil_s_time)


print('-- 256x256 --')

acc_s_time = time.time()
for i in range(1000): 
    acc_image = accimage.Image("chicago256.jpg")
acc_e_time = time.time()

cv_s_time = time.time()
for i in range(1000):
    cv_image = cv2.imread("chicago256.jpg")
cv_e_time = time.time()

pil_s_time = time.time()
for i in range(1000):
    pil_image = Image.open("chicago256.jpg")
    pil_image = pil_image.convert('L')
pil_e_time = time.time()

print('acc time: ', acc_e_time-acc_s_time)
print('cv time: ', cv_e_time-cv_s_time)
print('pil time: ', pil_e_time-pil_s_time)


print('-- 256x256 -> 512x512 --')

acc_s_time = time.time()
for i in range(1000): 
    acc_image = accimage.Image("chicago256.jpg")
    buffer = numpy.empty([acc_image.channels, acc_image.height, acc_image.width], dtype=numpy.uint8)
    acc_image.copyto(buffer)
    acc_image = np.transpose(buffer, (1,2,0))
    acc_image = cv2.resize(acc_image.astype(np.float), (512, 512))
acc_e_time = time.time()

cv_s_time = time.time()
for i in range(1000):
    cv_image = cv2.imread("chicago256.jpg")
    cv_image = cv2.resize(cv_image, (512,512))
cv_e_time = time.time()

pil_s_time = time.time()
for i in range(1000):
    pil_image = Image.open("chicago256.jpg")
    pil_image = pil_image.convert('L')
    pil_image = cv2.resize(np.array(pil_image), (512,512))
pil_e_time = time.time()

print('acc time: ', acc_e_time-acc_s_time)
print('cv time: ', cv_e_time-cv_s_time)
print('pil time: ', pil_e_time-pil_s_time)
