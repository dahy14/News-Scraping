from bs4 import BeautifulSoup
from datetime import date
import requests, csv, os

# saving the file in csv
os.makedirs('News', exist_ok=True)
file_csv = date.today().strftime("%m-%d-%Y") + ".csv"
file_csv = os.path.join("News/", file_csv)

header = ['#', 'Link', 'News', 'Description']
csv_file = open(file_csv, 'w', newline ='')
csv_writer = csv.DictWriter(csv_file, fieldnames=header)
csv_writer.writeheader()


# data scraping
url = "https://www.philstar.com/"
data = requests.get(url)
soup = BeautifulSoup(data.text, 'html.parser')
soup = soup.find_all('div', class_="TilesText spec")
n = 1
for item in soup: 
    news = item.find('div', class_='news_title').text
    link = item.find('a').get('href')
    descr = item.find('div', class_="news_summary").text
    print(n, link, news, "\n", descr, "\n")
    # putting the scraped data inside the csv file
    csv_writer.writerow({
        "#": n,
        'Link': link,
        'News': news,
        'Description': descr 
    })

    n += 1 

csv_file.close()