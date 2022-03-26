from django.shortcuts import render

from django.http import HttpResponse

from .models import Topic,AccessRecord,Webpage

from app1.forms import FormName


# Create your views here.


def index(request):
    abc = AccessRecord.objects.order_by('-date')
    date_dict = {'access':abc}
    return render(request,'app1/index.html',context=date_dict)

def form_name(request):
    form = FormName()
    if request.method == "POST":
        form = FormName(request.POST)

        if form.is_valid():
            print("validation success")
            print(form.cleaned_data['roll_number'])
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['text'])
    return render(request,'app1/form.html',{'form':form})


