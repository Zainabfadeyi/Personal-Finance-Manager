from rest_framework import serializers
from .models import ExpenseCategory, Expense, Saving, Budget, Account, Transaction, Goal, Notification

class ExpenseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseCategory
        fields = ['id','name']

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        exclude=['user']
        read_only_fields=['user','created_at']

class SavingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saving
        exclude=['user']

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        exclude=['user']


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        exclude=['user']


# class TransactionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Transaction
        

class TransactionSerializer(serializers.ModelSerializer):
    transaction_type = serializers.ReadOnlyField()

    class Meta:
        model = Transaction
        fields = ['id','transaction_type', 'category', 'amount', 'description', 'transaction_date', 'created_at']

    def validate(self, attrs):
        # Ensure that the category is valid
        if attrs['category'] not in dict(Transaction.EXPENSE_CATEGORY_CHOICES) and attrs['category'] != "Income":
            raise serializers.ValidationError(f"Category must be one of the following: {', '.join([c[0] for c in Transaction.EXPENSE_CATEGORY_CHOICES])} or 'Income'")
        return attrs
    exclude=['user']


class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        exclude=['user']


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        exclude=['user']
