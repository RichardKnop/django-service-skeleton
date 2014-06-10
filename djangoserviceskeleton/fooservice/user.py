from .models import User


class UserService():
    def register(self, email, password):
        user = User(
            email=email,
            password=password,
        )

        user.full_clean()
        user.save()

        return user