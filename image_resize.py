import numpy as np
from PIL import Image
import os

def resize_image(image, newHeight, newWidth):
    image_array = np.array(image) # converts image to na array

    originalHeight, originalWidth = image_array.shape[:2] # gets the OG height and width

    newImage = np.zeros((newHeight, newWidth, 3), dtype=np.uint8) # creates a new image with the new dimensions

    h_scale = originalHeight / newHeight # scale at which to multiply the newHeight
    w_scale = originalWidth / newWidth # scale at which to multiply the newWidth

    # iterates through the new image and fills it with the corresponding pixel from the original image
    for i in range(newHeight):
        for j in range(newWidth):
            newImage[i, j] = image_array[int(i * h_scale), int(j * w_scale)]

    resizedImage = Image.fromarray(newImage)
    return resizedImage

if __name__ == '__main__':
    # User inputs
    image_path = input("Enter the image path: ")
    file_name_temp = image_path.split("/")[-1]
    file_name, file_format = file_name_temp.split(".")[0], file_name_temp.split(".")[-1]
    newHeight = int(input("Enter the new height: "))
    newWidth = int(input("Enter the new width: "))

    image = Image.open(image_path)
    resizedImage = resize_image(image, newHeight, newWidth)
    output_path = "Resized Images"
    os.makedirs(output_path, exist_ok=True) # makes directory in current folder
    resizedImage.save(f"{output_path}/{file_name}_resized.{file_format}")




