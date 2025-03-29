from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import hello_world, AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView

app_name = "accountapp"

"127.0.0.1:8000/account/hello_world/"
"-> accountapp:hello_world"  #hello_world는 뷰 명을 적는게 아니라, urlpatterns에서 지정해 둔 name임.

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),

    # login과 logout은 views.py에서 상속받을 필요도 없이 바로 여기서 연결하면 됨.
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'), # 로그인은 템플릿 지정해줘야함
    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', AccountCreateView.as_view(), name='create'),
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),
]