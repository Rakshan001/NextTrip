


from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Review
from nextbus.models import Bus  # Import the Bus model

def review_form(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user  # Assign the current user to the review
            review.save()
            return redirect('reviews:all_reviews')  # Redirect to all reviews page
    else:
        form = ReviewForm()
    return render(request, 'reviews/review_form.html', {'form': form})

def all_reviews(request):
    reviews = Review.objects.all()
    # Fetch the bus details
    buses = Bus.objects.all()  # Or use a more specific query to get the required bus details
    bus_details = [{'number': bus.number, 'reg_number': bus.reg_number} for bus in buses]
    return render(request, 'reviews/all_reviews.html', {'reviews': reviews, 'bus_details': bus_details})




# it is used to display particular bus reviews
from django.shortcuts import render
from .models import Review

def bus_reviews(request, bus_name):
    # Fetch reviews for the specified bus
    bus_reviews = Review.objects.filter(bus__name=bus_name)
    context = {'bus_reviews': bus_reviews, 'bus_name': bus_name}  # Pass bus_name to the context
    return render(request, 'reviews/particularbus.html', context)




# Queries
# reviews/views.py

from django.shortcuts import render
from django.http import HttpResponse
from .forms import QueryForm

def submit_query(request):
    if request.method == 'POST':
        form = QueryForm(request.POST)
        if form.is_valid():
            # Process the form data and save it to the database
            form.save()
            # return HttpResponse('Query submitted successfully!')
            return render(request, 'reviews/Query.html')
        else:
            # Handle invalid form submission
            return HttpResponse('Invalid form data!')
    else:
        # Handle GET request
        return HttpResponse('Only POST requests are allowed!')
