import jwt
from datetime import datetime, timedelta, timezone
from django.conf import settings 
from rest_framework import exceptions

def generate_jwt(user):
    
    payload = {
        "user_id": user.id,
        "username": user.username,
        "exp": datetime.now(timezone.utc) + timedelta(minutes=15)
    }
    
    access = jwt.encode(payload, settings.SECRET_KEY, algorithhm="HS256")
    
    return access

def verify_jwt(token):
    
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithm="HS256")
        return payload
    except jwt.ExpiredSignatureError:
        raise exceptions.AuthenticationFailed("Expired Token!!")
    except jwt.InvalidTokenError:
        raise exceptions.AuthenticationFailed("Invalid Token!")
    
    
    
    
    