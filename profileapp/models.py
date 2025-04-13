from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # 연결되어있는 User객체가 지워질 때 같이 지워지도록(CASCADE)
    # request.user.profile 처럼 바로 접근할 수 있도록 연결이름을 정해주는 것 related_name='profile'
        # request.user.profile.nickname처럼 profile의 더 내부의 필드도 접근 가능
    image = models.ImageField(upload_to="profile/", null=True)
    # upload_to로 이미지 저장 경로 지정 -> media/profile/
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)

