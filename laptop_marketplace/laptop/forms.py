from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.forms import ModelForm, CharField


from laptop.models import Laptop


class LaptopForm(ModelForm):

    # name = CharField(validators=[MinLengthValidator(8)])
    name = CharField(min_length=8)


    class Meta:
        model = Laptop
        fields = ['name']

    # def clean(self):
    #     cleaned_data = super().clean()
    #     if len(cleaned_data["name"]) < 8:
    #         raise ValidationError("Laptop name must be at least 8")



