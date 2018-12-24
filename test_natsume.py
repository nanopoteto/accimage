import accimage
import numpy
import cv2
from PIL import Image
import time

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
