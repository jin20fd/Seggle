from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from notice import views

urlpatterns = [
    path('admin/announcements/', views.AdminNoticeList.as_view()),
    path('admin/announcements/<int:pk>/', views.AdminNoticeDetail.as_view()),
    path('admin/announcements/<int:pk>/check/', views.AdminNoticeCheckDetail.as_view()),
    path('announcements/', views.NoticeList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)