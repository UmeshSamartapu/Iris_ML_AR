from django.shortcuts import render
from .ml.predict import predict_iris
from .models import IrisPrediction

def home(request):
    result = None
    if request.method == "POST":
        sepal_length = float(request.POST.get("sepal_length"))
        sepal_width = float(request.POST.get("sepal_width"))
        petal_length = float(request.POST.get("petal_length"))
        petal_width = float(request.POST.get("petal_width"))

        features = [sepal_length, sepal_width, petal_length, petal_width]
        result = predict_iris(features)

        IrisPrediction.objects.create(
            sepal_length=sepal_length, sepal_width=sepal_width,
            petal_length=petal_length, petal_width=petal_width,
            prediction=result
        )

    history = IrisPrediction.objects.all().order_by('-created_at')
    return render(request, "index.html", {"result": result, "history": history})

def landing_page(request):
    return render(request, "landing.html")

def mobile_view(request):
    return render(request, "mobile_ar.html")

# def laptop_view(request):
#     return render(request, "laptop_ar.html")

def laptop_view(request):
    # Get the most recent prediction to show on the AR marker
    latest_prediction = IrisPrediction.objects.latest('created_at')
    return render(request, "laptop_ar.html", {"result": latest_prediction.prediction})