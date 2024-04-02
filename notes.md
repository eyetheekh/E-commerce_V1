#Configure templates, static dirs

#start app core

#base,index,navbar,footer .html files

#Configure static url, media url in project urls.py

    from django.conf import settings
    from django.conf.urls.static import static

    if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

#start app userauth
    
    #customUser
        from django.contrib.auth.models import AbstractUser
        class customUser(AbstractUser):
    AUTH_USER_MODEL in settings

    #registration and login
        templates- login, register .html
        forms.py - registerform


