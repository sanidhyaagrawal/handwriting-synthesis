from django.shortcuts import render, redirect
from . import Text_Wrap 
from . import Text_Render 
from . import a4toblocks as a4tb
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.db.models import Q
# Create your views here.
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse,JsonResponse
#from .models import template
from .models import template 
from django.db.models import Count
from django.contrib.auth import logout
from django.conf import settings
from django.http import FileResponse


def view_404(request, exception=None):
    # make a redirect to homepa
    return redirect('/')

def home(request):
    print('home')
    
    if request.user.is_active:
        print(request.user.username)
        userfonts=template.objects.filter(username=request.user.username).order_by('-id')
        fonts=template.objects.all().filter(~Q(username=request.user.username)).order_by('-id')[:50]
        return render(request,'index.html',{'userfonts':userfonts,'fonts':fonts })
    else:
        fonts=template.objects.all().order_by('-id')[:50]
        print('####nottttt logged in')
        return render(request,'index.html',{'fonts':fonts})
    
def your_fonts(request):
    print('your_fonts')
    return redirect('/#portfolio')

def deletefont(request,value):
    print('your_fonts')
    print('####DELETED ID#####', value)
    fontID= value
    try:
        userfont=template.objects.get(id=fontID)
    except:
       return redirect('/#portfolio')
    if userfont.username ==  request.user.username:
        template.objects.filter(id=fontID).delete()
    print('###Deleted###')
    return redirect('/#portfolio')


def render_text(request):
    print('render_text')
    return render(request,'render_text.html')


def save_preview(request):
    print('############save_preview##########')
    width = request.POST['width']
    fontID= request.POST['fontID']
    print('###########width$$$$$$$===  ',width)
    print('##########fontid$$$$$$$===  ',fontID)
    t = template.objects.get(id=int(fontID))
    t.font_width = width  # change field
    t.save()
    print('##Saved##')
    response_data = {}
    response_data['seved'] = True
    response_data['True'] = "True"
    print(response_data['seved'])
    return JsonResponse(response_data)

def templateupload(request):
    context = {}  
    print('####################helo#######')
    template_id=template.objects.all().count()+2
    
    if request.method == 'POST':
        images = []
        response_data = {}
        template1 = request.FILES['template1']
        template2 = request.FILES['template2']
        template3 = request.FILES['template3']
        print(template1.name,template_id)
        
        print(request.user.username)
        namet1= (str(template_id)+'_'+request.user.username+'_from1')
        namet2= (str(template_id)+'_'+request.user.username+'_from2')
        namet3= (str(template_id)+'_'+request.user.username+'_from3')

        fs = FileSystemStorage(location=settings.MEDIA_ROOT+'/templates')
        url1 = fs.save(namet1, template1) #/media/35_77777_f1.jpg
        url2 = fs.save(namet2, template2)
        url3 = fs.save(namet3, template3)
        images.append('/templates/'+namet1)
        images.append('/templates/'+namet2)
        images.append('/templates/'+namet3)
        print(images)
        temp = template.objects.create(username=request.user.username, template1 =images[0], template2=images[1],template3=images[2],font_width=55 )
        a4tb.a4toblocks(images,str(temp.pk))
        response_data['id'] = temp.pk
        response_data['font_preview'] = str(temp.pk)+'.png'
        print('############worked#######', temp.template1)
        create_preview(temp.pk,request.user.username)
        #return render(request, 'upload.html', context)
        return JsonResponse(response_data)

def preview_tinkering(request):
    
	print('############preview_tinkering#######')
	response_data = {}
	width = request.POST['width']
	fontID= request.POST['fontID']
	print('width= ',width)
	print('fontID ',fontID)
	print('request.user.username- ',request.user.username)
	create_preview(int(fontID),request.user.username,int(width))
	response_data['font_preview'] = str(fontID)+'.png'
	print('path = ',response_data['font_preview'])
	return JsonResponse(response_data)
   

def logout(request):
    auth.logout(request)
    return redirect('/#onboarding')

def create_font(request):
    return render(request,'create_font.html')

def signupcheck(request):
        print('signupcheck')
        response_data = {}
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        response_data['access_granted'] = False
        if len(username)<3:
            response_data['error'] = 'Username must be atlest 3 characters'    
            return JsonResponse(response_data)

        elif User.objects.filter(username=username).exists():
            response_data['error'] = 'Username Already Taken'
            return JsonResponse(response_data)    

        elif len(password1)==0:
            response_data['error'] = 'Input Password'
            return JsonResponse(response_data)

        elif len(password1)<5:
            response_data['error'] = 'Password must be atlest 5 characters'
            return JsonResponse(response_data)
        
        elif len(password1)>5 and len(password2)==0:
            response_data['error'] = 'Please enter the same password to confirm'
            return JsonResponse(response_data)

        elif len(password2)>5 and len(password1)==0:
            response_data['error'] = 'Enter the password in both the fields'
            return JsonResponse(response_data)

        elif password1 != password2:
                response_data['error'] = 'Password does not mach'
                return JsonResponse(response_data)
        else:
            response_data['access_granted'] = True
            response_data['error'] = 'Looks Good! You may submit'
            return JsonResponse(response_data)
            
