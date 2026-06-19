from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import os

# Create your views here.

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")
    
def projects(request):
    projects_show = [
      {"title": "Portfolio", "path":"images/portfolio.png"},
      {"title": "Photoshare", "path":"images/photoshare.png"},
      {"title": "Ecommerce", "path":"images/ecommerce.png"},
      {"title": "Covid-19 Global Data Tracker", "path":"images/data.png"},
      {"title": "Simple Django Webpage", "path":"images/nature.png"},
    ]
    return render(request, "projects.html", {"projects_show": projects_show})
    
def experience(request):
    experiences = [
      {"company": "Tenwek Mission Hospital",
      "position": "IT Intern", 
      "department": "IT Department",
      "period": "May,2023 - Aug, 2023"
      },
      {"company": "Nairobi County",
      "position": "IT Intern", 
      "department": "Innovation and Digital Economy",
      "period": "May,2024 - Aug, 2024"
      }
    ]
    return render(request, "experience.html", {"experiences": experiences})
    
def education(request):
    levels = [
      {"school": "Kirinyaga University",
      "course": "Bsc Software Engineering",
      "period": "SEP, 2021 - OCT, 2025",
      "award": "Bachelors Certificate"
      },
      {"school": "Chepalungu Boys High school",
      "course": "High School",
      "period": "JAN, 2017 - DEC, 2020",
      "award": "KCSE Certificate"
      },
      {"school": "Tilangok Primary school",
      "course": "Primary School",
      "period": "JAN, 2008 - DEC, 2016",
      "award": "KCSE Certificate"
      }
    ]
    return render(request, "education.html", {"levels": levels})
    
def contact(request):
    return render(request, "contact.html")
    
def resume(request):
    file_path = os.path.join(
        settings.BASE_DIR,
        'resume',
        'static',
        'mycv',
        'NGENO-CV.pdf'
    )

    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            response = HttpResponse(
                f.read(),
                content_type='application/pdf'
            )
            response['Content-Disposition'] = (
                'attachment; filename="NGENO-CV.pdf"'
            )
            return response

    return HttpResponse("Resume not found!", status=404)