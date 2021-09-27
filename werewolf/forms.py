from django import forms

from .models import werewolf


class blogpostForm(forms.Form):
     title = forms.CharField()
     slug = forms.SlugField()
     content = forms.CharField(widget=forms.Textarea)


class blogpostmodelForm(forms.ModelForm):

     class Meta:
          model = werewolf
          fields = ['title','slug','content']     

     def clean_title(self,*args,**kwargs):
          instance=self.instance
          title= self.cleaned_data.get('title')
          qs = werewolf.objects.filter(title__iexact=title)
          if instance is not None:
               qs= qs.exclude(pk=instance.pk)
          if qs.exists():
             raise forms.ValidationError("this title is already used .please do not use ")
          return title              