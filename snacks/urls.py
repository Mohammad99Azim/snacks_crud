from django.urls import path

from .views import SnacksListView, SnacksDetailView, SnacksCreateView, SnacksUpdateView, SnacksDeleteView

urlpatterns = [
    path('', SnacksListView.as_view(), name='snacks_list'),
    path('<int:pk>/', SnacksDetailView.as_view(), name='snack_detail'),
    path('create/', SnacksCreateView.as_view(), name='create_snack'),
    path('update/<int:pk>/', SnacksUpdateView.as_view(), name='update_snack'),
    path('delete/<int:pk>/', SnacksDeleteView.as_view(), name='delete_snack')
]
