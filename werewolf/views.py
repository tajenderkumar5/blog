
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.shortcuts import render,get_object_or_404, redirect
from .forms import blogpostmodelForm
from .forms import blogpostForm
from .models import werewolf
 

#CRUD
#POST->CREATE /UPDATE /DELETE
#CREATE UPDATE RETREIVE DELETE
def  were_wolf_list_veiw(request):
       
   qs = werewolf.objects.all()
   template_name='list.html'
   context={'object_list': qs}
   return render(request ,template_name,context) 

def   were_wolf_detail_veiw(request,slug):
      obj =  get_object_or_404(werewolf, slug=slug)
      template_name='detail.html'
      context={"object":obj}
      return render(request,template_name,context) 
@staff_member_required
def  were_wolf_update_veiw(request,slug):
      obj =  get_object_or_404(werewolf, slug=slug)
      form=blogpostmodelForm(request.POST or None, instance=obj)
      if form.is_valid():
            form.save()
      template_name='form.html'
      context={'form':form,"title":f"update {obj.title}"}
      return render(request,template_name,context)


@staff_member_required
def  were_wolf_create_veiw(request):

   
   form = blogpostmodelForm(request.POST or None)
   if form.is_valid():

      obj = form.save(commit=False)
      obj.user= request.user
      obj.save()
      form = blogpostmodelForm()
   template_name='form.html'
   context={'form':form}
   return render(request,template_name,context) 
@staff_member_required
def  were_wolf_delete_veiw(request,slug):
      obj =  get_object_or_404(werewolf, slug=slug)
      template_name='delete.html'
      if request.method=="POST":
            obj.delete()
            return redirect("/blog")
      context={"object":obj}
      return render(request,template_name,context) 

