from django.shortcuts import render
from pytrends.request import TrendReq
from django.http import JsonResponse
import urllib.parse
import myapp.task
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
    myapp.task.fetch_and_update_data2()
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
    myapp.task.fetch_and_update_ggTrendsRealtimeData()
    return render(request, 'myapp/youtube.html')

def facebook(request):
    return render(request, 'myapp/facebook.html')

def twitter(request):
    return render(request, 'myapp/twitter.html')
#realtime
def display_trending(request):
    # pytrends = TrendReq(hl='en-US', tz=360)
    pytrends = TrendReq()
    trending_data = pytrends.realtime_trending_searches(pn='VN')
    trending_data = trending_data.head(30)
    keyword_list = trending_data.to_records(index=False).tolist()
    # Loại bỏ dấu ngoặc đơn và dấu phẩy từ mỗi chuỗi trong danh sách
    cleaned_list = [item[0].replace("'", "").replace(",", "") for item in keyword_list]
    print(cleaned_list)

    return render(request, 'myapp/google-trend-realtime.html', {'trending_list': cleaned_list})
#realtime
def update_realtime_trending_data(request):
    pn = request.GET.get('pn', 'vn')  # Lấy giá trị của pn từ yêu cầu GET, mặc định là 'vietnam'
    pytrends = TrendReq(hl='en-US', tz=360)
    trending_data = pytrends.realtime_trending_searches(pn=pn)
    trending_data = trending_data.head(30)
    keyword_list = [item[0] for item in trending_data.to_records(index=False)]
    return JsonResponse(keyword_list, safe=False)


def update_daily_trending_data1(request):
    pn = request.GET.get('pn', 'VN')  # Lấy giá trị của pn từ yêu cầu GET, mặc định là 'vietnam'
    pytrends = TrendReq(hl='en-US', tz=360)
    today_searches_df = pytrends.today_searches(pn=pn)
    processed_data = []
    for entry in today_searches_df:
        decoded_keyword = urllib.parse.unquote(entry.split('=')[1].split('&')[0], encoding='utf-8')
        decoded_keyword = decoded_keyword.replace('+', ' ')
        processed_data.append(decoded_keyword)
    print(processed_data)
    return JsonResponse(processed_data, safe=False)

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