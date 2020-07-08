
import timeit
starttime = timeit.default_timer()
print('Processing, Can take upto 10 Seconds')
import textwrap 
from . import PageCreator as PC
import textwrap 
from PIL import Image
import numpy as np
import random
import PIL
import os
temp=0 
def write(text,line1,line2,line3,fontid,Username,width=55): 
    pagedir= os.path.dirname(os.path.realpath(__file__))+'/'+'poor3.jpg'
    outputdir= os.path.dirname(os.path.realpath(__file__))[:-4]+'media/'+'font_preview/'
    fontdir=os.path.dirname(os.path.realpath(__file__))[:-4]+'media/fonts/'+str(fontid)
    fontid = str(fontid)  
    print(fontid)
    print(fontid)
    page=Image.open(pagedir).convert("RGBA")
    page = page.rotate(-0.25, PIL.Image.NEAREST, expand = 1) 
    pglist=[]     
    linenumber = 0
    file = open(os.path.dirname(os.path.realpath(__file__))+'/'+text,encoding='utf-8-sig') 
    data=file.readlines()

    para = []
    pageno = 0
    diff = False
    diffpoints = []
    sec1 = []
    sec2 = []
    points = []
    point = []
    index = 0
    '''
    name = 'Hritika Agrawal'
    roll = '2BAI-19-013'
    section = 'Section A'
    width=48
    fonts = 'Krishna'
    '''
    name = line1
    roll = line2
    section = line3
    fonts = fontdir

    #width=width

    wrapper = textwrap.TextWrapper(width)
    temp=0
    def ncrandom(ll,ul): #non consecutive random
        global temp
        num=random.randint(ll,ul)
        #print(temp,num)
        if num != temp:
            temp = num
            return(num)
        else:
            return(ncrandom(ll,ul))
        


    for lines in data: 
        word_list = wrapper.wrap(text=lines) 
        if "<diff>" in word_list:
            diff=True
            diffindex = index
        elif "</diff>" in word_list:
            diff=False
        elif diff == False:
            para.append(word_list)
        index = index+1


    wrapper = textwrap.TextWrapper(width=26) 
    for lines in data: 
        word_list = wrapper.wrap(text=lines) 
        if "<diff>" in word_list:
            diff=True
        elif "</diff>" in word_list:
            diff=False
        elif diff == True:
             diffpoints.append(word_list)



    num = []

    for i in range(0,len(diffpoints)):
        if i%2 == 0:
            points.append(diffpoints[i])
    for i in range(0,len(points)): 
        if i%2 == 0:
            sec1.append(points[i])
        else:
            sec2.append(points[i])

    for i in range(0,len(sec1)):
        sec1[i][0] = str(i+1) +'.   '+ sec1[i][0]
        


    if len(sec1) != len(sec2):
        print("Both section do not have same number of points, Result might be unstable")
    para1 = []
    emp = '                  ' #24 spaces
    a1 = []
    b1 = []
    enter = []
    for i in range(0,len(sec1)):#This given number of points
        if len(sec1[i]) > len(sec2[i]):
            diff = len(sec1[i]) - len(sec2[i])
            for p in range(0,diff):
                sec2[i].append(emp)
                
            for j in range(0,len(sec1[i])):
                while len(sec1[i][j]) <25:
                    sec1[i][j]=sec1[i][j]+' '
                print(len(sec1[i][j]),len(sec2[i][j]))    
                para.append([sec1[i][j]+"    "+sec2[i][j]])

        else:
            diff = len(sec2[i]) - len(sec1[i])
            for p in range(0,diff):
                sec1[i].append(emp)
            for j in range(0,len(sec2[i])):
                print(len(sec1[i][j]))
                para.append([sec1[i][j]+"    "+sec2[i][j]])
        para.append(enter)        
              
    if pageno == 0:
                    page=PC.Signle_Line_Writter(page,str(name),linenumber,space = 25, x=1050+(random.randint(2,5)*9),y1=60,font = fonts)
                    page=PC.Signle_Line_Writter(page,str(section),linenumber,space = 25, x=1000+(random.randint(2,5)*9),y1=118,font = fonts)
                    page=PC.Signle_Line_Writter(page,str(roll),linenumber,space = 25, x=1020+(random.randint(2,5)*9),y1=175,font = fonts)

    for paras in para:
        if len(paras) == 0: 
            linenumber = linenumber +1
        
    
   
        for element in paras:
                if linenumber < 28:
                   

                    element=element.replace("‘","'")
                    element=element.replace("’","'")
                    element=element.replace('“','"')
                    element=element.replace('”','"')
                    element=element.replace('ü','')
                    element=element.replace('ο','')
                    element=element.replace('κ','')
                    element=element.replace('μ','')            
                    element=element.replace('–','-')
                
                    if element.find('Q.')== 0 or element.find('Ans.') == 0:
                        page=PC.Signle_Line_Writter(page,str(element),linenumber,space = 25, x=70+(random.randint(0,3)*7),colour = 'Black',font = fonts)
                        #linenumber=linenumber+1
                    elif element.find('<name>')==0:
                         page=PC.Signle_Line_Writter(page,str(element[6:]),linenumber,space = 25, x=1050+(random.randint(1,5)*10),y1=180-(random.randint(1,5)*3),font = fonts)
            
                    
                    elif element[0].isdigit() == True and element[0:3].isdigit() == False:
                       # print(element)
                        firstspace = element.find(' ')
                        if element[firstspace+1] == " ":
                            if element[firstspace+2] == " ":
                                  if element[firstspace+3] == ' ':
                                      while element[firstspace+3] == ' ':
                                          element=element[:firstspace+3]+element[firstspace+4:]
                                          #print(element)
                            else:
                                  element=element[:firstspace]+' '+element[firstspace:]
                        else:
                            element=element[:firstspace]+' '+' '+element[firstspace:]
                        
                        if element[3].isdigit():    
                            page=PC.Signle_Line_Writter(page,str(element),linenumber,space = 25, x=60+(random.randint(1,5)*4),font = fonts)

                        elif element[2].isdigit():    
                            page=PC.Signle_Line_Writter(page,str(element),linenumber,space = 25, x=65+(random.randint(1,5)*4),font = fonts)
                        
                        elif element[1].isdigit():    
                            page=PC.Signle_Line_Writter(page,str(element),linenumber,space = 25, x=70+(random.randint(1,5)*4),font = fonts)
                            
                        else:
                            page=PC.Signle_Line_Writter(page,str(element),linenumber,space = 25, x=80+(random.randint(3,5)*4),font = fonts)
                        linenumber=linenumber+1
                        #print(element)
       
                    else:
                        if element.find('^') > 0:
                            xr = 200
                            pow_pos =[i for i in range(len(element)) if element.startswith('^', i)]
                            for i in range(0,len(pow_pos)-1,2):
                                
                                if i == 0:
                                    page,xr=PC.Signle_Line_Writter(page,str(element[:pow_pos[i]]),linenumber,x=200+(random.randint(0,5)*7),return_x = True,font = fonts)
                                   # page,xr=PC.Signle_Line_Writter(page,str(element[pow_pos[i]+1:pow_pos[i+1]]),linenumber,x=xr, ispow = True,return_x=True)
                                   # page,xr=PC.Signle_Line_Writter(page,str(element[pow_pos[i+1]+1:pow_pos[i+2]]),linenumber,x=xr+(random.randint(0,5)*7),return_x=True)
                                if i == len(pow_pos)-2:
                                    print("ok")
                                    page,xr=PC.Signle_Line_Writter(page,str(element[pow_pos[i]+1:pow_pos[i+1]]),linenumber,x=xr, ispow = True,return_x=True,font = fonts)
                                    page=PC.Signle_Line_Writter(page,str(element[pow_pos[i+1]+1:]),linenumber,x=xr+(random.randint(0,5)*7),font = fonts)
                                else:
                                    page,xr=PC.Signle_Line_Writter(page,str(element[pow_pos[i]+1:pow_pos[i+1]]),linenumber,x=xr, ispow = True,return_x=True,font = fonts)
                                    page,xr=PC.Signle_Line_Writter(page,str(element[pow_pos[i+1]+1:pow_pos[i+2]]),linenumber,x=xr+(random.randint(0,5)*7),return_x=True,font = fonts)
                            linenumber=linenumber+1                            
                        else:
                            page=PC.Signle_Line_Writter(page,str(element),linenumber,x=200+(random.randint(0,5)*7),font = fonts)
                            linenumber=linenumber+1
                else:
                    linenumber = 0
                    pageno = pageno+1
                    flag = random.randint(0,1)
                    print('#########PAGENO###############',pageno)
                    #if pageno == 1:
                          #  page=PC.Signle_Line_Writter(page,str(name),linenumber,space = 25, x=1100+(random.randint(2,5)*9),y1=60,font = fonts)
                           # page=PC.Signle_Line_Writter(page,str(section),linenumber,space = 25, x=1145+(random.randint(2,5)*9),y1=118,font = fonts)
                            #page=PC.Signle_Line_Writter(page,str(roll),linenumber,space = 25, x=1125+(random.randint(2,5)*9),y1=175,font = fonts)
                    if flag == 1:
                        page=PC.Signle_Line_Writter(page,str(name),linenumber,space = 25, x=1000+(random.randint(2,5)*9),y1=180-(random.randint(1,5)*3),font = fonts)

                    width, height = page.size
                    left = random.randint(0,5)*5
                    top =  random.randint(0,5)*5
                    right = width - random.randint(0,5)*5
                    bottom = height - random.randint(0,5)*5
                      
                    # Cropped image of above dimension 
                    # (It will not change orginal image) 
                    page = page.crop((left, top, right, bottom)) 
                      
                    page = page.rotate(ncrandom(-1,1))
                    image = page
                    new_image = Image.new("RGBA", image.size, "WHITE") # Create a white rgba background
                    new_image.paste(image, (0, 0), image)              # Paste the image on the background. Go to the links given below for details.
                    pglist.append(new_image.convert('RGB'))
                    page.save(outputdir+fontid+'.png')
                    page=Image.open(pagedir).convert("RGBA")
                    page = page.rotate(-0.25, PIL.Image.NEAREST, expand = 1)
                    if element.find('Q.')== 0 or element.find('Ans.') == 0:
                        page=PC.Signle_Line_Writter(page,str(element),linenumber,space = 25, x=70+(random.randint(0,3)*7),colour = 'Black',font = fonts)
                        #linenumber=linenumber+1
                    else:
                        page=PC.Signle_Line_Writter(page,str(element),linenumber,x=200+(random.randint(0,5)*7),font = fonts)
                        linenumber=linenumber+1
    pageno = pageno+1
    #page = page.rotate(ncrandom(-1,1))
    page.save(outputdir+fontid+'.png')
    print("Done")
    print("The time taken :", timeit.default_timer() - starttime,'sec')  
    print("Number of pages created :",pageno)
    print("Time per page :",pageno/timeit.default_timer() - starttime)


    #image = page
    #new_image = Image.new("RGBA", image.size, "WHITE") # Create a white rgba background
    #new_image.paste(image, (0, 0), image)              # Paste the image on the background. Go to the links given below for details.
   
    
    #pglist.append(new_image.convert('RGB'))
    
    #pglist[0],pglist[-1]=pglist[-1],pglist[0]

    #del(pglist[0])
   





