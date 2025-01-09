from django.urls import path
from django.contrib.auth.views import LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from . import views

#urlpatterns is a variable that is used for the urls.py in the Quiz_Game folder 
#basically for pathing and rendering different templates
urlpatterns = [
    path("", views.index, name="main"),
    path("report/", views.report, name="report"),
    path("report/<int:id>", views.report_details, name="report-details"), # Report details
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path('report-entry/',views.process_report_entry,name="process-report-entry"),
    path("water-levels/", views.water_level_data, name='water_level_data'), # GeoJSON data URL
    path("water-levels/<int:hzb>", views.prev_water_levels, name='prev_water_levels'), # Historic water Levels
    path("water-levels/watererror", views.prev_water_levels, name='water_level_error'), # Error page for missing data
    path("reports/", views.report_data, name='report_data'),
    path("password_reset/", PasswordResetView.as_view(), name="password_reset"),
    path("password_reset/done/", PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("reset/done/", PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]

