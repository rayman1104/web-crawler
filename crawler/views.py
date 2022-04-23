import logging
from django.shortcuts import render

from crawler.tasks import crawl_task
from crawler.forms import CrawlActionForm

logger = logging.getLogger(__name__)


def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CrawlActionForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            results = crawl_task.delay(form.cleaned_data['url'])
            return render(request, 'index.html', {'form': form, 'results': results.get()})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CrawlActionForm()

    return render(request, 'index.html', {'form': form})
