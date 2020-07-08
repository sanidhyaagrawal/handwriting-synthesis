#from django.test import TestCase

# Create your tests here.


from PIL import Image,ImageOps  
import numpy as np
import random
import PIL
temp=0
fonts = 'NULL'
def Signle_Line_Writter(page,string,Line_Number,space = 25, x=200,y1=261,colour = "Blue",return_x = False,ispow = False,font = fonts):
    pow_counter = 0  
    #print(font)
    y=y1+int(70.8*Line_Number)
    capital_letter_size_factor = 0.5
    
        #img.save("rich.png")  
    def ncrandom(ll,ul): #non consecutive random
        global temp
        num=random.randint(ll,ul)
        #print(temp,num)
        if num != temp:
            temp = num
            return(num)
        else:
            return(ncrandom(ll,ul))
        

     

    #width, height = img.size 
    #area = (0, 0, width, height) 
    #img = img.crop(area) 
    #img = img.resize((width/2, height/2)) 
    #orgin = 200,261

    for char in string:
        assci=ord(char)
        if assci == 32: #Spacebar
            x=x+space+int(ncrandom(1,5)*1.5)
      
        else:
            sub=ncrandom(0,3) #0,1,2,3
            #print(str(assci)+str(sub))
            #if(assci>126):
              #  print('ASCII-', assci,'i.e-',chr(assci), 'Not Found in Libray, Skipping the Line')
            try:
                path = str(font)+'/'+str(assci)+str(sub)+'.png'
                aplha  = Image.open(path).convert("RGBA")  
            except:
                print('In line :-   "', string,'"')
                print('ASCII-', assci,'i.e-',"'",chr(assci),"'",path, 'Not Found in Libray, Skipping the Line')
                break
            width, height = aplha.size
            if assci == ord('f') or assci == ord('g') or assci == ord('j') or assci == ord('p') or assci == ord('q')or assci == ord('y') or assci == 95: #down
                height = int(height/2)
            if assci == ord(','):
                height = int(height/10 -7)
            if assci == ord(';'):
                height = int(height/2 +3)    
            if assci == ord('"') or assci == ord("'") or assci == ord('^') or assci == 96 : #up
                height = int(height+25)
            if assci == ord('*') or assci == ord('+') or assci == 44 or assci == ord(':') or assci == ord('<')or assci == ord('@')or assci == ord('=')or assci == ord('-'): #center
                height = int(height+10)
            if assci == ord('p'): #center
                height = int(height+6)
            if ispow == True:
                    if assci > 47 and assci <58:
                        pow_counter = pow_counter + 1
                    height = int(height+25)
                    
                    if pow_counter == 1:
                        if assci > 47 and assci <58:
                            aplha = aplha.resize((int(width*capital_letter_size_factor), int(height*capital_letter_size_factor)),Image.ANTIALIAS )   
                            width=int(width*capital_letter_size_factor)
                            height=int(height*capital_letter_size_factor)
                            height = int(height+25)
                            temp=y-height
                            print(temp)
                    else:
                        if assci > 47 and assci <58:  #Numberes 
                            aplha = aplha.resize((int(width*capital_letter_size_factor), int(height*capital_letter_size_factor)),Image.ANTIALIAS )   
                            width=int(width*capital_letter_size_factor)
                            height=int(height*capital_letter_size_factor)
                            #height = int(height+25)
                            print(height)
                            yplot=y-height
                            diff = temp - yplot
                            height = height - diff
                            print(height)
                            
                                                   # if assci > 64 and assci <91:  #capital letters
                                                   #    aplha = aplha.resize((int(width*capital_letter_size_factor), int(height*capital_letter_size_factor)),Image.ANTIALIAS )   
                                                   #    width=int(width*capital_letter_size_factor)
                                                   #    height=int(height*capital_letter_size_factor)
            
            yplot=y-height-ncrandom(-1,2)
            page.paste(aplha,(x, yplot),aplha)
          
            x=x+int(width)+random.randint(0,4)  #Spacing between letters 
    if return_x == True:
        return page,x-int(width)
    else:
        return page
