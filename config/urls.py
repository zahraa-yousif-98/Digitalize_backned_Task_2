from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from files_management.controller import posts_controller
api = NinjaAPI()
api.add_router('/posts', posts_controller)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),

]
