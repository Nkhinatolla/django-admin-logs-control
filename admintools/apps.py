from django.apps import AppConfig
print("app bar eken")

class AdmintoolsConfig(AppConfig):
    name = 'admintools'

    def ready(self):
        import admintools.signals
