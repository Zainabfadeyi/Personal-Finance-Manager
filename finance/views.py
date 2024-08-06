from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .serializers import ExpenseCategorySerializer, ExpenseSerializer, SavingSerializer, BudgetSerializer, AccountSerializer, TransactionSerializer, GoalSerializer, NotificationSerializer
from .models import ExpenseCategory, Expense, Saving, Budget, Account, Transaction, Goal, Notification
from rest_framework.response import Response


class CustomViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    http_method_names = ('get', 'post', 'put', 'patch', 'delete')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ExpenseCategoryViewSet(CustomViewSet):
    serializer_class = ExpenseCategorySerializer

    def get_queryset(self):
        return ExpenseCategory.objects.filter(user=self.request.user)

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


# class TransactionViewSet(CustomViewSet):
#     serializer_class = TransactionSerializer
    
#     def get_queryset(self):
#         return Transaction.objects.filter(user=self.request.user)


# 
class TransactionViewSet(CustomViewSet):
    
    def list(self, request):
        user_id = request.query_params.get('user_id')
        if user_id:
            transactions = Transaction.objects.filter(user_id=user_id)
        else:
            transactions = Transaction.objects.all()
        
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)

    def create(self, request):
        user_id = request.query_params.get('user_id')
        if not user_id:
            return Response({"error": "User ID is required."}, status=400)

        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            # Set the user before saving
            serializer.save(user_id=user_id)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class GoalViewSet(CustomViewSet):
    serializer_class = GoalSerializer
    
    def get_queryset(self):
        return Goal.objects.filter(user=self.request.user)

class NotificationViewSet(CustomViewSet):
    serializer_class = NotificationSerializer
    
    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)
