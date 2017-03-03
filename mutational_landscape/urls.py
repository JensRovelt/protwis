from django.conf.urls import url
from django.views.decorators.cache import cache_page

from mutational_landscape import views

urlpatterns = [
    url(r'^$', cache_page(60*60*24*0)(views.TargetSelection.as_view()), name='targetselection'),
    url(r'^render', views.render_variants, name='render'),
    url(r'^(?P<download>download)', views.render_variants, name='render'),
    url(r'^statistics', views.statistics, name='statistics'),
    url(r'^ajax/NaturalMutation/(?P<slug>[-\w]+)/$', views.ajaxNaturalMutation, name='ajaxNaturalMutation'),
    url(r'^ajax/CancerMutation/(?P<slug>[-\w]+)/$', views.ajaxCancerMutation, name='ajaxCancerMutation'),
    url(r'^ajax/DiseaseMutation/(?P<slug>[-\w]+)/$', views.ajaxDiseaseMutation, name='ajaxDiseaseMutation'),
    url(r'^ajax/mutant_extract', views.mutant_extract, name='mutant_extract')
]
