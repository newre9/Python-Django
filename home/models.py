from django.db import models

# Create your models here.
from django.forms import ModelForm, Textarea, TextInput, Select


class Contact(models.Model):
    STATUS = (
        (1, 'new'),
        (0, 'read'),
    )

    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=255)
    message = models.TextField(max_length=255)
    status = models.IntegerField(choices=STATUS, default=1)
    creatat = models.DateTimeField(auto_now_add=True)
    updateat = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "contact Form Message"
        verbose_name_plural = "contact Form Messages"


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': TextInput(attrs={'class': 'input', 'placeholder': 'Name & Surname'}),
            'subject': TextInput(attrs={'class': 'input', 'placeholder': 'Subject'}),
            'email': TextInput(attrs={'class': 'input', 'placeholder': 'Email Address'}),
            'message': TextInput(attrs={'class': 'input', 'placeholder': 'Your Message'}),
        }
