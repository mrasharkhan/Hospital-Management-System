from ctypes import Union
from distutils import dep_util
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib import messages
from numpy import array, empty
from requests import post
from Hospital.models import Administrator, AdmissionDetails, Appointment, Doctor, Department, LabTechnician, Laboratories, Nurses, Patient, Prescription, Qualification, Rooms, TestReports, Tests
from django.contrib.auth.models import  User, auth
import pymysql

def homepage(request):
    return render(request, "homepage.html")
def lab_tech(request):
     if request.method== 'POST':
          name=request.POST['name']
          pid=request.POST['Patient name']
          tid=request.POST['Test name']
          lab=request.POST['Lab name']
          result=request.POST['result']
          dt=request.POST['Date']
          if Patient.empAuth_objects.filter(p_name=pid).exists() and Laboratories.empAuth_objects.filter(lab_name=lab).exists() and Tests.empAuth_objects.filter(test_name=tid).exists():
               p=Patient(p_id=pid)
               c=Laboratories(lab_id=lab)
               d=Tests(test_id=tid)
               a=TestReports.empAuth_objects.create(p_name=p, l_name=c, r_date=dt ,result=result, r_name=name, t_name=d)
               messages.info(request,'*Test Report Generated')
               return redirect('lab_tech')
          else:
               messages.info(request,'*invalid credentials')
               return redirect('lab_tech')
     else:
          return render(request, "lab_tech.html")
def patient(request):
     if request.method== 'POST':
          dept=request.POST['dept']
          dname=request.POST.get('dname', False)
          time=request.POST['time']
          date=request.POST['date']
          pid=request.POST['pid']
          pname=request.POST['pname']
          if Patient.empAuth_objects.filter(p_id=pid).exists() and Doctor.empAuth_objects.filter(d_name=dname).exists() and Department.empAuth_objects.filter(dept_name=dept).exists():
               p=Patient(p_id=pid)
               c=Department.empAuth_objects.get(dept_name=dept)
               d=Doctor.empAuth_objects.get(d_name=dname, dept=c.dept_id)
               x=Doctor(d_id=d.d_id)
               a=Appointment(p=p, d=x, a_date=date ,a_time=time, p_name=pname )
               a.save();
               messages.info(request,'*Appointment Succesfull.')
               return render(request,"patient.html")
          else:
               messages.info(request,'*invalid credentials')
               return redirect('patient')
     else:
          return render(request, "patient.html")

def login1(request):
     if request.method== 'POST':
          username= request.POST.get('Login ID', False)
          password= request.POST.get('Password', False)
          if Patient.empAuth_objects.filter(p_id=username, p_password=password).exists():
               info=Patient.empAuth_objects.all().filter(p_id=username).only("p_id")
               x=Patient.empAuth_objects.get(p_id=username)
               alltestreports=TestReports.empAuth_objects.all().filter(p_name=x.p_name).only("p_name")
               allprescriptions=Prescription.empAuth_objects.all().filter(p=username).only("p")
               return render( request,"patient.html",{"information":info, "alltestreports": alltestreports, "allprescriptions":allprescriptions})
          elif Administrator.empAuth_objects.filter(a_id=username, a_password=password).exists():
               info=Administrator.empAuth_objects.all().filter(a_id=username).only("a_id")
               return render( request,"administrator.html",{"information":info})
          elif Doctor.empAuth_objects.filter(d_id=username, d_password=password).exists():
               info=Doctor.empAuth_objects.all().filter(d_id=username).only("d_id")
               x=Doctor.empAuth_objects.get(d_id=username)
               dinfo=Department.empAuth_objects.all().filter(dept_id=x.dept).only("dept_id")
               qinfo=Qualification.empAuth_objects.all().filter(d_id=x.d_id).only("d_id")
               allappointments= Appointment.empAuth_objects.all().filter(d=username).only("d")
               allprescriptions=Prescription.empAuth_objects.all().filter(d=x.d_name).only("d")
               alltestreports=TestReports.empAuth_objects.all()
               return render(request,"doctor.html",{"information":info,"Department":dinfo,"Qualification":qinfo,"allappointments": allappointments, "allprescriptions":allprescriptions, "alltestreports": alltestreports})
          elif LabTechnician.empAuth_objects.filter(l_id=username, l_password=password).exists():
               info=LabTechnician.empAuth_objects.all().filter(l_id=username).only("l_id")
               x=LabTechnician.empAuth_objects.get(l_id=username)
               y=Laboratories.empAuth_objects.get(lab_id=x.lab)
               dinfo=Department.empAuth_objects.all().filter(dept_id=y.dept).only("dept_id")
               linfo=Laboratories.empAuth_objects.all().filter(lab_id=x.lab).only("lab_id")
               alltestreports=TestReports.empAuth_objects.all()
               return render( request,"lab_tech.html",{"information":info,"Department":dinfo,"Lab":linfo, "alltestreports": alltestreports})
          else:
               messages.info(request,'*invalid credentials')
               return redirect('login1')
          
     else:    
          return render(request, "login1.html")  
def logreg(request):
     if request.method=='POST':
          name=request.POST['name']
          id=request.POST.get('id', False)
          password=request.POST['password']
          password2=request.POST['password2']
          cnic=request.POST['cnic']
          address=request.POST['address']
          age=request.POST['age']
          sex=request.POST.get('sex', False)
          email=request.POST['email']
          if password==password2:
               if Patient.empAuth_objects.filter(p_id=id).exists():
                    messages.info(request,'*username taken')
                    return redirect('logreg')
               elif Patient.empAuth_objects.filter(p_email=email).exists():
                    messages.info(request,'*email already exists')
                    return redirect('logreg')
               else:
                    a=Patient.empAuth_objects.create(p_name=name, p_id=id, p_password=password, p_cnic=cnic, p_address=address,p_age=age,p_sex=sex,p_email=email)
                    a.save();
                    messages.info(request,'*succeefully registered, now login.')
                    return redirect('login1')
          else:
               messages.info(request,'*password not matching...')
               return redirect('logreg')
     else:
          return render(request, "logreg.html") 
