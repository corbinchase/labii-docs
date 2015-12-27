from django.conf.urls import patterns, url, include
from common.views import url2template

urlpatterns = patterns('docs.views',
	url(r'^home/$', 'docs_home', name='docs_home'),
	
	url(r'^page/(?P<filename>.+)/$', 'docs_page', name='docs_page'),

	url(r'^view/(?P<filename>.+)/$', 'docs_view', name='docs_view'),
	url(r'^modalview/(?P<filename>.+)/$', 'docs_modalview', name='docs_modalview'),
)