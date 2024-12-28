from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")


def projects(request):
    projects_show=[
    
       {"title":"Machine learing",
        "path":"images/mli.jpg",
        "link":"https://github.com/Anarulislam10/MachineLearning",
        },

         {"title":" Ecommerce",
        "path":"images/ec.jpg",
        "link":"https://github.com/Anarulislam10/MachineLearning",
        },

         {"title":" portfolio",
        "path":"images/portfolio.jpg",
        "link":"https://github.com/Anarulislam10/MachineLearning",
        },

         {"title":" Timetable Schedular",
        "path":"images/timtable.PNG",
        "link":"https://github.com/Anarulislam10/MachineLearning",
        }  
    
    ]

    return render(request,"projects.html",{"projects_show":projects_show})