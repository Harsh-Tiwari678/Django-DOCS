from django.http import HttpResponse  #now we are ready for response and request both 
from django.shortcuts import render


# now we have to make some meathods or we can say functions 

def home(request): # means ek request pe mujhe is home to return karna hai 
    # return HttpResponse("this is the home page")
    return render(request,'websites/index.html')

def about(request): # means ek request pe mujhe is about ko return karna hai 
    # return HttpResponse("this is the about page") 
    return render(request , 'websites/about.html')


def contact(request): # means ek request pe mujhe iss contatc  ko  return karna hai 
    # return HttpResponse("this is the contact page") 
     return render(request , 'websites/contact.html')

#now we have to handle routes from url.py .. bcs export vagera inta nhi hota python mein 

