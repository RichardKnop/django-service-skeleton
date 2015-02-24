from apps.user.models import User


class UserService(object):

    def __init__(self):
        self._model = User

    def register(self, email, password):
        user = self._model(
            email=email,
            password=password,
        )

        user.full_clean()
        user.save()

        return user