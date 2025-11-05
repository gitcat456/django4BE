from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Post

@csrf_exempt
def post_list(request):
    if request.method == 'GET':
        posts = list(Post.objects.values())
        return JsonResponse(posts, safe=False)

@csrf_exempt
def create_post(request): 
    if request.method == 'POST':
        data = json.loads(request.body)
        post = Post.objects.create(
            title=data['title'],
            content=data['content'],
            is_published=data.get('is_published', False)
        )
        return JsonResponse({
            'id': post.id,
            'title': post.title,
            'content': post.content,
            'created_at': post.created_at.isoformat()
        })


def delete_post(request):
    return JsonResponse({'success': 'false', 'message': 'Unauthorised to perform this action'})