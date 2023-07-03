import sys,os
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .textsummarization import calculateNow

import os

def clear_folder():
    for filename in os.listdir("./static"):
        file_path = os.path.join("./static", filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(f"Error deleting file: {e}")

# Specify the path to the folder you want to clear

# Call the function to clear the folder



def index(request):
    clear_folder()
    if request.method == 'POST':
        saved_files = []
        for file in dict(request.FILES)['file']:
            saved_file = FileSystemStorage(location=settings.STATICFILES_DIRS[0]).save(file.name, file)
            saved_files.append(str(settings.STATICFILES_DIRS[0])+"\\"+saved_file)
        calculateNow.calculateIt(saved_files)
        data = calculateNow.getAllData()
        return render(request,"show.html",{"klsum":data[0],"lexrank":data[1],"lsa":data[2],"tfidf":data[3]})
    return render(request,'index.html')