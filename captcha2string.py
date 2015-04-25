######### Read CAPTCHA v.0.1 ######
######### Author : Jovin Lobo ##############
######### Email : j0k3r@null.co.in / jovyn4590@gmail.com #####
######### Twitter : @7h3_j0k3r ############

import time, datetime, sys
import argparse
import urllib
from pytesser import *

#Printing ReadCaptcha Usage /Help >>
# usage$: python ReadCaptcha.py -url (URL)
# Example: python ReadCaptcha.py -url www.example.com/Captcha_image

argp = argparse.ArgumentParser(prog='python ReadCaptcha.py',usage='%(prog)s -url [Captcha_url] -s [nos. of samples]',description='Eg: python ReadCaptcha.py -url http://www.example.com/Captcha_Image/ -s 20. **ReadCaptcha.py** is a python script that uses Pytesser to convert sample Captchas to text.',epilog="That's All Folks")
argp.add_argument('-url', help='enter the captcha url ', nargs='+')
argp.add_argument('-s', help='enter the no. of samples ', nargs='+')
if len(sys.argv)!=3:
    argp.print_help()
    sys.exit(1)
args = argp.parse_args()
timestamp = time.time()
image_dir = "Captcha_Images_" + str(timestamp)
os.mkdir(image_dir)
num = 0
for num in range(0,sys.argv[4]): 
    img_name = str("image_" + timestamp + ".png")
    urllib.urlretrieve (sys.argv[2], img_name)
    image = Image.open(img_name)
    print (num + "> Value of captcha ........")
    print image_file_to_string(img_name)
    print ("--------------------------------")
    

    
