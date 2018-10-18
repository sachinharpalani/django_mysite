from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100, initial="sachin")
    img = forms.FileField()

    # def clean_name(self):
    #     print('clean name')
    #     name = self.cleaned_data['name']
    #     if name == 'pradeep':
    #         raise forms.ValidationError('Name cannot be %s' % (name))
    #     return name

    # def clean(self):
    #     print('clean')
    #     super().clean()
