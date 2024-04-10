from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required

from .models import Internship, Application
from .forms import InternshipForm, ApplicationForm


@login_required
def dashboard_view(request):
    if hasattr(request.user, 'studentprofile'):
        internships = Internship.objects.all()
        applied_internships = [ application.internship for application in Application.objects.filter(student=request.user)]
        applied_ids = [internship.id for internship in internships if internship in applied_internships]
        unavailable_ids = [internship.id for internship in internships if internship.is_active == False]
        
        return render(request, 'student_dashboard.html', {'internships': internships, 'applied_ids':applied_ids, 'unavailable_ids':unavailable_ids})
    
    elif hasattr(request.user, 'teacherprofile'):
        internships = Internship.objects.all()
        return render(request, 'teacher_dashboard.html', {'internships': internships, "user":request.user})
    else:
        return redirect('logout_view')

@login_required
@permission_required('dashboard.can_post_internship', raise_exception=True)
def post_internship(request):
    if request.method == 'POST':
        form = InternshipForm(request.POST)
        if form.is_valid():
            internship = form.save(commit=False)
            internship.teacher = request.user
            internship.save()
            return redirect('dashboard_view') 
    else:
        form = InternshipForm()
    return render(request, 'post_internship.html', {'form': form})

@login_required
@permission_required('dashboard.can_edit_internship', raise_exception=True)
def edit_internship(request, internship_id):
    internship = get_object_or_404(Internship, id=internship_id)
    if request.user.is_authenticated and request.user == internship.teacher:
        if request.method == 'POST':
            form = InternshipForm(request.POST, instance=internship)
            if form.is_valid():
                form.save()
                return redirect('dashboard_view')
        else:
            form = InternshipForm(instance=internship)
        return render(request, 'edit_internship.html', {'form': form, 'internship': internship})
    else:
        return redirect('dashboard_view')

@login_required
@permission_required('dashboard.can_delete_internship', raise_exception=True)
def delete_internship(request, internship_id):
    internship = get_object_or_404(Internship, id=internship_id)
    if request.user.is_authenticated and request.user == internship.teacher:
        if request.method == 'POST':
            internship.delete()
            return redirect('dashboard_view')
        else:
            return render(request, 'delete_internship.html', {'internship': internship})
    else:
        return redirect('dashboard_view')

@login_required
@permission_required('dashboard.can_apply_to_internship', raise_exception=True)
def apply_internship(request, internship_id):
    internship = get_object_or_404(Internship, id=internship_id)
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.internship = internship
            application.student = request.user
            application.save()
            
            internship.is_active = False
            internship.save()
            
            return redirect('dashboard_view')
    else:
        form = ApplicationForm()
    return render(request, 'apply_internship.html', {'form': form, 'internship': internship})

@login_required
@permission_required('dashboard.can_view_applied_internships', raise_exception=True)
def applied_internships(request):
    if request.user.is_authenticated:
        applications = Application.objects.filter(student=request.user)
        return render(request, 'applied_internships.html', {'applications': applications})
    else:
        return redirect('dashboard_view')

@login_required
@permission_required('dashboard.can_view_internship_applications', raise_exception=True)
def internship_applications(request, internship_id):
    applications = Application.objects.filter(internship_id=internship_id)
    internship = Internship.objects.get(id=internship_id)
        
    return render(request, 'internship_applications.html', {'applications': applications, 'internship':internship})
