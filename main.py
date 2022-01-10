# import Libraries
from PIL import Image
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


# Read image
img = Image.open('lex.jpg')  # show image
plt.imshow(img)
plt.show()

small_img = img.resize((32, 32), Image.BILINEAR)

# resize
o_size = (960, 640)  # output size
res = small_img.resize(o_size, Image.NEAREST)  # save image
res.save('lex_32x32.png')  # display image
plt.imshow(res)
plt.show()
