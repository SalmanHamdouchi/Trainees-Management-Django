from django.db import models


class Admin(models.Model):
    cin = models.CharField(max_length=15, primary_key=True)
    prenom = models.CharField(max_length=25)
    nom = models.CharField(max_length=25)
    email = models.EmailField(max_length=62, unique=True)
    password = models.CharField(max_length=255)
    A_Image = models.ImageField(upload_to='admin', default='admin/admin.jpg', blank=True, null=True)
    Numero_De_Telephone = models.CharField(max_length=20, default='+2126482315474')

    def __str__(self):
        return self.cin


def user_directory_path(instance, filename):
    return 'stagiaire/image/{0}/{1}'.format(instance.cne, filename)


def user_directory_path_cv(instance, filename):
    return 'stagiaire/cv/{0}/{1}'.format(instance.cne, filename)


class Stagiaire(models.Model):
    cne = models.CharField(max_length=15, primary_key=True)
    prenom = models.CharField(max_length=25)
    nom = models.CharField(max_length=25)
    email = models.EmailField(max_length=62, unique=True)
    sujet = models.TextField()
    etablissement = models.CharField(max_length=100)
    date_ajout = models.DateField(auto_now_add=True)
    S_Image = models.ImageField(upload_to=user_directory_path, default='stagiaire/l60Hf.png', blank=True, null=True)
    cv = models.FileField(upload_to=user_directory_path_cv)

    def __str__(self):
        return self.cne


class absence(models.Model):
    cne = models.ForeignKey(Stagiaire, on_delete=models.CASCADE)
    date_absence = models.DateField()
    justifiee = models.BooleanField()

    def __str__(self):
        return Stagiaire.objects.get(pk=self.cne).cne
