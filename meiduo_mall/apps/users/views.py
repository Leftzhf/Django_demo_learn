
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


class UsernameCountView(View):

    def get(self,request,username):
        """
        验证用户名是否重复
        Args:
            request: 请求对象
            username: 用户名

        Returns:
        没有重复返回0，有重复返回1.
        """
        from apps.users.models import User
        count=User.objects.filter(username=username).count()
        return JsonResponse({'code':0,'count':count,'errmsg':'ok'})