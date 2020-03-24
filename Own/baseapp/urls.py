from django.urls import path
from baseapp import views
from django.views.generic import TemplateView


app_name = "pictures"

urlpatterns=[
        path("",views.PostListView.as_view(),name='post_list'),
        path('post/new',views.CreatePostView.as_view(),name='post_new'),
        path("post/<int:pk>",views.PostDetailView.as_view(),name="post_detail"),
        path("profile_pic/profile/",views.NewProfListView.as_view(),name='profile_pic_list'),
        path('post/<int:pk>/edit/',views.UpdatePostView.as_view(),name='post_edit'),
        path('post/<int:pk>/remove/',views.DeletePostView.as_view(),name='post_remove'),
        path("upload/",views.Pictures_View,name="uploads"),
        path("contact/",views.ContactView,name='contact_us'),
        path("priests/",views.NewProfile,name='profile'),
        path('notices/',views.SaveNotices,name='notice_form'),
        path('notices/list',views.NoticesListView.as_view(),name="notices_list"),
        path('notices/<int:pk>/',views.delete_file,name="delete_file"),
        path('timings',views.timing.as_view(),name="timing"),
        path('history/',views.History.as_view(),name='history'),
        path('profile_p/<int:pk>/',views.delete_profile_p,name="delete_profile_p"),
        path('edit/<int:pk>/',views.UpdateProfile,name="profile_p_edit"),
        path("parish_council/",views.ParishCouncil.as_view(),name='parish_council'),
        path("church_staff/",views.ChurchStaff.as_view(),name="church_staff"),
        path("office_timings/",views.OfficeTimings.as_view(),name="office_timings"),
        path("zone/",views.Zone.as_view(),name="zone"),
        path("confession/",views.Confessions.as_view(),name="confession"),
        path("lectors/list",views.LectorsListView.as_view(),name="lectors_list"),
        path("lectors",views.SaveLectors,name="lectors_form"),
        path('lectors/<int:pk>/',views.delete_lectors,name='delete_lectors'),
    ]
