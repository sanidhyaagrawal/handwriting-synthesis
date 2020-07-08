import cv2
import numpy as np
import os.path
import os 


# Path 



images=['1.png']
for image in images:
   
    #print(image) # = 35_77777_f1.jpg
    #np.set_printoptions(threshold=np.inf)
    image = cv2.imread(image)
    cv2.imshow('Hello',image)
    dim = (1654, 2338)
    print(image.shape)
    image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    print(image.shape)
   
    counter = -1
  


#image= image[220:360]
    w=242   
    h=269
    imagec= image[h:h+65,w:w+50]
    for j in range(0,11):
        i=0
        w=242
        for i in range(0,12):
            counter = counter + 1
            if(counter%4==0):
                assci = assci +1
                name=chr(assci)
                k=0
            
            imagec= image[h:h+65,w:w+50] #[Hight,Width]
            w=w+106
            

            
            im_gray = cv2.cvtColor(imagec, cv2.COLOR_BGR2GRAY)
            
            
            (thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
            
            mesh = np.where(im_bw == 0)
            #print(len(mesh))
            try:
                cords = list(zip(*mesh))
                #print(cords)
                x, y = map(list, zip(*cords))
                cropped = imagec[min(x):max(x),min(y):max(y)]
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

                cv2.imwrite(dirname+"/"+str(assci)+str(k)+".png", dst)
                #print(name)   
                k = k+1
            except:
                pass    
        h=h+113

    w=242   
    h=270
    imagec= image[h:h+70,w:w+56]
        
cv2.imshow('Hello',imagec)
    #cv2.imwrite("cropped\test1.png", dst)

'''

#image= image[264:345,233:293] # 1st box
#image= image[264:345,233:293]
#image= image[264:345,233:293]
#image= image[270:345, w:w+60] #[Hight,Width]
'''
