from django.db import models
from django.core.validators import MinLengthValidator


class Author(models.Model):
    name = models.CharField(
        max_length=100,
        help_text='Enter your name',
        validators=[MinLengthValidator(2, "Author name must be greater than 1 character")]
    )

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Blog(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.CharField(max_length=100)
    trailer = models.CharField(max_length=300, null=True)
    time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, null=False)

    # Shows up in the admin list
    def __str__(self):
        return self.title
