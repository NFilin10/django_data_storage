from .models import Document, Note
from django import forms


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('document', 'file_type',)


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('heading', 'user_data', 'file_type',)