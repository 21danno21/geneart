from randimage import get_random_image
from PIL import Image
import numpy as np


a = int(input("How many images to generate? "))  #asks user how many images to generate
b = 1 #starting number for counter for image generator so image saves are numbered
for i in range (0, a):
  img_size = (240,240)  #determines size image
  img = get_random_image(img_size)    #gets first random image array
  img2 = get_random_image(img_size)   #gets second random image array
  img3 = Image.fromarray((img * 1000).astype(np.uint8))   #converts first random image array to proper image and resizes
  img4 = Image.fromarray((img2 * 1000).astype(np.uint8))  #converts second random image array to proper image and resizes
  
  

  
  Image.blend(img3, img4, alpha=.4).save("image" + str(b) + ".png")    #blends the two random images together and saves

  print("Generated " + str(b))  #lets user know which image was generated
  b += 1    #counter for image generator so image saves are numbered
 