def register(request):
     if request.method=='POST':
          name=request.POST['name']
          id=request.POST.get('id', False)
          password=request.POST['password']
          password2=request.POST['password2']
          cnic=request.POST['cnic']
          address=request.POST['address']
          age=request.POST['age']
          sex=request.POST.get('sex', False)
          email=request.POST['email']
          if password==password2:
               if Patient.empAuth_objects.filter(p_id=id).exists():
                    messages.info(request,'*username taken')
                    return redirect('register')
               elif Patient.empAuth_objects.filter(p_email=email).exists():
                    messages.info(request,'*email already exists')
                    return redirect('register')
               else:
                    p=Patient.empAuth_objects.create(p_name=name, p_id=id, p_password=password, p_cnic=cnic, p_address=address,p_age=age,p_sex=sex,p_email=email)
                    p.save();
                    messages.info(request,'*succeefully registered, now login.')
                    return redirect('login1')
          else:
               messages.info(request,'*password not matching')
               return redirect('register')
     else:
          return render(request, "register.html")       
def administrator1(request):
     if request.method== 'POST':
          name=request.POST['D_name']
          id=request.POST['D_id']
          password=request.POST['D_password']
          cnic=request.POST['D_cnic']
          address=request.POST['D_address']
          age=request.POST['D_age']
          salary=request.POST['D_salary']
          sex=request.POST.get('D_sex', False)
          senioritylevel=request.POST['D_senioritylevel']
          email=request.POST['D_email']
          Dpt=request.POST['Dept']
          if Doctor.empAuth_objects.filter(d_id=id).exists():
               messages.info(request,'*username taken')
               return redirect('administrator1')
          elif Doctor.empAuth_objects.filter(d_email=email).exists():
               messages.info(request,'*email already exists')
               return redirect('administrator1')
          else:
               c=Department(dept_id=Dpt)
               d=Doctor(d_name=name, d_id=id, d_password=password, d_cnic=cnic, d_address=address,d_age=age,d_salary=salary,d_senioritylevel=senioritylevel,d_sex=sex,d_email=email, dept=c)
               d.save();
               messages.info(request,'*Registeration successfull')
               return redirect('administrator1')
     else:
          return render(request, "administrator1.html")
def administrator2(request):
     if request.method== 'POST':
          name=request.POST['name']
          id=request.POST['userid']
          password=request.POST['password']
          cnic=request.POST['cnic']
          address=request.POST['address']
          age=request.POST['age']
          salary=request.POST['salary']
          sex=request.POST.get('sex', False)
          senioritylevel=request.POST['seniority level']
          email=request.POST['email']
          lab=request.POST['Lab']
          if LabTechnician.empAuth_objects.filter(l_id=id).exists():
               messages.info(request,'*username taken')
               return redirect('administrator2')
          elif LabTechnician.empAuth_objects.filter(l_email=email).exists():
               messages.info(request,'*email already exists')
               return redirect('administrator2')
          else:
               c=Laboratories(lab_id=lab)
               l=LabTechnician(l_name=name, l_id=id, l_password=password, l_cnic=cnic, l_address=address,l_age=age,l_salary=salary,l_senioritylevel=senioritylevel,l_sex=sex,l_email=email, lab=c)
               l.save();
               messages.info(request,'*Registeration successfull')
               return redirect('administrator2')
     else:
          return render(request, "administrator2.html")
def administrator3(request):
     if request.method== 'POST':
          name=request.POST['name']
          cnic=request.POST['cnic']
          address=request.POST['address']
          age=request.POST['age']
          salary=request.POST['salary']
          sex=request.POST.get('sex', False)
          senioritylevel=request.POST['seniority level']
          room=request.POST['room']
          c=Rooms(room_id=room)
          n=Nurses(n_name=name, n_cnic=cnic, n_address=address,n_age=age,n_salary=salary,n_senioritylevel=senioritylevel,n_sex=sex, room=c)
          n.save();
          messages.info(request,'*Registeration successfull')
          return redirect('administrator3')
     return render(request, "administrator3.html")
def administrator(request):
     if request.method=='POST':
          Pid=request.POST['patient id']
          Rid=request.POST['room id']
          if Patient.empAuth_objects.filter(p_id=Pid).exists():
               r=Rooms(room_id=Rid)
               Patient.empAuth_objects.filter(p_id=Pid).update(room=r) 

               messages.info(request,'*Registeration successfull')
               return redirect('administrator')
          else:
               messages.info(request,'*invalid credentials')
               return redirect('administrator')
     else:
          return render(request, "administrator.html")
def doctor(request):
     if request.method=='POST':
          pid=request.POST['Patient Id']
          m=request.POST.get( 'med',True)
          test=request.POST['tname']
          did=request.POST.get('Doctor')
          if Patient.empAuth_objects.filter(p_id=pid).exists():
               pt=Patient(p_id=pid)
               a=Prescription(tests=test, medicine=m, p=pt, d=did)
               a.save();
               messages.info(request,'*Prescriped')
               return redirect('doctor')
          else:
               messages.info(request,'*invalid credentials')
               return redirect('doctor')
          

     else:
          return render(request, "doctor.html")  
   

          
          



# Create your views here.
