from django.shortcuts import render, redirect
from .form import *
from .models import Stagiaire, absence, Admin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse
from django.views.generic import UpdateView
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms


@login_required(login_url='/admin_/login/')
def pdf_view(request, cne):
    with open(Stagiaire.objects.get(pk=cne).cv.url, 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=cv.pdf'
        return response


@login_required(login_url='/admin_/login/')
def view_profile(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    form = AjoutAdmin(instance=Admin.objects.get(pk=username))
    form2 = PasswordChangeForm(request.user)
    if request.method == 'POST' and 'old_password' not in request.POST:
        form = AjoutAdmin(request.POST, request.FILES, instance=Admin.objects.get(pk=username))
        if form.is_valid():
            form.save()
            form = AjoutAdmin(instance=Admin.objects.get(pk=username))
        else:
            print(form.errors)
    return render(request, "admin_/profile.html", {'Admin': Admin.objects.get(pk=username), 'form': form, 'form2': form2, 'views': change_password})


@login_required(login_url='/admin_/login/')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return redirect('profile')


@login_required(login_url='/admin_/login/')
def ajout_stagiaire(request):
    form = AjoutForm()
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    if request.method == 'POST':
        form = AjoutForm(request.POST, request.FILES)
        if form.is_valid():
            Stagiaire.objects.create(
                cne=form.cleaned_data['cne'],
                prenom=form.cleaned_data['prenom'],
                nom=form.cleaned_data['nom'],
                email=form.cleaned_data['email'],
                sujet=form.cleaned_data['sujet'],
                etablissement=form.cleaned_data['etablissement'],
                S_Image=form.cleaned_data['image'],
                cv=form.cleaned_data['cv']
            )
            messages.success(request, "stagiaire " + str(form.cleaned_data['prenom']) + " " + str(form.cleaned_data['nom']) + " ajoute avec succes")
            form = AjoutForm()
        else:
            print(form.errors)
    return render(request, 'admin_/ajouter_stagiaire.html', {'form': form, 'Admin': Admin.objects.get(pk=username)})


@login_required(login_url='/admin_/login/')
def view_login(request):
    form = login()
    if form.is_valid():
        form.save()
        form = login()
    return render(request, "admin_/login.html", {'form': form})


@login_required(login_url='/admin_/login/')
def view_stagiaire(request, cne):
    stagiaire = Stagiaire.objects.get(pk=cne)
    return render(request, "admin_/info_stagiaire.html", {'stagiaire': stagiaire})


@login_required(login_url='/admin_/login/')
def supp_stagiaire(request, cne):
    Stagiaire.objects.get(pk=cne).delete()
    return redirect('stagiaire_list')


# @method_decorator(login_required, name='dispatch')
class update_stagiaire(LoginRequiredMixin, UpdateView):
    login_url = '/admin_/login/'
    template_name_suffix = 'update.html'
    pk_url_kwarg = 'cne'
    context_object_name = 'Stagiaire'
    form_class = UpdateForm
    model = Stagiaire

    def form_valid(self, form):
        post = form.save(commit=False)
        post.updated_by = self.request.user
        post.updated_at = timezone.now()
        post.save()
        return redirect('stagiaire_list')

    def get_context_data(self, *args, **kwargs):
        context = super(update_stagiaire, self).get_context_data(*args, **kwargs)
        context["prenom"] = Admin.objects.get(pk=self.request.user.username).prenom
        context["image"] = Admin.objects.get(pk=self.request.user.username).A_Image.url
        context["s_image"] = self.get_object().S_Image.url
        return context


@login_required(login_url='/admin_/login/')
def marquer_absence(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    form = AbsenceForm()
    if request.method == 'POST':
        form = AbsenceForm(request.POST)
        if form.is_valid():
            absence.objects.create(
                date_absence=form.cleaned_data['date_absence'],
                cne=Stagiaire.objects.get(pk=form.cleaned_data['cne']),
                justifiee=form.cleaned_data['justifiee'],
            )
            form = AbsenceForm()
        else:
            print(form.errors)
    return render(request, 'admin_/marquer_absence.html', {'form': form, 'Admin': Admin.objects.get(pk=username)})


@login_required(login_url='/admin_/login/')
def afficher_tout(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    return render(request, 'admin_/trainees.html', {'stagiaires': Stagiaire.objects.all(), 'Admin': Admin.objects.get(pk=username)})
