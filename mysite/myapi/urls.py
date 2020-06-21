from django.urls import include, path
from rest_framework import routers
from . import views
from django.conf.urls import url

router = routers.DefaultRouter()
# Wire up our API using automatic URL routing.
# Additionally, we include the application URLs for the browsable API.
urlpatterns = [
    path('',include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('workflows/$', views.WorkFlowListView.as_view()),
    url('workflows/(?P<pk>\d+)/$', views.WorkFlowView.as_view()),
    url('steps/$', views.StepListView.as_view()),
    url('steps/(?P<pk>\d+)/$', views.StepView.as_view()),
    url('commentaries/$', views.CommentListView.as_view()),
    url('commentaries/(?P<pk>\d+)/$', views.CommentView.as_view()),
    

]
