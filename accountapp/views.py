from django.http import HttpResponse
from django.shortcuts import render

from accountapp.models import HelloWorld


# Create your views here.


def hello_world(request):
    if request.method == "POST":

        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        return render(request, 'accountapp/hello_world.html', context={'hello_world_output': new_hello_world})
        # new_hello_world는 객체임.
    else:
        return render(request, 'accountapp/hello_world.html', context={'text': 'GET Method'})


