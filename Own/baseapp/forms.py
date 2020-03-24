from django import forms
from django.contrib.auth.models import User
from baseapp.models import Pictures,Post,Profile_pic,Notices,Lectors

class Pictures_Form(forms.ModelForm):
        class Meta:
            model = Pictures
            fields= ('church_pic',)


class Profile_Form(forms.ModelForm):

        class Meta:
            model = Profile_pic
            fields= ('Priest_Name','Parishpriest_pic','Description',)

            widgets = {
                'Priest_Name':forms.TextInput(attrs={'class':'textinputclass'}),
                'Description':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}),
                }

class PostForm(forms.ModelForm):

        class Meta():
            model = Post
            fields = ('author','title','text')

            widgets = {
                'title':forms.TextInput(attrs={'class':'textinputclass'}),
                'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
                }


class NoticesForm(forms.ModelForm):
        class Meta:
            model = Notices
            fields = ['title','file',]


class LectorsForm(forms.ModelForm):
        class Meta:
            model = Lectors
            fields = ['title','file',]
