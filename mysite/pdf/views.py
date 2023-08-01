from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.template import loader
import pdfkit
import io


def accept(request):

    if(request.method == "POST"):
        
        p = Profile()

        p.name = request.POST.get("name","")
        p.email = request.POST.get("email","")
        p.phone = request.POST.get("phone","")
        p.summary = request.POST.get("summary","")
        p.degree = request.POST.get("degree","")
        p.school = request.POST.get("school","")
        p.university = request.POST.get("university","")
        p.previous_work = request.POST.get("previous_work","")
        p.skills = request.POST.get("skills","")

        p.save()

    return render(request,"pdf/accept.html")


def resume(request, id):
    
    user_profile = Profile.objects.get(pk=id)

    template = loader.get_template("pdf/resume.html")
    html = template.render({"user_profile":user_profile,})
    options = {
        "page-size": "Letter",
        "encoding": "UTF-8",
    }
    pdf = pdfkit.from_string(html, False, options)

    response = HttpResponse(pdf, content_type="application/pdf")
    response["Content-Disposition"] = "attachment"
    filename = "resume.pdf"

    return response

def list(request):
    profiles = Profile.objects.all()
    return render(request, "pdf/list.html", {"profiles":profiles,})
