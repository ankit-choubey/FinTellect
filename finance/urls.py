from django.urls import path
from .views import TransactionListCreateView, TransactionDetailView, upload_transaction_file
from . import views

urlpatterns = [
    path("", views.finance_home, name="finance_home"),  # Finance home page
    path('transactions/', TransactionListCreateView.as_view(), name='transaction-list'),
    path('transactions/<int:pk>/', TransactionDetailView.as_view(), name='transaction-detail'),
    path("upload/", upload_transaction_file, name="upload_transaction"),
]