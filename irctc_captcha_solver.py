#code to solve NLP captch of IRCTC website and send the solved captcha back --This code only sends the solved captcha back and not the username and password
#note : tesseract-ocr should be installed
#web driver should be installed(chrome has been used here)

import pytesseract
from PIL import Image  #Pillow package
import cv2
import urllib
from selenium import webdriver

#pytesseract environmental path should be set first
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'

#chrome driver path
chrome_path = r"C:\Users\Himanshu Poddar\Desktop\chromedriver.exe"

#supplying the chrome driver path to webdriver
wd = webdriver.Chrome(chrome_path)

#open the website
wd.get('https://www.irctc.co.in/eticketing/loginHome.jsf')

#downloading the captcha image of IRCTC website
img = wd.find_element_by_id('captchaImg')
src = img.get_attribute('src')
urllib.request.urlretrieve(src, "irctc_nlp_captcha.png") #saved with the name irctc_nlp_captcha.png

#cropping the image
img = cv2.imread("irctc_nlp_captcha.png")
crop_nlp_irctc_img = img[0:19, 160:255] #dimensions supplied- website -https://www.mobilefish.com/services/record_mouse_coordinates/record_mouse_coordinates.php

#saving the cropped image
#cv2.imwrite('crop_nlp_irctc_img.png',crop_nlp_irctc_img)

#converting to grayscale
gray_image = cv2.cvtColor(crop_nlp_irctc_img, cv2.COLOR_BGR2GRAY)

#saving the grayscaled image
cv2.imwrite('gray_image_irctc_nlp_captcha.png',gray_image)

#predicting the text
text_predict = pytesseract.image_to_string(Image.open(".\\gray_image_irctc_nlp_captcha.png"))
print(text_predict)

#send the predicted values
#nlpAnswer is the id for the text box
nlpAnswer = wd.find_element_by_id("nlpAnswer")
nlpAnswer.send_keys(text_predict)

wd.close()
