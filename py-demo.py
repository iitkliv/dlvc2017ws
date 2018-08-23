from PIL import Image
import os
import numpy as np

#Loading an image
img = Image.open('data/iitkgp.jpg')
print('Image size: '+str(img.size)) # image dimensions

# Numpy

import numpy as np
# Converting to numpy array and properties
print('Converting to numpy array.. ')
img_arr = np.array(img)
print('Array shape and typr: ')
print(img_arr.shape, img_arr.dtype)
print('Converting to grayscale..')
img_grayarr = np.array(img.convert('L'),'f') # 'f' => floating point
print('Array shape and typr: ')
print(img_grayarr.shape, img_grayarr.dtype)

# Acessing an element in an array
px1 = img_arr[100,100,2]
print('px1: '+ str(px1))

# Accessing multiple elements by slicing
px2 = img_grayarr[100,:] # all the elemts in a row
print('px2: '+ str(px2))

px3 = img_grayarr[100,30:40] # range of elements in a row
print('px3: '+ str(px3))

px4 = img_grayarr[:,-1] # last column
print('px4: '+ str(px4))


