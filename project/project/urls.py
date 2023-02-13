
from django.contrib import admin
from django.urls import include,path
from rest_framework import routers
from members import views

router = routers.SimpleRouter()

router.register(r'members', views.MembersViewSet)
router.register(r'accounts', views.AccountsViewSet)
router.register(r'cards', views.CardsViewSet)



urlpatterns = [
  
    path('admin/', admin.site.urls),
    path('' ,include(router.urls)),
    path('', include('members.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

 
   
]
