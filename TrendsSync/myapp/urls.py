from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("time/", views.current_datetime, name="get_time"),
    path('google-trend/', views.google_trend_daily, name='google_trend'),
    path('youtube/', views.youtube, name='youtube'),
    path('facebook/', views.facebook, name='facebook'),
    path('twitter/', views.twitter, name='twitter'),
    path("google-trend/realtime", views.google_trend_realtime, name="display_realtime_trending"),
    path('update_realtime_trending_data/', views.update_realtime_trending_data, name='update_realtime_trending_data'),
    path("google-trend/daily", views.google_trend_daily, name="display_daily_trending"),
    path('get-country-data/', views.get_country_data, name='get_country_data'),
    
    
]