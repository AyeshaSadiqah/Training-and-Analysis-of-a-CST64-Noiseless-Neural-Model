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
Seed=39
random.seed(Seed)

trials=1
iter=0


while iter <N:

    # Total area is [0,1]x[0,1] (before resizing) 
    # Area of the triangle should vary between 5% and 25% of the total area
    # 5% is too small for 28x28 pictures, start from 10% up to 35%
    # Generate 3 random points in unit square
    points = [(random.uniform(0.0, 1.0), random.uniform(0.0, 1.0)) for _ in range(3)]

    ## Area is 1/2 |(Bx-Ax)(Cy-Ay)-(Cx-Ax)(By-Ay)|
    detMatrix=(points[1][0]-points[0][0])*(points[2][1]-points[0][1])
    detMatrix=detMatrix-(points[2][0]-points[0][0])*(points[1][1]-points[0][1])
    triangle_area = 0.5*abs(detMatrix)
    if triangle_area<0.10 or triangle_area>0.35:
       trials=trials+1
       continue

    # Scale the points to image size
    scaled_points = [(int(x * img_size), int(y * img_size)) for x, y in points]

    #print("%d Triangle area is %1.4f " % (iter, triangle_area));
    #print(scaled_points)

    # Create a white background image
    ##image = Image.new("RGB", (img_size, img_size), "black")
    # Instead of "black", use the numeric value 0 explicitly
    image = Image.new("L", (img_size, img_size), 0)
    # I also added "L" to Draw() to be sure that the background stays black
    draw = ImageDraw.Draw(image, "L")
    
    # Draw the triangle edges manually with specified line width
    for i in range(3):
        start_point = scaled_points[i]
        end_point = scaled_points[(i + 1) % 3]
        draw.line([start_point, end_point], fill="white", width=line_width)
    
    # Save as JPEG
    if iter<4000 : ## Training dataset
       filename="Train_noiseless_CST64/triangle/synthetic_triangle_train_%04d.jpg" % (iter)
    else: ## Test dataset
       filename="Test_noiseless_CST64/triangle/synthetic_triangle_test_%04d.jpg" % (iter)
    
    image.save(filename, "JPEG")
    print("\n%d Triangle area is %1.4f " % (iter, triangle_area));
    print("Image %d completed after %d trials.\n" % (iter, trials))
    trials=1
    iter=iter+1
    
print("Created %d synthetic images of a triangle." % (N))

