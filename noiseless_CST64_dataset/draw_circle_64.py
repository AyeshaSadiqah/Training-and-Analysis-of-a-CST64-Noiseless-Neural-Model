## ECEN 250 - Spring 2025
## Last modified: 18 April 2025
##

import math
import random
from PIL import Image, ImageDraw
import numpy as np

# Image size in pixels
img_size = 64
line_width = 3  # Set your desired line width here


N=4400 ## 4000 training images and 400 test images
Seed=37
random.seed(Seed)

iter=0

while iter <N:

    # Total area is [0,1]x[0,1] (before resizing) 
    # Area inside the circle varies between 5% and 25% of the total area
    # 5% is too small for 28x28 pictures, start from 10% up to 35%
    disc_area = random.uniform(0.10, 0.35)
    radius=math.sqrt(disc_area/math.pi)
    
    #print("\n%d Circle radius is %1.4f " % (iter, radius));
    #print("%d Disc area is %1.4f \n" % (iter, disc_area));

    # Generate a random center
    center = (random.uniform(0.0+radius,1.0-radius), random.uniform(0.0+radius,1.0-radius))

    # Scale to image size
    cx, cy = int(center[0] * img_size), int(center[1] * img_size)
    r = int(radius * img_size)

    # Create a white background image
    ##image = Image.new("RGB", (img_size, img_size), "black")
    # Instead of "black", use the numeric value 0 explicitly
    image = Image.new("L", (img_size, img_size), 0)
    # I also added "L" to Draw() to be sure that the background stays black
    draw = ImageDraw.Draw(image, "L")

    # Define the bounding box of the circle
    bbox = [(cx - r, cy - r), (cx + r, cy + r)]

    # Draw the circle outline
    draw.ellipse(bbox, outline="white", width=line_width)

    # Save as JPEG
    if iter<4000 : ## Training dataset
       filename="Train_noiseless_CST64/circle/synthetic_circle_train_%04d.jpg" % (iter)
    else: ## Test dataset
       filename="Test_noiseless_CST64/circle/synthetic_circle_test_%04d.jpg" % (iter)

    image.save(filename, "JPEG")
    print("\n%d Circle radius is %1.4f " % (iter, radius));
    print("%d Disc area is %1.4f \n" % (iter, disc_area));
    iter=iter+1
    
print("Created %d synthetic images of a circle." % (N))



