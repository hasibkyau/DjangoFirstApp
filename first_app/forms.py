from django import forms
from django.core import validators
# from first_app.models import Album, Musician
from first_app import models

class MusicianForm(forms.ModelForm):
    class Meta:
        model = models.Musician
        fields = "__all__"
        # exclude = ['first_name']
        # fields = ('first_name', 'last_name')
e


# def even_or_not(value):
#     if value%2 == 1:
#         raise forms.ValidationError("please insert an even number!")

# class user_form(forms.Form):
#     user_email = forms.EmailField()
#     user_vmail = forms.EmailField()

#     def clean(self):
#         all_cleaned_data = super().clean
#         user_email = all_cleaned_data['user_email']
#         user_vmail = all_cleaned_data['user_vmail']
    
#         if user_email != user_vmail:
#             raise forms.ValidationError("Fields Don't Match !!!!!!")




class user_form3(forms.Form):
    name = forms.CharField(validators = [validators.MaxLengthValidator(10)])

    choices = (('male','Male'), ('female','Female'))
    sex = forms.ChoiceField(choices=choices, label="Sex", widget=forms.RadioSelect)
    
    
    languages = (('english','English'), ('bangla','Bangla'))
    language = forms.MultipleChoiceField(choices=languages, label="Language", widget=forms.CheckboxSelectMultiple)
    
    user_dob = forms.DateField(label="Date of Birth", widget=forms.TextInput(
        attrs={'type':'date'}
    ))
    user_email = forms.EmailField(label="Email", required=True, )






class user_form2(forms.Form):
    user_name = forms.CharField(label="Full Name", required=True, initial="", widget=forms.TextInput(
        attrs= {'placeholder':'Enter Your Full Name'}
    ))

    choices = (('male','Male'), ('female','Female'))
    sex = forms.ChoiceField(choices=choices, label="Sex", widget=forms.RadioSelect)
    
    
    languages = (('english','English'), ('bangla','Bangla'))
    language = forms.MultipleChoiceField(choices=languages, label="Language", widget=forms.CheckboxSelectMultiple)
    
    user_dob = forms.DateField(label="Date of Birth", widget=forms.TextInput(
        attrs={'type':'date'}
    ))
    user_email = forms.EmailField(label="Email", required=True, )





# <form class="" action="" method="post">
#       <label for="user_name">Full Name</label>
#       <input type="text" name="user_name" value="" required>  
#       <label for="user_email">Email</label>
#       <input type="email" name="user_email" value="" required>  
#       <input type="submit" name="submit" value="Submit">
# </form>
    