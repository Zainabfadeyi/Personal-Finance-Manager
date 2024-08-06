"""
URL configuration for financemanager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from users.views import RegisterationViewSet,LoginViewSet,RefreshViewset, UserDetailsView
from rest_framework.routers import DefaultRouter
from finance.views import ExpenseCategoryViewSet, ExpenseViewSet, SavingViewSet, BudgetViewSet, AccountViewSet, TransactionViewSet, GoalViewSet, NotificationViewSet

router=DefaultRouter()

router.register(r'auth/register', RegisterationViewSet,basename='auth-register')
router.register(r'auth/login',LoginViewSet,basename='auth-login')
router.register(r'auth/refresh',RefreshViewset,basename='auth-refresh')
router.register(r'expense-category',ExpenseCategoryViewSet,basename='expense-category')
router.register(r'expense',ExpenseViewSet,basename='expense')
router.register(r'saving',SavingViewSet,basename='saving')
router.register(r'budget',BudgetViewSet,basename='budget')
router.register(r'account',AccountViewSet,basename='account')
# router.register(r'transaction',TransactionViewSet,basename='transaction')

router.register(r'goal',GoalViewSet,basename='goal')
router.register(r'notification',NotificationViewSet,basename='notification')


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include((router.urls, 'api'))),
    path("api/user/details/", UserDetailsView.as_view({'get': 'list'}), name='user-details'),
    path("api/transactions", TransactionViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-transactions'),
    path("api/accounts", AccountViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-accounts'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)