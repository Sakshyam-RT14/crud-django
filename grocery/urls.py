from django.urls import path
from . import views

app_name = "grocery"

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add_item, name="add_item"),
    path("toggle/<int:item_id>/", views.toggle_completed, name="toggle_completed"),
    path("delete/<int:item_id>/", views.delete_item, name="delete_item"),
    path("edit/<int:item_id>/", views.edit_item, name="edit_item"),
    path("update/<int:item_id>/", views.update_item, name="update_item"),
]