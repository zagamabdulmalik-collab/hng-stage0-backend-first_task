from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from datetime import datetime, timezone
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

@api_view(['GET'])
def get_profile(request):
    try:
        # Fetch a random cat fact
        res = requests.get("https://catfact.ninja/fact", timeout=5)
        res.raise_for_status()
        fact_data = res.json()
        cat_fact = fact_data.get("fact", "No cat fact available right now.")
    except Exception as e:
        cat_fact = f"Could not fetch cat fact: {str(e)}"

    data = {
        "status": "success",
        "user": {
            "email": os.getenv("USER_EMAIL"),
            "name": os.getenv("USER_NAME"),
            "stack": os.getenv("USER_STACK")
        },
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "fact": cat_fact
    }

    return Response(data)
