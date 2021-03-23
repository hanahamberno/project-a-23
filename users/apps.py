from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    # (Hanah) import singals from signals.py
    def ready(self):
        import users.signals
