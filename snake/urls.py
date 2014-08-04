from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'snake_game.views.home', name='home'),
    url(r'^dome/$', 'snake_game.views.dome', name='dome'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^register/$', 'snake_game.views.register', name='register'),
    url(r'^leaderboard/$', 'snake_game.views.leaderboard', name='leaderboard'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    # url(r'^profile/(?P<username>\w+)/$', 'snake_game.views.view_profile', name='view_profile'),
    url(r'^profile/$', 'snake_game.views.profile', name = 'profile'),
    url(r'^update_score/$', 'snake_game.views.update_score', name = 'update_score'),




    url(r'^admin/', include(admin.site.urls)),
)
