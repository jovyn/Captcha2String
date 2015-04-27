import urllib
from pytesser import *

i = 1;
for i in range (1,16):
	img = "images\img" + str(i) +".png"
	urllib.urlretrieve ("[somURL]",img)
	print str(i) + ". Reading the value ....."
	captchaobj = Image.open(img)
	print " " + image_to_string(captchaobj).rstrip()
	print ("----------------------------------")
	i = i+1
	
