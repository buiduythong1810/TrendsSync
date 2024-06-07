from django.shortcuts import render
from pytrends.request import TrendReq
from django.http import JsonResponse
import urllib.parse
import myapp.tasks
from myapp.models import MyData, ggTrendsDailyData, Country, ggTrendsRealtimeData
from .forms import CountryForm

# Create your views here.
from django.http import HttpResponse 
import datetime 
import schedule
import time


    
 
def current_datetime(request): 
    now = datetime.datetime.now() 
    html = "<html><body>It is now %s.</body></html>" % now 
    return HttpResponse(html)

def home(request):
    myapp.tasks.print_current_time()
    return render(request, 'myapp/index.html') 

# def google_trend(request):
#     myapp.task.fetch_and_update_data()
#     all_objects = MyData.objects.all()
#     processed_data1 = []
#     for item in all_objects:
#         processed_data1.append(item.name)
#     print(processed_data1)
#     # Truyền dữ liệu sang template HTML
#     return render(request, 'myapp/google-trend.html', {'trending_list': processed_data1})
#     # return render(request, 'myapp/google-trend.html')

def youtube(request):
    myapp.tasks.fetch_and_update_ggTrendsRealtimeData()
    return render(request, 'myapp/youtube.html')

def facebook(request):
    return render(request, 'myapp/facebook.html')

def twitter(request):
    return render(request, 'myapp/twitter.html')


def google_trend_daily(request):
    countries = Country.objects.all()
    selected_country = request.GET.get('country', 'VN')  # Thiết lập giá trị mặc định là 'VN'
    
    # Truy vấn cơ sở dữ liệu để lấy tên của quốc gia dựa trên mã code
    try:
        selected_country1 = Country.objects.get(code=selected_country)
        selected_country_name = selected_country1.name
    except Country.DoesNotExist:
        # Xử lý trường hợp nếu không tìm thấy quốc gia
        selected_country_name = "Unknown"

    if selected_country:
        trending_data = ggTrendsDailyData.objects.filter(country=selected_country)  # Không sắp xếp theo bất kỳ trường nào
    else:
        trending_data = ggTrendsDailyData.objects.none()

    return render(request, 'myapp/google-trend-daily.html', {
        'countries': countries,
        'selected_country': selected_country,
        'selected_country_name': selected_country_name,
        'trending_list': trending_data
    })

def google_trend_realtime(request):
    countries = Country.objects.all()
    selected_country = request.GET.get('country', 'VN')  # Thiết lập giá trị mặc định là 'VN'
    
    # Truy vấn cơ sở dữ liệu để lấy tên của quốc gia dựa trên mã code
    try:
        selected_country1 = Country.objects.get(code=selected_country)
        selected_country_name = selected_country1.name
    except Country.DoesNotExist:
        # Xử lý trường hợp nếu không tìm thấy quốc gia
        selected_country_name = "Unknown"

    if selected_country:
        trending_data = ggTrendsRealtimeData.objects.filter(country=selected_country)  # Không sắp xếp theo bất kỳ trường nào
    else:
        trending_data = ggTrendsRealtimeData.objects.none()

    return render(request, 'myapp/google-trend-realtime.html', {
        'countries': countries,
        'selected_country': selected_country,
        'selected_country_name': selected_country_name,
        'trending_list': trending_data
    })


def get_country_data(request):
    selected_country = request.GET.get('country')
    # Xử lý dữ liệu của quốc gia ở đây
    # Ví dụ: lấy dữ liệu từ model và trả về dưới dạng JSON
    country_data = {
        'country': selected_country,
        'data': 'Dữ liệu của ' + selected_country
    }
    return JsonResponse(country_data)