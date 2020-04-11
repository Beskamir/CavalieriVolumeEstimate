from PIL import Image
import math
import random
import os

# Parameters that can be modified as needed
scale = float(575)/float(2) # 575 pixels / 2 mm = pixels/mm 
area = 0.01 # area in mm (Recommended is 0.5 for around 200ish pixels between points)
color = (0,0,0) # pixel color that we're looking for
averageSampling = 50
print("Area:",area,"area in mm^2")
# Dependent parameters
sample = math.floor(scale*math.sqrt(area))
area = (sample*(1/scale))**2
print("Sample:",sample,"uniform spacing in pixels")
print("Area:",area,"area in mm^2")


def main(filename):
    counter=0
    myImage = Image.open(filename)
    for avg in range(averageSampling):
        offset = random.randint(0,sample)
        # Need these to get image height, width and pixels
        height, width = myImage.size
        pixels = myImage.load()
        # goes through the input image and regularly samples it
        for i in range(height):
            if((i+offset)%sample==0):
                for j in range(width):
                    if((j+offset)%sample==0):
                        # print(pixels[i,j])
                        if(pixels[i,j]==0 or pixels[i,j]==color):
                            counter+=1
    return int(counter / averageSampling)


if __name__ == "__main__":
    print("Following are the data we want")
    print("Name, Count, Volume (mm^3)")
    for folder in os.listdir("Data"):
        counter = 0
        for filename in os.listdir("Data/"+folder):
            counter += main("Data/"+folder+"/"+filename)

        # Output results to screen, Volume calculation = count * area (mm) * 0.05 (mm) * 10 (1/10 sections) 
        print(folder+", ", counter, ", ", counter * area * 0.05 * 10) 