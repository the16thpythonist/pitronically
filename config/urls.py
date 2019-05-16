# Python standard library imports
import os

# Django standard library imports
from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views

# Third party imports
from filebrowser.sites import site

# The filebrowser app needs to be a sub path of the admin url, and since the admin url is
# not static, we have to assemble this sub path here first using the admin url variable
FILEBROWSER_URL = os.path.join(settings.ADMIN_URL, 'filebrowser')


urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path(
        "about/", TemplateView.as_view(template_name="pages/about.html"), name="about"
    ),
    # Config for the filebrowser app, which is needed for the editor. This needs to be added before the base
    # admin url is defined.
    path(FILEBROWSER_URL, site.urls),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path("users/", include("pitronically.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    # Your stuff: custom urls includes go here
    path("blog/", include("pitronically.blog.urls", namespace="blog")),
    # TinyMCE Editor for blog posts
    #path("tinymce/", include("tinymce.urls")),
    path("ckeditor/", include("ckeditor_uploader.urls"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
