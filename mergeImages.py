#!/usr/bin/env python
# coding: utf-8

import numpy as np
from PIL import Image
from glob import glob
import numpy as np

def get_images(file_path, name):
	imgs = []

	for file in file_path:
		img_file_path = glob(file +"/*.jpg")[np.random.randint(500)]
		img = Image.open(img_file_path)
		imgs.append(img)
		
	merge_images(name + "1.jpg", imgs[:10])
	merge_images(name + "2.jpg", imgs[10:])
	
def merge_images(file_name, imgs):
	min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
	imgs_comb = np.hstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )

	imgs_comb = np.vstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )
	imgs_comb = Image.fromarray( imgs_comb)
	imgs_comb.save(file_name)
	
train_files = glob("C:/Users/mbura/Desktop/EE492/Dataset/train/*")
test_files =  glob("C:/Users/mbura/Desktop/EE492/Dataset/test/*")

get_images(train_files, "Train")
get_images(test_files, "Test")

