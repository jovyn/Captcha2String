import urllib
from pytesser import *

i = 1;
for i in range (1,16):
	img = "images\img" + str(i) +".png"
	urllib.urlretrieve ("http://10.24.149.27:6003/contestphase2/CallCaptacha.do",img)
	print str(i) + ". Reading the value ....."
	captchaobj = Image.open(img)
	print " " + image_to_string(captchaobj).rstrip()
	print ("----------------------------------")
	i = i+1
	
