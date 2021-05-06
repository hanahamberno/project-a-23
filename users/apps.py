from django.apps import AppConfig
#This code is modified from code that's part of this tutorial: https://www.youtube.com/watch?v=FdVuKt_iuSI&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=11&t=1143s

class UsersConfig(AppConfig):
    name = 'users'

    # (Hanah) import singals from signals.py
    def ready(self):
        import users.signals
