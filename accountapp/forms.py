from django.contrib.auth.forms import UserCreationForm

class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):  # 클래스 생성자. AccountUpdateForm(폼도 클래스) 생성 시, 들어오는 정보들(유저 정보같은거)
        super().__init__(*args, **kwargs)

        self.fields['username'].disabled = True