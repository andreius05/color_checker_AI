"""
BRO ALL YOU NEED
IS JUST GIVE
 I IMAGE WITH SOME COLOR
"""





import numpy as np

# THIS IS OUR DATA
X = np.array([
    [255, 0, 0],    # RED
    [0, 255, 0],    # GREEN
    [0, 0, 255],    # BLUE
    [255, 255, 255],# WHITE
    [0, 0, 0],      # BLACK
    [255, 255, 0],  # YELLOW
    [0, 255, 255],  # CIAN
    [255, 0, 255]   # MAGENTA
])

y = np.array([
    'red',
    'green',
    'blue',
    'white',
    'black',
    'yellow',
    'cyan',
    'magenta'
])

from sklearn.neighbors import KNeighborsClassifier
model_1 = KNeighborsClassifier(n_neighbors=1)
model_2 = KNeighborsClassifier(n_neighbors=2)

# MODEL TRAINING
model_1.fit(X, y)
model_2.fit(X, y)

import cv2 as cv

img = cv.imread('photos/red.jpg')
cv.imshow('SUCK',img)
cv.waitKey(0)
(b, g, r) = img[10, 10]
print(r,g,b)
color =np.array([[r,g,b]])



# PREDICTIONS

"""
AND YEAH I
WANT TO SAY THAT 2 
PREDICTIONS IS REALLY SHIT , SO FOCUS ON 1 PREDICTION

"""
predictions_1 = model_1.predict(color)
predictions_2 = model_2.predict(color)
print(f"Predict 1 :{predictions_1}")
print(f"Predict 2 :{predictions_2}")
#   |
#   |
#   |
#   |
# THIS IS A SHIT predict but i wanted show
# how work this model if its very loud...