from django.conf.urls import include, url
from django.contrib import admin

import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'jvis.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^jvis/', views.gui, name='jvis'),
    url(r'^detail/', views.detail, name='detail')
]
