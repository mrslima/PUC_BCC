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
    - The colour attributes presented are also standardised by the CIE system, which makes it possible to fully describe a colour using the three variables.
- **What is an image channel?**
    - Color digital images are made of pixels, and pixels are made of combinations of primary colors represented by a series of code. A channel in this context is the grayscale image of the same size as a color image, made of just one of these primary colors. For instance, an image from a standard digital camera will have a red, green and blue channel. A grayscale image has just one channel. 
    - **E.g.:** An RGB image has three channels: red, green, and blue. RGB channels roughly follow the color receptors in the human eye, and are used in computer displays and image scanners. If the RGB image is 24-bit (the industry standard as of 2005), each channel has 8 bits, for red, green, and blue—in other words, the image is composed of three images (one for each channel), where each image can store discrete pixels with conventional brightness intensities between 0 and 255. If the RGB image is 48-bit (very high color-depth), each channel has 16-bit per pixel color, that is 16-bit red, green, and blue for each per pixel.
- **What are RGB, Grayscale, and Binary color systems?**
    - **RGB Images:**
        - Colour images are three band monochrome images in which, each band contains a different color and the actual information is stored in the digital image. The color images contain gray level information in each spectral band. The images are represented as red, green and blue (RGB images). And each color image has 24 bits/pixel means 8 bits for each of the three color band(RGB).
    - **Grayscale Images:**
        - Grayscale images are monochrome images, Means they have only one color. Grayscale images do not contain any information about color. Each pixel determines available different grey levels. A normal grayscale image contains 8 bits/pixel data, which has 256 different grey levels. In medical images and astronomy, 12 or 16 bits/pixel images are used.
    - **Binary Images:**
        - It is the simplest type of image. It takes only two values i.e, Black and White or 0 and 1. The binary image consists of a 1-bit image and it takes only 1 binary digit to represent a pixel. Binary images are mostly used for general shape or outline. For Example: Optical Character Recognition (OCR).
- **What is the difference between RGB and HSV color systems?**
    - **RGB Colorspace** is a three dimensional model, consist of three primary colors, and based on the combination of these colors you are able to generate any other possible color.
    - **HSV Colorspace** is composed three components, Hue, Saturation and Value. In simple terms, Hue represents the actual pure color perceived by our eyes, Saturation is the colorfulness of that pure color (i.e decreasing Saturation reduces the colorfulness from the color itself), Value is the intensity of the color, correlates with the its darkness.
