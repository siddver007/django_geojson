from django.conf.urls import include, url
from django.views.decorators.csrf import csrf_exempt
from djangoGeojson.views import *

urlpatterns = [
	
	# URLs to create, retrieve, update, and delete Providers
    url(r'^provider/create/$', csrf_exempt(createProviderView.as_view())),
    url(r'^provider/get/$', getProviderView.as_view()),
    url(r'^provider/update/$', csrf_exempt(updateProviderView.as_view())),
    url(r'^provider/delete/$', csrf_exempt(deleteProviderView.as_view())),
    # URLs to create, retrieve, update, and delete Regions/ Polygons
    url(r'^region/add/$', csrf_exempt(createPolygonView.as_view())),
    url(r'^region/get/$', getPolygonView.as_view()),
    url(r'^region/update/$', csrf_exempt(updatePolygonView.as_view())),
    url(r'^region/delete/$', csrf_exempt(deletePolygonView.as_view())),
  
]