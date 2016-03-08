"""django_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from CryptoChat import views

# routers convert view sets to usable API endpoints
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)                    # view/edit users at http://159.203.252.197/users/
router.register(r'conversations', views.ConversationViewSet)    # view/edit conversations at http://159.203.252.197/conversations/
router.register(r'messages', views.MessageViewSet)              # view/edit messages at http://159.203.252.197/messages
router.register(r'publickeys', views.PublicKeyViewSet)          # view/edit public keys at http://159.203.252.197/publickeys

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),                            # make the router patterns above usable
]
