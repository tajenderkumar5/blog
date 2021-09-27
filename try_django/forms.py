from django import forms

class contactForm(forms.Form):
   full_name = forms.CharField()
   email = forms.EmailField()
   content = forms.CharField(widget=forms.Textarea)

   def clean_email(self,*args,**kwargs):
      email= self.cleaned_data.get('email')
      print(email)
      if email.endswith(".edu"):
         raise forms.ValidationError("this is not vaild email .please do not use .edu")
      return email   