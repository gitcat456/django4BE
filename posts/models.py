from django.db import models

class Author(models.Model):
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.author

class Post(models.Model): 
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
