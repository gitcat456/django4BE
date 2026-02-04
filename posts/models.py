from django.db import models

class Author(models.Model):
    author_name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.author_name

class Post(models.Model): 
    title = models.CharField(max_length=200)
    content = models.TextField()
    author_name = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="posts")
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
