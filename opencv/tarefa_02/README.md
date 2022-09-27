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
- **How are colors formed?**
    - Human eye cannot objectively assess the colour, but there are devices that measure colour precisely. Instrumental methods allow to define the colour in numerical form based on a standardized calculation using colorimeters or spectrophotometers. The mathematical colour record was developed by the International Commission on Illumination (CIE) and is consistent with the visual assessment.
    - Colour can be described using three attributes: hue, brightness and saturation.
      - **Hue** is a colour feature that depends on the radiation of a specific wavelength, which is captured by the receptors in the eye. Then, we can see a specific colour, e.g. green, red or blue. Colours that have hue are called chromatic colours.
      - **Brightness**, or colour intensity, is the sensitivity to radiation intensity that causes the colour to develop. A measure of colour brightness is luminance, which in daylight has the highest value for the yellow-green colour with a wavelength of 555 nm, and at night for a wavelength of 510 nm corresponding to the blue-green colour.
      - **Saturation** means mixing a chromatic colour with white, grey or black. Pastel colours are called unsaturated ones because they contain a lot of white colour.
The colour attributes presented are also standardised by the CIE system, which makes it possible to fully describe a colour using the three variables.
