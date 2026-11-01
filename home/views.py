from django.shortcuts import render


def index(request):
    """Show the homepage."""
    return render(request, 'home/index.html')
