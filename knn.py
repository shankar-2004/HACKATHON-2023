from django.shortcuts import render
from .knn import knn

def predict_crop(request):
    if request.method == 'POST':
        temperature = int(request.POST['temperature'])
        humidity = int(request.POST['humidity'])
        ph = int(request.POST['ph'])
        rainfall = int(request.POST['rainfall'])
        prediction = knn.predict([[temperature, humidity, ph, rainfall]])
        return render(request, 'result.html', {'prediction': prediction[0]})
    return render(request, 'form.html')
