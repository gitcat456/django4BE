from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Post
from .jwt_utils import generate_jwt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import authenticate 

#jwt_login view
@api_view(["POST"])
@permission_classes([AllowAny])
def jwt_login_view(request):
    
    username = request.data.get('username')
    password = request.data.get('password')
    
    if not username or not password:
        return Response({
            "error": "username and password are required!"
        }, status=401)
        
    user = authenticate(username=username, password=password)
    
    if user is None:
        return Response({
            "error":"Invalid credentials!"
        }, status=401)
        
    token = generate_jwt(user)
    
    return Response({
        "user": user,
        "token": token
    })

@csrf_exempt   
def post_list(request):
    if request.method == 'GET':
        posts = list(Post.objects.values()) 
        return JsonResponse(posts, safe=False)

@csrf_exempt
def create_post(request): 
    if request.method == 'POST':
        data = json.loads(request.body)
        post = Post.objects.create(   # SQL: "INSERT INTO posts_post ..."
            title=data['title'],
            content=data['content'],
            is_published=data.get('is_published', False)
        )
        return JsonResponse({
            'id': post.id,    # ← This ID comes from SQLite auto-increment
            'title': post.title,
            'content': post.content,
            'created_at': post.created_at.isoformat()   # ← This timestamp from SQLite
        })


def delete_post(request):
    return JsonResponse({'success': 'false', 'message': 'Unauthorised to perform this action'})