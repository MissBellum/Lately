import os
import anthropic
from django.shortcuts import render

# Create your views here.
def home(request):
    """View function for homepage of site"""
    return render(request, 'home.html')

def index(request):
    """View function for homepage of site"""
    return render(request, 'index_fit.html')

def test(request):
    # Create an instance of the Anthropics API client
    client = anthropic.Anthropic(api_key=os.getenv('sonnet'))
    response = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Write a short story."}],
    system="You are a creative writing assistant.",
    stop_sequences=["The end."],
    temperature=0.9
    )
    return render(request, 'test.html', context=response)
