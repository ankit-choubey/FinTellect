from rest_framework import generics
from .models import Transaction
from .serializers import TransactionSerializer
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse

from django.db.models import Sum
from django.shortcuts import render
import json

def frontend_home(request):
    return render(request, "index.html")

def dashboard(request):
    return render(request, "finance/dashboard.html")

def analytics(request):
    transactions = Transaction.objects.all()

def transactions(request):
    return render(request, 'finance/transactions.html')

def analytics(request):
    return render(request, 'finance/analytics.html')

    # Transaction Trends Data
    transaction_data = {
        "dates": [t.date.strftime("%Y-%m-%d") for t in transactions],
        "amounts": [t.amount for t in transactions]
    }

    # Spending by Category Data
    category_summary = {}
    for t in transactions:
        category_summary[t.category] = category_summary.get(t.category, 0) + t.amount

    category_data = {
        "labels": list(category_summary.keys()),
        "values": list(category_summary.values())
    }

    # Monthly Expense Data
    monthly_summary = {}
    for t in transactions:
        month = t.date.strftime("%b %Y")
        monthly_summary[month] = monthly_summary.get(month, 0) + t.amount

    monthly_data = {
        "months": list(monthly_summary.keys()),
        "values": list(monthly_summary.values())
    }

    context = {
        "transaction_data": json.dumps(transaction_data),
        "category_data": json.dumps(category_data),
        "monthly_data": json.dumps(monthly_data)
    }

    return render(request, "finance/analytics.html", context)



# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import pandas as pd
# import json

#CSV Reading
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
from .models import Transaction
from django.contrib.auth.models import User

@csrf_exempt
def upload_transaction_file(request):
    if request.method != "POST":
        return JsonResponse({"error": "Request must be POST"}, status=400)

    if "file" not in request.FILES:
        return JsonResponse({"error": "No file uploaded"}, status=400)

    uploaded_file = request.FILES["file"]

    # Check file type
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith(".json"):
        df = pd.read_json(uploaded_file)
    else:
        return JsonResponse({"error": "Unsupported file format"}, status=400)

    user = User.objects.first()  # Temporary fix (replace with real user authentication)
    
    transactions = []
    for _, row in df.iterrows():
        transaction = Transaction.objects.create(
            user=user,
            amount=row.get("amount", 0),
            category=row.get("category", "Uncategorized"),
            description=row.get("description", ""),
            source="UPI File"
        )
        transactions.append({
            "amount": transaction.amount,
            "category": transaction.category,
            "description": transaction.description,
            "source": transaction.source
        })

    return JsonResponse({"message": "Transactions saved", "transactions": transactions})

#AI Categorization
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
from .models import Transaction
from django.contrib.auth.models import User
import joblib

# 🔹 Load AI Model & Vectorizer (Ensure model is trained & saved)
try:
    model = joblib.load("ai/spending_model.pkl")  # AI model for classification
    vectorizer = joblib.load("ai/vectorizer.pkl")  # Converts text descriptions to numerical format
except:
    model = None
    vectorizer = None

def categorize_transaction(description):
    """
    Uses AI model to categorize transactions based on description.
    If AI model fails, returns 'Uncategorized'.
    """
    if not model or not vectorizer:  # If model is missing, return default category
        return "Uncategorized"

    X_test = vectorizer.transform([description])  # Convert text into numerical data
    predicted_category = model.predict(X_test)  # Predict the category
    return predicted_category[0]  # Return the predicted category

@csrf_exempt
def upload_transaction_file(request):
    if request.method != "POST":
        return JsonResponse({"error": "Request must be POST"}, status=400)

    if "file" not in request.FILES:
        return JsonResponse({"error": "No file uploaded"}, status=400)

    uploaded_file = request.FILES["file"]
    
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith(".json"):
        df = pd.read_json(uploaded_file)
    else:
        return JsonResponse({"error": "Unsupported file format"}, status=400)

    user = User.objects.first()  # Temporary user
    transactions = []
    
    for _, row in df.iterrows():
        description = row.get("description", "")
        predicted_category = categorize_transaction(description)  # 🔥 AI Prediction

        transaction = Transaction.objects.create(
            user=user,
            amount=row.get("amount", 0),
            category=predicted_category,  # ✅ AI-generated category
            description=description,
            source="UPI File"
        )

        transactions.append({
            "amount": transaction.amount,
            "category": transaction.category,  # ✅ Now categorized by AI
            "description": transaction.description,
            "source": transaction.source
        })

    return JsonResponse({"message": "Transactions saved & categorized", "transactions": transactions})


def finance_home(request):
    return HttpResponse("Finance App Working Successfully!") 

class TransactionListCreateView(generics.ListCreateAPIView):
    """
    API to fetch all transactions or create a new one.
    """
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TransactionDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API to get, update, or delete a single transaction.
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

#transaction fetch
def transactions_view(request):
    transactions = Transaction.objects.all()

    if request.method == "POST" and request.FILES.get("csv_file"):
        csv_file = request.FILES["csv_file"]
        df = pd.read_csv(csv_file)

        # Assuming your CSV has 'date', 'category', 'amount', 'type'
        for _, row in df.iterrows():
            Transaction.objects.create(
                date=row["date"],
                category=row["category"],
                amount=row["amount"],
                type=row["type"]
            )

    return render(request, "finance/transactions.html", {"transactions": transactions})