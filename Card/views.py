from django.shortcuts import render
from django.utils import timezone
from .models import FeedBack
from .forms import FeedBackForm

def post_list(request):
    feedbacks = FeedBack.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'card/post_list.html', {'feedbacks': feedbacks})

def download(request):
    return render(request, 'card/download.html')

def fb_new(request):
    if request.method == "POST":
        form = FeedBackForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            feedbacks = FeedBack.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
            return render(request, 'card/post_list.html', {'feedbacks': feedbacks})
    else:
        form = FeedBackForm()
    return render(request, 'card/feedback_edit.html', {'form': form})