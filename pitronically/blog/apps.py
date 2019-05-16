from django.apps import AppConfig


class BlogAppConfig(AppConfig):

    name = "pitronically.blog"
    verbose_name = "Blog"

    def ready(self):
        pass
