from account.models import User
from django.db import models


class OrganizationMember(models.Model):
    member_id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        default=None,
        related_name="organization_member",
    )
    role = models.CharField()

    def __str__(self):  # type: ignore
        return (
            f"OrganizationMember("
            f"{self.member_id}, role: {self.role}, userId: {self.user.user_id})"
        )
