from django.db.models.query import RawQuerySet
from django.shortcuts import render,redirect
from . models import reg1,reg2,reg3,reg4,reg5,reg6,reg7,reg8,reg9
import easygui


# Create your views here.
def studentlogin(request):
    if request.method=='POST':
        if reg4.objects.filter(Username=request.POST['Username'],password=request.POST['password']).exists():
            ex4=reg4.objects.get(Username=request.POST['Username'],password=request.POST['password'])
            easygui.msgbox('Logged succesfully..!!')
            return render(request,'index.html',{'ex4':ex4})
        else:
            context={'msg':'Please enter vali Email and Password'}
            return render(request,'studentlogin.html',context)
    return render(request,'studentlogin.html')          
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')   
def addnewcourse(request):
    return render(request,'addnewcourse.html')
def adminlogin(request):
    if request.method=='POST':
        if reg2.objects.filter(Username=request.POST['Username'],password=request.POST['password']).exists():
            ex2=reg2.objects.get(Username=request.POST['Username'],password=request.POST['password'])
            easygui.msgbox('Logged succesfully..!!')
            return render(request,'index3.html',{'ex2':ex2})
        else:
            context={'msg':'Please enter vali Email and Password'}
            return render(request,'adminlogin.html',context)
    return render(request,'adminlogin.html')
def adminregi(request):
    return render(request,'adminregi.html')
def allstudent(request):
    return render(request,'allstudent.html')
def blank(request):
    return render(request,'blank.html')
def blog(request):
    return render(request,'blog.html')
def boxed(request):
    return render(request,'boxed.html')
def breadcrumbs(request):
    return render(request,'breadcrumbs.html')
def compact(request):
    return render(request,'compact.html')
def contact(request):
    return render(request,'contact.html')
def context(request):
    return render(request,'context.html')
def coursecomment(request):
    return render(request,'coursecomment.html')
def courses(request):
    return render(request,'courses.html')
def courseview(request):
    return render(request,'courseview.html')
def dragula(request):
    return render(request,'dragula.html')
def dropify(request):
    return render(request,'dropify.html')
def events(request):
    return render(request,'events.html')
def homes(request):
    return render(request,'homes.html')
def horizontal(request):
    return render(request,'horizontal.html')
def ind(request):
    return render(request,'ind.html')
def index2(request):
    return render(request,'index2.html')
def index3(request):
    return render(request,'index3.html')
def instruclogin(request):
    if request.method=='POST':
        if reg3.objects.filter(Username=request.POST['Username'],password=request.POST['password']).exists():
            ex3=reg3.objects.get(Username=request.POST['Username'],password=request.POST['password'])
            easygui.msgbox('Logged succesfully..!!')
            return render(request,'index2.html',{'ex3':ex3})
        else:
            context={'msg':'Please enter vali Email and Password'}
            return render(request,'instruclogin.html',context)
    return render(request,'instruclogin.html')
def instructreg(request):
    return render(request,'instructreg.html')
def message(request):
    return render(request,'message.html')
def quiz(request):
    return render(request,'quiz.html')
def studentreg(request):
    return render(request,'studentreg.html')
def layout(request):
    return render(request,'layout.html')
def shop(request):
    return render(request,'shop.html')
def sidebar(request):
    return render(request,'sidebar.html')
def teachers(request):
    return render(request,'teachers.html')
def zoom(request):
    return render(request,'zoom.html')
def indreg(request):
    if request.method=='POST':
        ex1=reg1(name=request.POST['name'],
                 mail_id=request.POST['mail_id'],
                 phone_number=request.POST['phone_number'],
                )
        ex1.save()
        easygui.msgbox('yor response saved succesfully..!!')
        return redirect(studentlogin)
    return render(request,'indreg.html')

def adreg(request):
    if request.method=='POST':
        ex2=reg2(Username=request.POST['Username'],
                 First_name=request.POST['First_name'],
                 Last_name=request.POST['Last_name'],
                 Mail_id=request.POST['Mail_id'],
                 password=request.POST['password']
                 
                )
        ex2.save()
        easygui.msgbox('yor response saved succesfully..!!')
        return redirect(adminlogin)
    return render(request,'adreg.html')
def insreg(request):
    if request.method=='POST':
        ex3=reg3(Username=request.POST['Username'],
                 First_name=request.POST['First_name'],
                 Last_name=request.POST['Last_name'],
                 Mail_id=request.POST['Mail_id'],
                 password=request.POST['password']
                )
        ex3.save()
        easygui.msgbox('your response saved succesfully..!!')
        return redirect(instruclogin)
    return render(request,'insreg.html')

def stureg(request):
    if request.method=='POST':
        ex4=reg4(Username=request.POST['Username'],
                 First_name=request.POST['First_name'],
                 Last_name=request.POST['Last_name'],
                 Mail_id=request.POST['Mail_id'],
                 password=request.POST['password']
                )
        ex4.save()
        easygui.msgbox('your response saved succesfully..!!')
        return redirect(studentlogin)
    return render(request,'stureg.html')
def boxedreg(request):
    if request.method=='POST':
        ex5=reg5(name=request.POST['name'],
                 Password=request.POST['Password'],
                 E_Mail=request.POST['E_Mail'],
                 Confirm_Password=request.POST['Confirm_Password'])
        ex5.save()
        easygui.msgbox('data saved succesfully..!!')
        return redirect(blank)
    return render(request,'boxedreg.html')
def breadcrumbsreg(request):
    if request.method=='POST':
        ex6=reg6(Name=request.POST['Name'],
                 E_Mail=request.POST['E_Mail'],
                 password=request.POST['password'])
        ex6.save()
        easygui.msgbox('data saved succesfully..!!')
        return redirect(blank)

    return render(request,'breadcrumbsreg.html')
def contextreg(request):
    if request.method=='POST':
        ex7=reg7(Enter_Price=request.POST['Enter_Price'],
                 Parent_Category=request.POST['Parent_Category'],
                 fileToUpload=request.POST['fileToUpload'])
        ex7.save()
        easygui.msgbox('data saved succesfully..!!')
        return redirect(compact)
def zoomreg(request):
     if request.method=='POST':
        ex8=reg8(Password=request.POST['Password'],
                 token=request.POST['token'])
        ex8.save()
        easygui.msgbox('your response saved succesfully..!!')
        return redirect(zoom)
     return render(request,'zoomreg.html')
def addnewreg(request):
     if request.method=='POST':
        ex9=reg9(Enter_course_title=request.POST['Enter_course_title'],
                 from_url=request.POST['from_url'],
                 fileToUpload=request.POST['fileToUpload'],
                 overview_URL=request.POST['overview_URL'],
                 Enter_requirements=request.POST['Enter_requirements'],
                 Enter_outcome=request.POST['Enter_outcome'],
                 Enter_tags=request.POST['Enter_tags'],
                 Amount=request.POST['Amount'],
                 Enter_meta_title=request.POST['Enter_meta_title'],
                 Course_level=request.POST['Course_level'],
                 Provider=request.POST['Provider'],
                 Free_course=request.POST['Free_course'],
                 Discount=request.POST['Discount'],
                 Language=request.POST['Language'],
                 Category=request.POST['Category'],)
        ex9.save()
        easygui.msgbox('your response saved succesfully..!!')
        return redirect(courseview)
     return render(request,'addnewreg.html')
