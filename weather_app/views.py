
from django.http import HttpResponse
from django.shortcuts import render
from .classes import Fileparser,Calculation
import os

def index(request):
    year = int(request.GET.get("year", 2024)) 
    month = int(request.GET.get("month", 1))  

    parser = Fileparser()
    files = parser.get_files_by_year(year)
    
    all_data = []
    required_columns = ["PKT", "PKST", "Max TemperatureC", "Min TemperatureC", "Max Humidity", "Min Humidity", "Mean Humidity"]
    
    for file in files:
        all_data.extend(parser.get_file_data(file, required_columns))

    calc = Calculation(all_data)
    
    avg_max_temp = calc.average_max_temperature(year, month)
    avg_min_temp = calc.average_min_temp(year, month)

    
    highest_temp = calc.get_max_temperature()  
    lowest_temp = calc.get_min_temperature()  
    most_humid_day = calc.get_max_huimidity()  

    
    avg_max_temp = int(avg_max_temp) if isinstance(avg_max_temp, (int, float)) else 0
    avg_min_temp = int(avg_min_temp) if isinstance(avg_min_temp, (int, float)) else 0

    
    max_temp_stars = "*" * avg_max_temp
    min_temp_stars = "*" * avg_min_temp

    context = {
        "year": year,
        "month": month,
        "avg_max_temp": avg_max_temp,
        "avg_min_temp": avg_min_temp,
        "max_temp_stars": max_temp_stars,
        "min_temp_stars": min_temp_stars,
        "highest_temp": highest_temp,
        "lowest_temp": lowest_temp,
        "most_humid_day": most_humid_day,
    }

    return render(request, "weather_report.html", context)
