# trong một file tên là tasks.py hoặc bất kỳ tên nào bạn muốn
import schedule
import time
from pytrends.request import TrendReq
from myapp.models import MyData, ggTrendsDailyData, Country, ggTrendsRealtimeData
import urllib.parse
import datetime
from celery import shared_task

#Hàm updta dữ liệu trend hàng ngày ở Việt Nam
@shared_task
def fetch_and_update_data():
    pytrends = TrendReq()
    # Thực hiện lấy dữ liệu
    trending_data = pytrends.today_searches(pn='VN') # Thay 'VN' bằng mã quốc gia bạn muốn
    # Xóa dữ liệu cũ trong database
    processed_data = []
    for entry in trending_data:
        decoded_keyword = urllib.parse.unquote(entry.split('=')[1].split('&')[0], encoding='utf-8')
        decoded_keyword = decoded_keyword.replace('+', ' ')
        processed_data.append(decoded_keyword)
    # print(processed_data)
    MyData.objects.all().delete()
    now = datetime.datetime.now()
    now_str = now.strftime('%Y-%m-%d %H:%M:%S')
    processed_data.append(now_str)
    for item in processed_data:
        obj = MyData(name=item)
        obj.save()

    

def schedule_task():
    # Lên lịch thực hiện hàm fetch_and_update_data mỗi 30 phút
    schedule.every(1).minutes.do(fetch_and_update_data)
    while True:
        schedule.run_pending()
        time.sleep(1)


@shared_task
def fetch_and_update_data1():
    pytrends = TrendReq()
    countries = ['VN', 'US', 'JP', 'KR', 'FR', 'DE']  # Danh sách mã quốc gia
    
    all_processed_data = []

    for country in countries:
        trending_data = pytrends.today_searches(pn=country)
        processed_data = []

        for entry in trending_data:
            decoded_keyword = urllib.parse.unquote(entry.split('=')[1].split('&')[0], encoding='utf-8')
            decoded_keyword = decoded_keyword.replace('+', ' ')
            processed_data.append(decoded_keyword)

        now = datetime.datetime.now()
        now_str = now.strftime('%Y-%m-%d %H:%M:%S')
        processed_data.append(f"Timestamp: {now_str}")
        processed_data.append(f"Country: {country}")
        
        all_processed_data.extend(processed_data)

    # Xóa dữ liệu cũ trong database
    MyData.objects.all().delete()

    # Lưu dữ liệu mới vào database
    for item in all_processed_data:
        obj = MyData(name=item)
        obj.save()



@shared_task
def fetch_and_update_data2():
    pytrends = TrendReq()
    countries = [
        {'name': 'Vietnam', 'code': 'VN'},
        {'name': 'United States', 'code': 'US'},
        {'name': 'Japan', 'code': 'JP'},
        {'name': 'South Korea', 'code': 'KR'},
        {'name': 'France', 'code': 'FR'},
        {'name': 'Germany', 'code': 'DE'},
    ]

    # Xóa dữ liệu cũ trong database
    ggTrendsDailyData.objects.all().delete()

    for country_info in countries:
        country_code = country_info['code']

        # Thực hiện lấy dữ liệu trending
        trending_data = pytrends.today_searches(pn=country_code)

        for entry in trending_data:
            decoded_keyword = urllib.parse.unquote(entry.split('=')[1].split('&')[0], encoding='utf-8')
            decoded_keyword = decoded_keyword.replace('+', ' ')
            ggTrendsDailyData.objects.create(
                content=decoded_keyword,
                country=country_code
            )

@shared_task
def fetch_and_update_ggTrendsRealtimeData():
    pytrends = TrendReq()
    countries = [
        {'name': 'Vietnam', 'code': 'VN'},
        {'name': 'United States', 'code': 'US'},
        {'name': 'Japan', 'code': 'JP'},
        # {'name': 'South Korea', 'code': 'KR'},
        {'name': 'France', 'code': 'FR'},
        {'name': 'Germany', 'code': 'DE'},
    ]

    # Xóa dữ liệu cũ trong database
    ggTrendsRealtimeData.objects.all().delete()

    for country_info in countries:
        country_code = country_info['code']

        # Thực hiện lấy dữ liệu trending
        trending_data = pytrends.realtime_trending_searches(pn=country_code)
        # trending_data = trending_data.head(30)
        keyword_list = trending_data.to_records(index=False).tolist()
        # Loại bỏ dấu ngoặc đơn và dấu phẩy từ mỗi chuỗi trong danh sách
        cleaned_list = [item[0].replace("'", "").replace(",", "") for item in keyword_list]
        

        for entry in cleaned_list:        
            
            ggTrendsRealtimeData.objects.create(
                content=entry,
                country=country_code
            )