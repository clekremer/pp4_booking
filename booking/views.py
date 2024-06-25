# booking/views.py
from django.shortcuts import render, redirect
from appointment.forms import AppointmentForm

def booking_view(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_success')
    else:
        form = AppointmentForm()
    return render(request, 'booking/booking.html', {'form': form})