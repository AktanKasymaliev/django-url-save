from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Link(models.Model):
    """ Website's link model """

    url = models.TextField(verbose_name="Website URL links")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    links_title = models.CharField(verbose_name="Links name", max_length=255)

    def __str__(self) -> str:
        return f"{self.user.username} - {self.links_title}"

    class Meta:
        db_table = "links_db"
        verbose_name = "Link"
        verbose_name_plural = "Links"