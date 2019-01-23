from django.urls import include, path
from . import views
urlpatterns = [
    path('', views.HomeView.as_view(), name='HomeView'),
    path('ajax/timing/', views.GetTiming.as_view(), name='AjaxTiming'),
    path('contactus',views.ContactUS.as_view(), name='contactview'),
    path('Men',views.MenList.as_view(),name='MenView'),
    path('Women',views.WomenList.as_view(),name='WomenView'),
    path('booking/<int:id>',views.Booking.as_view(),name='bookingsview'),
    path('booking/<int:id>/<int:day>/<int:month>/<int:year>',views.TimeList.as_view(), name='TimeView'),
    path('booking/<int:id>/<int:day>/<int:month>/<int:year>/<int:timeid>',
         views.Bookingdetails.as_view(),name= 'BookingDetailView')

]