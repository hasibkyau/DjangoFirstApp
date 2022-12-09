from django import forms

class user_form(forms.Form):
    user_name = forms.CharField(label="Full Name", required=True, initial="", widget=forms.TextInput(
        attrs= {'placeholder':'Enter Your Full Name'}
    ))
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
    