import cv2
import numpy as np
from matplotlib import pyplot as plt
img_bgr = cv2.imread('htc_logo.jpg')#,cv2.IMREAD_GRAYSCALE)

# 將 BGR 圖片轉為 RGB 圖片
img_rgb = img_bgr[:,:,::-1]

# 或是這樣亦可
# img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

#print(type(img))
#print(img.shape)
cv2.namedWindow('htc',cv2.WINDOW_NORMAL)
cv2.imshow('htc',img_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('output.jpg',img_bgr,[cv2.IMWRITE_JPEG_QUALITY, 10])

#plt.imshow(img_rgb)
#plt.show()