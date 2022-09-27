# Resolução TAREFA 2

- **How to load and plot any image?**
```python
image = cv2.imread('img_gray.jpg')  # LOADING
plt.imshow(image)  # DISPLAYING
```
- **How to get image size?**
```python
w, h = image.shape[0], image.shape[1]

print(f'Width: {w}px')
print(f'Height: {h}px')
```
- **How many pixels does this image have?**
```
Width * Height = # of pixels
469 * 625 = 293.125 pixels
```
  
