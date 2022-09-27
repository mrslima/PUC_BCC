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
- **What is image resolution?**
  - Image resolution is typically described in PPI, which refers to how many pixels are displayed per inch of an image. Higher resolutions mean that there more pixels per inch (PPI), resulting in more pixel information and creating a high-quality, crisp image.  
- **What is DPI?**
  - PPI and DPI are two acronyms often used interchangeably although they do have different meanings. PPI (Pixels Per Inch) refers display resolution, or, how many individual pixels are displayed in one inch of a digital image. ***DPI (Dots Per Inch) refers to printer resolution, or, the number of dots of ink on a printed image.***
- **How does it related to your size?**
  - The file size is determined by the number of pixels so the aim is to find out how many pixels the image contains. Since the resolution is 300 dpi, it means that each inch is 300 pixels across. As the image is 8 inches wide that means there are 2,400 pixels in width (8 x 300). Likewise, as the image is 12 inches long, the image is 3,600 pixels in length (12 x 300). To get the total we multiply the breadth by the length and the answer is 8,640,000 pixels (2400 x 3600).
