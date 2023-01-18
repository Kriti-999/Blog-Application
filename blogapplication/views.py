
from django.http import HttpResponse
from django.template import loader
from .models import Post

# def index(request):
#   template = loader.get_template('ndex.html')
#   return HttpResponse(template.render())
def getPostData(request):
  query=Post.objects.all().values()
  context={
        'data':query,
    }
  template=loader.get_template('index_blog.html')
  return HttpResponse(template.render(context, request))

def postFullDetail(request,slug):
  query=Post.objects.get(slug=slug)
  context={
        'data':query,
    }
  template=loader.get_template('post_detail.html')
  return HttpResponse(template.render(context, request))
  
