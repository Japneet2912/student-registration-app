from django.shortcuts import render,HttpResponse,get_object_or_404
from datetime import datetime
from student.models import details1
from django.contrib import messages

# from django.shortcuts import get_object_or_404
# Create your views here.



def index(requests):
    if requests.method == "POST":
        name = requests.POST.get("name")
        stu_class = requests.POST.get("class")
        roll = requests.POST.get("roll")
        activity = requests.POST.get("activity")
        date = datetime.today()
        records = details1(stu_name = name,stu_class = stu_class,stu_rollno = roll,stu_activity = activity,date = date)
        
        existing_record = details1.objects.filter(stu_rollno = roll).exists()

        if existing_record:
            messages.error(requests,"This record is already existing")
            return render(requests,'index.html')    
        else:
        
            records.save()
            messages.success(requests, "You have registered Successfully.")
            return render(requests,'index.html')
        
    return render(requests,'index.html')
        


    # return HttpResponse("this is the homepage")



def details(requests):
    students = details1.objects.all()
    context = {"students":students}
    return render(requests,'details.html',context=context)



def delete(requests,id):
    print("id is: ",id)
    details1.objects.filter(id=id).delete()
    students = details1.objects.all()
    context = {"students":students}
    messages.success(requests, "Record deleted Successfully.")
    return render(requests,'details.html',context=context)


def update(requests,id):
    student = details1.objects.filter(id=id)
    data = {"student":student}
    print(data)
    return render(requests,'update.html',data)

     

def editrecord(requests,id):
    record = get_object_or_404(details1, id=id)  
    if requests.method == "POST":
          record.stu_name = requests.POST.get('name')
          record.stu_class = requests.POST.get('class')
          record.stu_activity = requests.POST.get('activity')
          messages.success(requests, "Record Updated Successfully.")
          record.save()
    
    students = details1.objects.all()
    context = {"students":students}
    return render(requests,'details.html',context=context)

