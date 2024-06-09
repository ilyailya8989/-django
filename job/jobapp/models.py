from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.id}. {self.name}'

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(null=True,
                               blank=True)

    description = models.CharField(max_length=255,
                                   null=True,
                                   blank=True)

    published_date = models.DateField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    categoryInPost = models.ForeignKey(Category,
                                       related_name='category',
                                       on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}. {self.title}'


class Coment(models.Model):
    name = models.CharField(max_length=255)
    coment = models.TextField(max_length=255)
    data = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey(Post,
                             related_name='post',
                             on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}. {self.name}'
