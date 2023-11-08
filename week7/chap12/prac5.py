import torchvision as tv
from PIL import Image
import matplotlib.pyplot as plt

gray_tran = tv.transforms.Grayscale()
img_raw = Image.open('thousand.png')
img_gray = gray_tran(img_raw)
img_gray.save('gray_thou.png')
resi = tv.transforms.Resize([120, 213])
img_shrink = resi(img_raw)
img_shrink.save('shrink_thou.png')
img_shrink_gray = gray_tran(img_shrink)
img_shrink_gray.save("gray_shrink_thou.png")

figure = plt.figure(figsize=(10, 10))
figure.add_subplot(2, 2, 1)
plt.title('raw')
plt.axis("off")
plt.imshow(img_raw)

figure.add_subplot(2, 2, 2)
plt.title('gray')
plt.axis("off")
plt.imshow(img_gray, cmap='gray')

figure.add_subplot(2, 2, 3)
plt.title('shrink')
plt.axis("off")
plt.imshow(img_shrink)

figure.add_subplot(2, 2, 4)
plt.title('gray and shrink')
plt.axis("off")
plt.imshow(img_shrink_gray, cmap='gray')

plt.show()
