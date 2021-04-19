from django.shortcuts import render
import json

# Create your views here.
# row = {'1':["kiran",25,"male"]}

def home(request):
    print(request.method)
    
    with open('myTable.json','r') as tb:
        row = json.loads(tb.read())
    
    if request.method == "GET":
        return render(request,'myuser/home.html',context={"rows":row,"msg":""})
    
    else:
        req = request.POST.dict()
        print(req)
        flag = False
        for k,v in req.items():
            if v=='':
                flag = True

        if flag:
            return render(request,'myuser/home.html',context={"rows":row,"msg":"Fill all the fields."})
        else:
            if req['RollNumber'] in row:
                return render(request,'myuser/home.html',context={"rows":row,"msg":"Record alredy exist."})
            else:
                data =[]
                data.append(req['Name'])
                data.append(int(req['Age']))
                data.append(req['Gender'])
                row[req['RollNumber']]=data
                print(data)
                with open('myTable.json','w') as newdata:
                    newdata.write(json.dumps(row))
                return render(request,'myuser/home.html',context={"rows":row,"msg":"Record Saved."})


