from django.shortcuts import render
import json

# Create your views here.
# row = {'1':["kiran",25,"male"]}

def home(request):
    print(request.POST)
    with open('myTable.json','r') as tb:
        row = json.loads(tb.read())
    

    return render(request,'myuser/home.html',context={"rows":row})