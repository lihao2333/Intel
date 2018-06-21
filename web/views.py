from django.shortcuts import render
from web.models import IMG
import os
import sys
import glob
import json
sample_path = 'static/images/portfolio/*.jpg'
# Create your views here.
def uploadImg(request):
    if request.method == 'POST':
        new_img = IMG(
            img=request.FILES.get('img')
        )

        new_img.save()
    return render(request, 'web/index.html')
    
   
def showImg(request):
    imgs = IMG.objects.all()
    content = {
        'imgs':imgs,
    }
    return render(request, 'web/showImg.html', content)
    
def index(request):
    if request.method == 'POST':
        new_img = IMG(
            img=request.FILES.get('img')
        )
        
        new_img.save()
        return render(request, 'web/index.html')
    # imgs = IMG.objects.all()
    # content = {
    #     'imgs':imgs,
    # }
    sys.path.append("..")
    sample = list(glob.glob(sample_path))
    for i in range(len(sample)):
        sample[i] = '/'+sample[i]
    print(sample)
    content = {
        'imgs_dir':json.dumps(sample),
    }
    return render(request, 'web/index.html', content)
    
