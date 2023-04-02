"""import sys
import os 
from PIL import Image

# set the arguments to be read by script.py
image_folder = sys.argv[1]
outpuy_folder = sys.argv[2]


if not os.path.exists(outpuy_folder):
    os.makedirs(outpuy_folder) 

for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{outpuy_folder}{clean_name}.png', 'png')
    print('done')"""

#Opencv example
"""import  cv2 

img = cv2.imread("C:\\Users\\LENOVO\\Downloads\\prasad_Batman_cinematic_lighting_high_resolution_3D_render_d05ec2cb-13a7-4e95-874d-8509c9b8f438.png", cv2.IMREAD_UNCHANGED)

img.shape

cv2.imshow("image", img)

cv2.waitKey(5000)

cv2.destroyAllWindows()"""

#matplotlib example
"""
import cv2
import numpy as np 
import matplotlib.pyplot as plt
img = cv2.imread("C:\\Users\\LENOVO\\Downloads\\prasad_Batman_cinematic_lighting_high_resolution_3D_render_d05ec2cb-13a7-4e95-874d-8509c9b8f438.png")

plt.imshow(img)

plt.waitforbuttonpress()
plt.close('all')"""

#pdfs with python

"""import  PyPDF2
with open('C:\\Users\\LENOVO\\Documents\\PrasadAtdharCard.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    page = reader.getPage(0)
    page.rotateClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    with open ('tilt.pdf','wb')as new_file:
        writer.write(new_file)"""

#Exercise on combine pdfs 
"""import PyPDF2
import sys

input = sys.argv[1:]

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('super.pdf')

pdf_combiner(input)"""

#Exercise of watermark adder
"""from PyPDF2 import PdfFileReader
import PyPDF2

template = PyPDF2.PdfFileReader(open('super.pdf','rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf','rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)
    with open('Watermarked_output.pdf','wb')as file:
        output.write(file)"""

#Sending email using python 
"""import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path 

html = Template(Path('C:\\Users\\LENOVO\\.vscode\\PORTFOLIO\\python_course\\index.html').read_text())

email = EmailMessage()
email['from'] = 'Prasad Kate'
email['to'] = 'kateprasad179@gmail.com','katep9619@gmail.com'
email['Subject'] = 'You won 1 ruppees'

email.set_content(html.substitute({'name':'TinTin'}),'html')
with smtplib.SMTP(host='smtp.gmail.com',port=587)as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('kateprasad445@gmail.com','rqehuraxgkpbgajz')
    smtp.send_message(email)
    print('all good boss!')"""


#Password checker 
"""import requests 
import hashlib
import sys


def request_api_data(query_char):
   url = 'https://api.pwnedpasswords.com/range/' + query_char
   res = requests.get(url)
   if res.status_code != 200:
       raise RuntimeError(f'check API, the response is {res.status_code}')
   return res
   
def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
       if h == hash_to_check:
           return count
    return 0

def pwned_api_check(password):

    shal1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    #print(shal1password)
    first5_char, tail = shal1password[:5], shal1password[5:]
    #print(first5_char, tail)
    responce = request_api_data(first5_char)
    return get_password_leaks_count(responce, tail)

def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times.... You should probably change your password')
        else:
            print(f'{password} was not found carry on !')

main(sys.argv[1:])"""

#hash Function 
"md5 HAsh Genrator"
"Hello : asfjhsdafjhHIuhruwRY34Y378Y"
 
#Twitter Bot











    




