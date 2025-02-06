from django.urls import path

from accountapp.views import hello_world, AccountCreateView

app_name = "accountapp"

"127.0.0.1:8000/account/hello_world/"
"-> accountapp:hello_world"  #hello_world는 뷰 명을 적는게 아니라, urlpatterns에서 지정해 둔 name임.

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    path('create/', AccountCreateView.as_view(), name='create'),
]