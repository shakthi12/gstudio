from django.conf.urls import patterns, url

urlpatterns = patterns('gnowsys_ndf.ndf.views.bioapp',
                       url(r'^$', 'bioapp', name='bioapp'),
                       
                       # url(r'^(?P<node_id>[\w-]+)/version/(?P<version_no>\d+\.\d+)$', 'version_node', name='node_version'),
)
