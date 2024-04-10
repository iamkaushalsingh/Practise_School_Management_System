from django.shortcuts import render, redirect

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Permission
from django.contrib.auth.decorators import login_required

from .models import StudentProfile, TeacherProfile
from .forms import StudentRegistrationForm, TeacherRegistrationForm, StudentProfileForm, TeacherProfileForm

def register_view(request):
    return render(request, 'registration.html')

def register_student(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user_profile = form.save()
            student_profile = StudentProfile(
                user                = user_profile, 
                registration_number = form.cleaned_data.get("registration_number"),
                address             = form.cleaned_data.get("address"),
                phone               = form.cleaned_data.get("phone"),
                department          = form.cleaned_data.get("department"),
                batch               = form.cleaned_data.get("batch")
            )
            student_profile.save()
            permissions = Permission.objects.filter(
                content_type__app_label='dashboard',
                codename__in=[
                    'can_apply_to_internship',
                    'can_view_applied_internships',
                ]
            )
            for permission in permissions:
                user_profile.user_permissions.add(permission)
            login(request, user_profile)
            return redirect('dashboard_view')
        else:
            print(form.errors)
            return render(request, 'student_registration.html', {'form': form, 'error': form.errors})
    else:
        form = StudentRegistrationForm()
    return render(request, 'student_registration.html', {'form': form})

def register_teacher(request):
    if request.method == 'POST':
        form = TeacherRegistrationForm(request.POST)
        if form.is_valid():
            user_profile = form.save()
            teacher_profile = TeacherProfile(
                user        = user_profile,
                teacher_id  = form.cleaned_data.get("teacher_id"),
                address     = form.cleaned_data.get("address"),
                phone       = form.cleaned_data.get("phone"),
                department  = form.cleaned_data.get("department"),
                
            )
            teacher_profile.save()
            permissions = Permission.objects.filter(
                content_type__app_label='dashboard',
                codename__in=[
                    'can_post_internship',
                    'can_edit_internship',
                    'can_delete_internship',
                    'can_view_internship_applications',
                ]
            )
            for permission in permissions:
                user_profile.user_permissions.add(permission)
                
            login(request, user_profile)
            return redirect('dashboard_view')
        else:
            return render(request, 'teacher_registration.html', {'form': form, 'error': "Something went wrong."})
    else:
        form = TeacherRegistrationForm()
    return render(request, 'teacher_registration.html', {'form': form})

@login_required
def edit_profile_view(request):
    if hasattr(request.user, 'studentprofile'):
        profile = request.user.studentprofile
        ProfileForm = StudentProfileForm
        editTemplate = "edit_student_profile.html"
    elif hasattr(request.user, 'teacherprofile'):
        profile = request.user.teacherprofile
        ProfileForm = TeacherProfileForm
        editTemplate = "edit_teacher_profile.html"
    else:
        return redirect('logout')
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_view') 
        else:
            return render(request, editTemplate, {'form': form, 'error': "Something went wrong.", "profile" : profile})
    else:
        form = ProfileForm(instance=profile)
        
    return render(request, editTemplate, {'form': form, 'profile':profile})

@login_required
def profile_view(request):
    if hasattr(request.user, 'studentprofile'):
        profile = request.user.studentprofile
    elif hasattr(request.user, 'teacherprofile'):
        profile = request.user.teacherprofile
    else:
        return redirect("login_view")

    return render(request, 'profile.html', {'profile': profile})


def login_view(request):
    if request.user.is_authenticated:
        if hasattr(request.user, 'studentprofile') or hasattr(request.user, 'teacherprofile'):
            return redirect('profile_view')
        else:
            return redirect('logout_view')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                next_url = request.GET.get('next')
                if next_url:
                    return redirect(next_url)
                else:
                    return redirect('dashboard_view')
            else:
                return render(request, 'login.html', {'form': form, 'error': 'Invalid username or password'})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login_view')
