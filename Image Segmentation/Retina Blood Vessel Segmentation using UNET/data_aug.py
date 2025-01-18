import os
import numpy as np
import cv2 as cv
from glob import glob
from tqdm import tqdm
import imageio
from albumentations import HorizontalFlip, VerticalFlip, Rotate
import re

# Createe a directory
def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def load_data(path):
    train_x = sorted(glob(os.path.join(path, "training", "images", "*.tif")))
    train_y = sorted(glob(os.path.join(path, "training", "1st_manual", "*.gif")))
    
    test_x = sorted(glob(os.path.join(path, "test", "images", "*.tif")))
    test_y = sorted(glob(os.path.join(path, "test", "1st_manual", "*.gif")))

    return (train_x, train_y), (test_x, test_y)
     
def argument_data(images, masks, save_path, argument=True):
    size = (512, 512)
    
    for idx, (x,y) in tqdm(enumerate(zip(images, masks)), total = len(images)):
        
        # Extracting the name
        name = re.split(r'[\\/]', x)[-1].split(".")[0]
        # print(name)
        
        # Reading Image and mask
        x = cv.imread(x, cv.IMREAD_COLOR)
        y = imageio.mimread(y)[0]
        # print(x.shape, y.shape)
        
        if argument == True:
            aug = HorizontalFlip(p=1.0)
            argumented = aug(image=x, mask=y)
            x1 = argumented["image"]
            y1 = argumented["mask"]
            
            aug = VerticalFlip(p=1.0)
            argumented = aug(image=x, mask=y)
            x2 = argumented["image"]
            y2 = argumented["mask"]
            
            aug = Rotate(limit=45, p=1.0)
            argumented = aug(image=x, mask=y)
            x3 = argumented["image"]
            y3 = argumented["mask"]
            
            X = [x, x1, x2, x3]
            Y = [y, y1, y2, y3]
        
        else:
            X = [x]
            Y = [y]
            
        index = 0
        for i, m in zip(X,Y):
            i = cv.resize(i, size)
            m = cv.resize(m, size)
            
            temp_image_name = f"{name}_{index}.png"
            temp_mask_name = f"{name}_{index}.png"

            image_path = os.path.join(save_path, "image", temp_image_name)
            mask_path = os.path.join(save_path, "mask", temp_mask_name)
            
            cv.imwrite(image_path, i)
            cv.imwrite(mask_path, m)
            
            index += 1
            

if __name__ == "__main__":
    np.random.seed(42)
    
    # Load the dataset
    data_path = "Dataset/"
    (train_x, train_y), (test_x, test_y) =  load_data(data_path)
    
    # Create directories to save the argumented data
    create_dir("new_data/train/image/")
    create_dir("new_data/train/mask/")
    create_dir("new_data/test/image/")
    create_dir("new_data/test/mask/")
    
    # Data Argumentation
    argument_data(train_x, train_y, "new_data/train/", argument=True)
    argument_data(test_x, test_y, "new_data/test/", argument=False)