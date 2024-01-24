### IMPORTS
import os
import io
import requests
from PIL import Image
from tqdm import tqdm

### INPUTS
basepath = "https://raw.githubusercontent.com/pippo-82/img_tests/main/"
basename  ="img_"
img_format = "jpg"
nrimgs = 10
output_filename = "mergedimgs.pdf"


### INIT VARS
# get the current path
thisfile_dir = os.path.dirname(__file__)
imgs = []

### CODE
# change current working directory
os.chdir(thisfile_dir)

# get all images from url and save them in memory with BytesIO (show progress bar)
for i in tqdm(range(1,nrimgs+1)):
    response = requests.get(basepath + basename + str(i) + "." + img_format)
    if response.status_code:
        imgs.append(Image.open(io.BytesIO(response.content)))

# save all images to a merged PDF and print result
try:
    print(f'Success: {imgs[0].save(output_filename, save_all=True, append_images=imgs[1:]) == None}')
    # check if PDF file contains all the pages, if not return a message
    if len(imgs) != nrimgs:
        print("PDF CREATED BUT NOT ALL THE IMAGES WERE DOWNLOADED CORRECTLY")    
except:
    print("Some error occurred while saving the images to PDF file.")