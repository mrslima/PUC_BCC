import cv2
import numpy as np


image = cv2.imread('img__label_to_src/Patient_28_0150_image.png')
label_grayscale = cv2.imread('img__label_to_src/Patient_28_0150_label.png')
label_color = label_grayscale.copy()


# GRAYSCALE
for key_lvl1, value_lvl1 in enumerate(label_grayscale):
    for key_lvl2, value_lvl2 in enumerate(value_lvl1):
        for key_lvl3, value_lvl3 in enumerate(value_lvl2):
            label_grayscale[key_lvl1][key_lvl2][key_lvl3] *= 100

# COLORFUL
for key_lvl1, value_lvl1 in enumerate(label_color):
    for key_lvl2, value_lvl2 in enumerate(value_lvl1):
        if str(label_color[key_lvl1][key_lvl2]) == '[1 1 1]':
            label_color[key_lvl1][key_lvl2] = np.array([0, 0, 255])
        elif str(label_color[key_lvl1][key_lvl2]) == '[2 2 2]':
            label_color[key_lvl1][key_lvl2] = np.array([0, 255, 0])
        elif str(label_color[key_lvl1][key_lvl2]) == '[3 3 3]':
            label_color[key_lvl1][key_lvl2] = np.array([255, 255, 0])
        elif str(label_color[key_lvl1][key_lvl2]) == '[4 4 4]':
            label_color[key_lvl1][key_lvl2] = np.array([255, 255, 0])

# BLEND
resultado = cv2.addWeighted(image, 0.3, label_color, 1, 0.0)

# DISPLAYING
cv2.imshow('GRAYSCALE', label_grayscale)
cv2.imshow('RGB', cv2.cvtColor(label_color, cv2.COLOR_BGR2RGB))
cv2.imshow('RESULTADO RGB', cv2.cvtColor(resultado, cv2.COLOR_BGR2RGB))
cv2.waitKey()
cv2.destroyAllWindows()
