from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


User = get_user_model()

class ExpenseCategory(models.Model):
    name = models.CharField(max_length=50, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2, null=False)
    description = models.TextField()
    date = models.DateField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.category.name} - {self.amount} on {self.date}"


class Saving(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2, null=False)
    description = models.TextField()
    date = models.DateField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.amount} saved on {self.date}"

class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2, null=False)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.category.name} Budget: {self.amount} from {self.start_date} to {self.end_date}"

class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False)
    account_type = models.CharField(max_length=50, null=False)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.name} ({self.account_type})"

# class Transaction(models.Model):
#     TRANSACTION_TYPE_CHOICES = [
#         ("Income", "Income"),
#         ("Expense", "Expense"),
#     ]

#     CATEGORY_CHOICES = [
#         ("Income", "Income"),
#         ("Groceries", "Groceries"),
#         ("Utilities", "Utilities"),
#         ("Entertainment", "Entertainment"),
#         ("Travel", "Travel"),
#         ("Miscellaneous", "Miscellaneous"),
#     ]

#     # ACTION_CHOICES = [
#     #     ("Edit", "Edit"),
#     #     ("Delete", "Delete"),
#     # ]

#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     # account = models.ForeignKey(Account, on_delete=models.CASCADE)
#     transaction_type = models.CharField(max_length=50, choices=TRANSACTION_TYPE_CHOICES, null=False)
#     category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, null=False)
#     # action = models.CharField(max_length=50, choices=ACTION_CHOICES, null=False)
#     amount = models.DecimalField(max_digits=12, decimal_places=2, null=False)
#     description = models.TextField()
#     transaction_date = models.DateField(null=False)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.user.username} - {self.transaction_type} of {self.amount} in {self.category} on {self.transaction_date}"


# class Transaction(models.Model):
#     TRANSACTION_TYPE_CHOICES = [
#         ("Income", "Income"),
#         ("Expenses", "Expenses"),
#     ]

#     EXPENSE_CATEGORY_CHOICES = [
#         ("Groceries", "Groceries"),
#         ("Utilities", "Utilities"),
#         ("Entertainment", "Entertainment"),
#         ("Travel", "Travel"),
#         ("Miscellaneous", "Miscellaneous"),
#     ]

#     # user = models.ForeignKey(User, on_delete=models.CASCADE)
#     # account = models.ForeignKey(Account, on_delete=models.CASCADE)
#     category = models.CharField(max_length=50, choices=EXPENSE_CATEGORY_CHOICES + [("Income", "Income")], null=False)
#     amount = models.DecimalField(max_digits=12, decimal_places=2, null=False)
#     description = models.TextField()
#     transaction_date = models.DateField(null=False)
#     created_at = models.DateTimeField(auto_now_add=True)

#     @property
#     def transaction_type(self):
#         if self.category == "Income":
#             return "Income"
#         else:
#             return "Expenses"

#     def __str__(self):
#         return f"{self.user.username} - {self.transaction_type} of {self.amount} in {self.category} on {self.transaction_date}"
    
class Transaction(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ("Income", "Income"),
        ("Expenses", "Expenses"),
    ]

    EXPENSE_CATEGORY_CHOICES = [
        ("Groceries", "Groceries"),
        ("Utilities", "Utilities"),
        ("Entertainment", "Entertainment"),
        ("Travel", "Travel"),
        ("Miscellaneous", "Miscellaneous"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Uncomment this line

    category = models.CharField(max_length=50, choices=EXPENSE_CATEGORY_CHOICES + [("Income", "Income")], null=False)

    amount = models.DecimalField(max_digits=12, decimal_places=2, null=False)
    description = models.TextField()
    transaction_date = models.DateField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE_CHOICES, null=False)  # Add this field

    def save(self, *args, **kwargs):
        # Set transaction_type based on category before saving
        self.transaction_type = "Income" if self.category == "Income" else "Expenses"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.transaction_type} of {self.amount} in {self.category} on {self.transaction_date}"

class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False)
    target_amount = models.DecimalField(max_digits=12, decimal_places=2, null=False)
    current_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    # due_date = models.DateField(null=False, default=datetime.date.today)

    def __str__(self):
        return f"{self.user.username} - Goal: {self.name} Target: {self.target_amount}"

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(null=False)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {'Read' if self.is_read else 'Unread'} Notification"