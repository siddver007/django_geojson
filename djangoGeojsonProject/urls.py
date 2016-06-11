from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [

	# Include djangoGeojson App URLs in the project
    url(r'^', include('djangoGeojson.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
