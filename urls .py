from django.urls import include, path

urlpatterns = [
    path('predict/', include('appname.urls')),
]
