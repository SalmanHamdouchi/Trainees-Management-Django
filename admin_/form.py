from django import forms
from .models import Stagiaire, Admin
from django.core.exceptions import ObjectDoesNotExist

CHOICES = [(True, 'Oui'),
           (False, 'Non')]


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Stagiaire
        fields = '__all__'


class DateInput(forms.DateInput):
    input_type = 'date'


class AjoutAdmin(forms.ModelForm):
    class Meta:
        model = Admin
        fields = ('cin', 'prenom', 'nom', 'email', 'Numero_De_Telephone', 'A_Image')


class AjoutForm(forms.Form):
    cne = forms.CharField(max_length=15, label='CNE')
    prenom = forms.CharField(max_length=25, label='Prenom')
    nom = forms.CharField(max_length=25, label='Nom')
    email = forms.EmailField(max_length=62, label='E-mail')
    sujet = forms.CharField(label='Votre Sujet', widget=forms.Textarea(attrs={'rows': 10, 'cols': 15}))
    etablissement = forms.CharField(max_length=100, label='Etablissement')
    image = forms.ImageField(label='Image', required=False)
    cv = forms.FileField(label='C.V')

    def get_object(self, id):
        try:
            Stagiaire.objects.get(pk=id)
        except ObjectDoesNotExist:
            return False

    def clean_cne(self):
        data = self.cleaned_data['cne']
        if self.get_object(data):
            raise forms.ValidationError("Ce stagiaire est deja existant.")
        return data


class login(forms.Form):
    nom = forms.EmailField(max_length=62, label='E-mail')
    password = forms.CharField(max_length=50, label='password', widget=forms.PasswordInput)


class SuppForm(forms.Form):
    cne = forms.CharField(max_length=15, label='CNE')

    def get_object(self, id):
        try:
            Stagiaire.objects.get(pk=id)
        except ObjectDoesNotExist:
            return False

    def clean_cne(self):
        data = self.cleaned_data['cne']
        if not self.get_object(data):
            raise forms.ValidationError("Ce stagiaire est deja existant.")
        return data


class AbsenceForm(forms.Form):
    cne = forms.CharField(max_length=15, label='CNE')
    date_absence = forms.DateField(widget=DateInput, label="Date d'absence'")
    justifiee = forms.CharField(widget=forms.RadioSelect(choices=CHOICES))

    def get_object(self, id):
        try:
            Stagiaire.objects.get(pk=id)
            return True
        except ObjectDoesNotExist:
            return False

    def clean_cne(self):
        data = self.cleaned_data['cne']
        if not self.get_object(data):
            raise forms.ValidationError("Ce stagiaire n'existe pas")
        return data
