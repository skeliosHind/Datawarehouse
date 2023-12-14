import requests
from bs4 import BeautifulSoup
import csv

def scrape_and_save_to_csv(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Rest of your code...
        # Find the container that holds the comments
        commentcontainer = soup.find('ul', class_='comment-list hide-comments')

        if commentcontainer:
            # Open a CSV file for writing
            with open('All2.csv', 'a', newline='', encoding='utf-8') as csvfile:
                # Create a CSV writer
                csv_writer = csv.writer(csvfile)

                # Iterate over each comment in the container
                for comment in commentcontainer.find_all('div', class_='comment-body'):
                    # Extract data from each comment
                    author_element = comment.find('span', class_='fn heey')
                    date_element = comment.find('div', class_='comment-date')
                    react_num = comment.find('span', class_='comment-recat-number')
                    commenttext_element = comment.find('div', class_='comment-text')

                    # Check if the elements exist before accessing their attributes
                    if author_element and date_element and react_num and commenttext_element:
                        author = author_element.text.strip()
                        date = date_element.text.strip()
                        likes = react_num.text.strip()
                        commenttext = commenttext_element.text.strip()

                        # Write data to the CSV file
                        csv_writer.writerow([author, date, likes, commenttext])
                    else:
                        print("Skipping comment due to missing element(s).")

            print(f"Comments data for {url} has been saved to 'All.csv'")
        else:
            print(f"No comments found on the page: {url}")
    else:
        print(f"The request for {url} failed with code: {response.status_code}")

# List of URLs to scrape
url_list = [
    "https://www.hespress.com/نقابة-نسبة-انخراط-نساء-ورجال-التعليم-ف-1281042.html",
    "https://www.hespress.com/الاحتقان-في-قطاع-التعليم-يعيد-التذكير-1280590.html",
    "https://www.hespress.com/امتداد-الإضرابات-ضد-النظام-الأساسي-ي-1279024.html",
    "https://www.hespress.com/أساتذة-الزنزانة-10-يطلبون-جبر-الضرر‬-1210590.html"
    # Add more URLs as needed
]

# Iterate through each URL and scrape data
for url in url_list:
    scrape_and_save_to_csv(url)