from django.db import models
from tv_show.models import Movies

class TodoModel(models.Model):
    CHECK = (
        ("✅", "✅"),
        ("❌", "❌")
    )
    task = models.TextField()
    checked = models.CharField(choices=CHECK, max_length=10)
    choice_movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.task}-{self.checked}'
