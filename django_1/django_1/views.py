from django.http import HttpResponse 
from django.shortcuts import render
#now we are ready for response and request both 

# now we have to make some meathods or we can say functions 

def home(request): # means ek request pe mujhe is home to return karna hai 
    # return HttpResponse("this is the home page")
    return render(request,'index.html')

def about(request): # means ek request pe mujhe is home to return karna hai 
    return HttpResponse("this is the about page") 


def contact(request): # means ek request pe mujhe is home to return karna hai 
    return HttpResponse("this is the contact page") 

#now we have to handle routes from url.py .. bcs export vagera inta nhi hota python mein 

