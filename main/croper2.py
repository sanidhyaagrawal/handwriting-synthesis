import cv2
import numpy as np
import glob
for img in glob.glob("*.png"):
    

    np.set_printoptions(threshold=np.inf)
    cv2.namedWindow("Tracking")

    image = cv2.imread(img)
    im_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    (thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    mesh = np.where(im_bw == 0)
    cords = list(zip(*mesh))
    x, y = map(list, zip(*cords))
    cropped = image[min(x):max(x),min(y):max(y)]

    frame=cropped

    im_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    (thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    im_bw=np.where(im_bw==0, 5, im_bw)
    im_bw=np.where(im_bw==255, 0, im_bw)
    im_bw=np.where(im_bw== 5,255, im_bw)

    res = cv2.bitwise_and(frame, frame, mask=im_bw)
    src=res
    tmp = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    _,alpha = cv2.threshold(tmp,0,255,cv2.THRESH_BINARY)
    b, g, r = cv2.split(src)
    rgba = [b,g,r, alpha]
    dst = cv2.merge(rgba,4)

    cv2.imwrite("./Cropped/"+img, dst)


           
    cv2.imshow("frame", dst)
    cv2.imshow("mask", im_bw)
    #cv2.imshow("res", res)

    key = cv2.waitKey(1)

