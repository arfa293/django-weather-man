from django.http import HttpResponse
from django.shortcuts import render
from .classes import Fileparser,Calculation
import os

def index(request):
    year = 2012
    month = 6
    fp = Fileparser()
    files = fp.get_files_by_year(year)
    total_data = []
    required_columns = ["PKT" or "PKST","Max TemperatureC", "Min TemperatureC", "Max Humidity",  "Min Humidity", "Mean Humidity"]
    for file in files:
        data = fp.get_file_data(to_read=file, required_columns=required_columns)
        total_data = total_data + data
    # print(total_data)
    print(fp.formatdata(extracted_data=total_data))
    fz=Calculation(total_data)
    fg=fz.get_min_temperature()
    fx=fz.get_max_temperature()
    print(fg)
    print(fx)
    fr=fz.get_max_huimidity()
    print(fr)
    fn = fz.get_min_huimidity()
    print(fn)
    gh=fz.average_max_temperature(year,month)
    print(f"average monthly max temp: {gh} C")
    gf=fz.average_min_temp(year,month)
    print(f"average monthly min temp: {gf} C")
    gd=fz.average_mean_humidity(year,month)
    print(f"average monthly mean humidity: {gd} %")    


    return HttpResponse()

def yearly_report(request):
    return render (request,'weatherreport.html')