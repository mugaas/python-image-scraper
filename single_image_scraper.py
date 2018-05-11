#-------------------------------------------------------------------------------
# Name:        Website Single Image Scraper
# Purpose:     Reaches out to an Image URL path, takes the image and stores it with a new name.
#              Options: User Input; Command Line Argument; Static Path
#
# Author:      rdahlin
#
# Created:     05/04/2018
# Copyright:   (c) rdahlin 2018
# Version:     Python 3.6.5
#-------------------------------------------------------------------------------

# imported libraries
import requests
import os
import time
import shutil
import sys

# time variable
timestr = time.strftime("%Y%m%d")

# User Input for URL
image_url = input("Please Enter URL: ")
print(image_url)
input("If URL looks correct, press ENTER to continue. If not, press CTRL+C")

# Command Line Argument for URL
#image_url = sys.argv[1]

# Static Image Path
#image_url = "https://www.WEBSITE.com/IMAGE.PNG"  
 
# URL of the image to be downloaded is defined as image_url
r = requests.get(image_url) # create HTTP response object
 
# send a HTTP request to the server and save
# the HTTP response in a response object called r
with open("GIVE_IMAGE_NAME.png",'wb') as f:
  
    # write the contents of the response (r.content)
    # to a new file in binary mode.
    f.write(r.content)

# rename the file to a new file name preceeded with a datetime
newname = 'NEW_IMAGE_NAME.png'
os.rename('GIVE_IMAGE_NAME.png', timestr+'_'+newname)


# move the Image to another directory
source_path = r"/LOCAL_PATH_OF_THIS_PYTHON_FILE/"
source_files = os.listdir(source_path)
dest_path = r"/LOCAL_OR_NETWORK_PATH_TO_MOVE_IMAGE_TO/"

for file in source_files:
        if file.endswith('.png'):
            shutil.move(os.path.join(source_path,file), os.path.join(dest_path,file))