def logincheck(request):
        print('logincheck')
        response_data = {}
        response_data['access_granted'] = False
        username = request.POST['username']
        password = request.POST['password']    
        print(username)
        print(password)
        user = auth.authenticate(username = username, password=password)
        print('##############LOGIIN###############')
        if user is not None:
            print(username, 'access_granted' )
            resp=  str('Welcome ' + username+ ' you may proceed to login-')
            response_data['access_granted'] = True
            response_data['error'] = resp
            return JsonResponse(response_data)
        else:
            print(username)
            if User.objects.filter(username=username).exists():
                response_data['error'] = 'Invalid Password'
                return JsonResponse(response_data)
            else:
                response_data['error'] = 'Username does not exist'
                return JsonResponse(response_data)

def signup(request):
    print('Signup')


    if request.method == 'POST':
        print('##########Signup#########')
        #name= request.POST['name']
        response_data = {}
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        print(username,password1,password2)

        if User.objects.filter(username=username).exists():
            response_data['error'] = 'Username Already Taken'
            return JsonResponse(response_data)    

        elif len(username)<3:
            response_data['error'] = 'Username must be atlest 3 characters'    
            return JsonResponse(response_data)

        elif len(password1)<5 or len(password2)<5:
            response_data['error'] = 'Password must be atlest 5 characters'
            return JsonResponse(response_data)
        
        elif password1 != password2:
             response_data['error'] = 'Password does not mach'
             return JsonResponse(response_data)
        
        else:
            user = User.objects.create_user(username=username, password =password1, last_name=password1 )
            user.save();
            user = auth.authenticate (username = username, password=password1)
            if user is not None:
                    auth.login(request, user)
                    print('#############Signup_End###############')
                    return render(request,'create_font.html')

        
    else:
         print('Fuckkkkkkkkkkkkkkkkkkkkkkkkk')
         
        

def login(request):
    if request.method == 'POST':
        response_data = {}
        username = request.POST['loginusername']
        password = request.POST['password']
        print(username)
        user = auth.authenticate(username = username, password=password)
        print('##############LOGIIN###############')
        if user is not None:
             auth.login(request, user)
             return redirect('/create_font')
        else:
             if User.objects.filter(username=username).exists():
                 response_data['error'] = 'Invalid Password'
                 return JsonResponse(response_data)
             else:
                  response_data['error'] = 'Username does not exist'
                  return JsonResponse(response_data)

def UserInputText(request):
    global text

    filename = exam
    line1= 'Font Id- 32'
    line2= 'Created By- Username'
    line3= 'Date- 2 Jan 2019'
    Text_Wrap.write(filename,line1,line2,line3)
    return render(request,'index.html')


def create_preview(fontid, Username,width=55):
    filename = 'exam.txt' # Examlpe file created by admin
    line1= 'Font Id- '+ str(fontid)
    line2= 'Created By- '+str(Username)
    line3= 'www.sanidhya.com'
    Text_Wrap.write(filename,line1,line2,line3,fontid,Username,width)
    print('######EXAMPLE CREATED SUCESS######','fontid = =',fontid)





def rendertext(request):
    
    print('##########render#######')
    
    if request.method == 'POST':
        try: 
            response_data = {}
            fontid = request.POST['fontid']

            try:
                 txtfile = request.FILES['txtfile']
                 flag=1
            except:
                 pinput = request.POST['pinput']
                 flag=0
            
            text = pinput.split('\n')
            i=0
            out=[]
            if len(text) == 1:
                out.append(text[i])
            else:    
              for i in range(0,len(text)):
                 if i==len(text)-1:
                    out.append(text[i])
                    break
                 else:
                    out.append(text[i][:-1])    
            print(text)
            print(len(text))
            print(out)
            line1 = request.POST['line1']
            line2 = request.POST['line2']
            line3 = request.POST['line3']
            try:
                width = request.POST['width']
                if width < 40:
                    width=template.objects.get(id=int(fontid)).font_width
            except:    
                width=template.objects.get(id=int(fontid)).font_width
            print('####width####', width)
            #fs = FileSystemStorage(location=settings.MEDIA_ROOT+'/textfiles')
            #url = fs.save(txtfile.name, txtfile) #/media/35_77777_f1.jpg
            #path= url
            #print('#######path#########', path)
            name = Text_Render.write(out,line1,line2,line3,fontid,width)
            print('######EXAMPLE CREATED SUCESS######','fontid = =',fontid)
            response = FileResponse(open(name, 'rb'))
            return response
        except:
            return redirect('/#portfolio')

       #return render(request, 'upload.html', context)
        


