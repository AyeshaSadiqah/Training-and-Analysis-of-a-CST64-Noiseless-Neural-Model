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
Seed=38
random.seed(Seed)

trials=1
iter=0

while iter <N:

    # Total area is [0,1]x[0,1] (before resizing) 
    # Area of the square varies between 5% and 25% of the total area
    # 5% is too small for 28x28 pictures, start from 10% up to 35%
    square_area = random.uniform(0.10, 0.35)
    side_length=math.sqrt(square_area)
    
    # Rotation angle from 0 to Pi/2 (90 degrees is a symmetry angle for the square)
    # Assuming the rotation center is the center of the square
    angle=0.5*math.pi*random.uniform(0.0, 1.0)
    
    #print("\n%d Side length is %1.4f " % (iter, side_length));
    #print("%d Square area is %1.4f " % (iter, square_area));
    #print("%d Rotation angle is %1.2f degrees \n" % (iter, angle*180.0/math.pi));

    x=[0.0]*4;  y=[0.0]*4;
    # Compute the top-left corner
    x[0] = random.uniform(0, 1 - side_length)
    y[0] = random.uniform(0, 1 - side_length)

    # Compute the bottom-left corner
    x[1] = x[0]
    y[1] = y[0] + side_length

    # Compute the bottom-right corner
    x[2] = x[0] + side_length
    y[2] = y[0] + side_length

    # Compute the top-right corner
    x[3] = x[0] + side_length
    y[3] = y[0]

    # The center of the square
    xc=(x[0]+x[2])/2
    yc=(y[0]+y[2])/2

    #print("x and y (before rotation):")
    #print(x)
    #print(y)

    #print("The square center:")
    #print(xc, yc)

    xr=[0.0]*4;  yr=[0.0]*4;
    # Rotate by an angle theta
    Accepted=True
    for j in range(4):
        xr[j]=xc+math.cos(angle)*(x[j]-xc)-math.sin(angle)*(y[j]-yc)
        if xr[j]<0 or xr[j]>1:
           Accepted=False
        yr[j]=yc+math.sin(angle)*(x[j]-xc)+math.cos(angle)*(y[j]-yc)
        if yr[j]<0 or yr[j]>1:
           Accepted=False
    #print("xr and yr (after rotation):")
    #print(xr)
    #print(yr)
    
    if Accepted==False:
       print("After %d trials at iteration %d " % (trials, iter))
       print("One or more vertices outside the picture!")
       print("Picking up another random square!")
       trials=trials+1
       continue
       
    #print("Iteration=%d. Accepted" %(iter))
    
    # Making a list for the 4 vertices of the rotated square
    points=[(xr[j], yr[j]) for j in range(4)]

    #print(points)
    
    # Scale the vertices/points to image size
    scaled_points = [(int(x * img_size), int(y * img_size)) for x, y in points]

    #print(scaled_points)

    # Create a white background image
    ##image = Image.new("RGB", (img_size, img_size), "black")
    # Instead of "black", use the numeric value 0 explicitly
    image = Image.new("L", (img_size, img_size), 0)   ## L for a grayscale image
    # I also added "L" to Draw() to be sure that the background stays black
    draw = ImageDraw.Draw(image, "L")
    
    # Draw the edges of the rotated square manually
    for j in range(4):
        start_point = scaled_points[j]
        end_point = scaled_points[(j + 1) % 4]
        draw.line([start_point, end_point], fill="white", width=line_width)
    
     # Save as JPEG
    if iter<4000 : ## Training dataset
       filename="Train_noiseless_CST64/square/synthetic_square_train_%04d.jpg" % (iter)
    else: ## Test dataset
       filename="Test_noiseless_CST64/square/synthetic_square_test_%04d.jpg" % (iter)

    image.save(filename, "JPEG")
    print("\n%d Side length is %1.4f " % (iter, side_length));
    print("%d Square area is %1.4f " % (iter, square_area));
    print("%d Rotation angle is %1.2f degrees \n" % (iter, angle*180.0/math.pi));
    print("Image %d completed after %d trials.\n" % (iter, trials))
    trials=1
    iter=iter+1
    
print("Created %d synthetic images of a square." % (N))
