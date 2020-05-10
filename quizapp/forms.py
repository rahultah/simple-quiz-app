from django import forms  
from quizapp.models import Questions

#Django allows us to create form based on Model/Schema design.
#To do so, we will create form based on 'Contact' model with all fields in it.
class QuestionForm(forms.ModelForm):  
    class Meta:  
        model = Questions
        fields = "__all__"