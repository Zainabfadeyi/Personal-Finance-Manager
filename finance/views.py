from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .serializers import ExpenseCategorySerializer, ExpenseSerializer, SavingSerializer, BudgetSerializer, AccountSerializer, TransactionSerializer, GoalSerializer, NotificationSerializer
from .models import ExpenseCategory, Expense, Saving, Budget, Account, Transaction, Goal, Notification


class CustomViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    http_method_names = ('get', 'post', 'put', 'patch', 'delete')

class ExpenseCategoryViewSet(CustomViewSet):
    serializer_class = ExpenseCategorySerializer

    def get_queryset(self):
        user_expenses = Expense.objects.filter(user=self.request.user)
        category_ids = user_expenses.values_list('category', flat=True).distinct()
        return ExpenseCategory.objects.filter(id__in=category_ids)

class ExpenseViewSet(CustomViewSet):
    serializer_class = ExpenseSerializer

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)

class SavingViewSet(CustomViewSet):
    serializer_class = SavingSerializer
    
    def get_queryset(self):
        return Saving.objects.filter(user=self.request.user)

class BudgetViewSet(CustomViewSet):
    serializer_class = BudgetSerializer
    
    def get_queryset(self):
        return Budget.objects.filter(user=self.request.user)

class AccountViewSet(CustomViewSet):
    serializer_class = AccountSerializer
    
    def get_queryset(self):
        return Account.objects.filter(user=self.request.user)

class TransactionViewSet(CustomViewSet):
    serializer_class = TransactionSerializer
    
    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

class GoalViewSet(CustomViewSet):
    serializer_class = GoalSerializer
    
    def get_queryset(self):
        return Goal.objects.filter(user=self.request.user)

class NotificationViewSet(CustomViewSet):
    serializer_class = NotificationSerializer
    
    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)
