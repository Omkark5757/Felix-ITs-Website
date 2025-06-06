from django.shortcuts import render, redirect, get_object_or_404
from .models import Felix_class
from .forms import FelixForm

# Display all courses
def all_felix(request):
    felixs = Felix_class.objects.all()
    return render(request, 'Felix_ITs/All_Felix.html', {'felixs': felixs})

# Create a new course
def create_course(request):
    if request.method == 'POST':
        form = FelixForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all_felix')  # Make sure your URL pattern is named 'all_felix'
    else:
        form = FelixForm()
    return render(request, 'Felix_ITs/felix_form.html', {'form': form})

# Update an existing course
def update_course(request, pk):
    course = get_object_or_404(Felix_class, pk=pk)
    if request.method == 'POST':
        form = FelixForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            return redirect('all_felix')
    else:
        form = FelixForm(instance=course)
    return render(request, 'Felix_ITs/felix_form.html', {'form': form})

# Delete a course
def delete_course(request, pk):
    course = get_object_or_404(Felix_class, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('all_felix')
    return render(request, 'Felix_ITs/delete_confirm.html', {'course': course})