'''

    # importing the required modules 
    import PyPDF2 
    pdf = outputdir+'/temp.pdf'

    def PDFsplit(pdf, splits): 
        # creating input pdf file object 
        pdfFileObj = open(pdf, 'rb') 
          
        # creating pdf reader object 
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
          
        # starting index of first slice 
        start = 0
          
        # starting index of last slice 
        end = splits[0] 
          
          
        for i in range(len(splits)+1): 
            # creating pdf writer object for (i+1)th split 
            pdfWriter = PyPDF2.PdfFileWriter() 
              
            # output pdf file name 
            outputpdf = pdf.split('.pdf')[0] + str(i) + '.pdf'
              
            # adding pages to pdf writer object 
            for page in range(start,end): 
                pdfWriter.addPage(pdfReader.getPage(page)) 
              
            # writing split pdf pages to pdf file 
            with open(outputpdf, "wb") as f: 
                pdfWriter.write(f) 
      
            # interchanging page split start position for next split 
            start = end 
            try: 
                # setting split end position for next split 
                end = splits[i+1] 
            except IndexError: 
                # setting split end position for last split 
                end = pdfReader.numPages 
              
        # closing the input pdf file object 
        pdfFileObj.close() 
                  

        # split page positions 
    splits = [1] 
          
        # calling PDFsplit function to split pdf 
    PDFsplit(pdf, splits)
    '''
   