from django.db import models


class Item(models.Model):
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(blank=True, upload_to="image")  # /media/image/
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]  # 기본 정렬 방식(작성일시 내림차순)

    def __str__(self) -> str:
        return self.title