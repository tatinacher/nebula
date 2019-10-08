from django.shortcuts import render
from django.utils import timezone
from .models import Post
from rest_framework import viewsets
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)



# def post_list(request):
#     #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#     posts = Post.objects.all()
#     return render(request, 'blog/post_list.html', {'posts': posts})
