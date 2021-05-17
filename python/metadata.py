import PIL.Image

image = PIL.Image.open('python/cielyesa.JPG')
exif_data = image._getexif()
for i,j in exif_data.items():
    print(i,j)