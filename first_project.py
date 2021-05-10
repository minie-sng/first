from urllib.request import urlopen
from bs4 import BeautifulSoup

country = input('country - ')
# 전세계 : worldwide, 한국 : south-korea, 미국 : united-states, 일본 : japan, 중국 : china, 등등...

html = urlopen("https://playboard.co/chart/video/most-viewed-all-videos-in-%s-total" %country)

soup = BeautifulSoup(html, "lxml")

chart_table = soup.find_all('table',{'class':'sheet sheet sheet--viewed'})

chart_table_tbody=chart_table[0].find_all("tbody")

chart_table_tbody_row= chart_table_tbody[0].find_all("tr")

chart_info = []
count = 0
for tr in chart_table_tbody_row:
    chart_list = []
    div = tr.find_all('div',{'class':'current'})
    a = tr.find_all('a',{'class':'title__label'})
    count += 1
    if count == 6:
        continue
    # 6번째 리스트(tr)에 정보가 아닌 사이트 광고가 담겨있기 때문에 count 변수 설정해서 6일때 continue

    for content in div:
        print(content.get_text(), end=' ')
        chart_list.append(content.get_text())

    for content in a:
        print(content.get_text())
        chart_list.append(content.get_text())

    print("")
    chart_info.append(chart_list)