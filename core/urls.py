from django.urls import path, include
from .views import viewNote, deleteNote, completeNote,uncompleteNote,updateTask

urlpatterns = [
    path('',viewNote),
    path('complete',completeNote),
    path('delete',deleteNote),
    path('uncomplete',uncompleteNote),
    path('updateTask',updateTask),
]
