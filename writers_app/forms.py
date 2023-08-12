from django import forms
from writers_app.models import Writer


class AddWriterForm(forms.ModelForm):

    class Meta:
        model = Writer
        fields = '__all__'
        #template_name = 'writer_app/create_writer.html'
