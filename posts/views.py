from django.shortcuts import render
from django.http import JsonResponse

def post_list(request):
    
    posts = [{'id': 1, 'title': 'First Post'}]
    return JsonResponse(posts, safe=False)

def create_post(request):
    return JsonResponse({'message': 'Post Created'})

def delete_post(request):
    return JsonResponse({'success': 'false', 'message': 'Unauthorised to perform this action'})