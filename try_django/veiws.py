from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from .forms import contactForm
from werewolf.models import werewolf


def home_page(request):
    my_title="ready to blog"
    qs = werewolf.objects.all()[:5]
    context = {"title":"welcome to werewolf blog", 'werewolf_list':qs}
    
    return render(request,"home.html", context )

    
def about_page(request):
    return render(request,"hello_world.html",{"title":"about"})

    
def contact_page(request):
    
    form = contactForm(request.POST or None)
    if form.is_valid():
       print(form.cleaned_data)
    context = {
        "title": "contact us",
        "form": form
    } 
    return render(request,"form.html",context)
    

def example_page(request):
    context  = {"title":"Example"} 
    template_name= "hello_world.html"
    template_obj = get_template(template_name)
    return HttpResponse(template_obj.render(context))   


