import requests
import pandas as pd
# Using advanced google search, search for keywords on google news.
# You can change from google news to other google webs
websites = {
    'BBC': 'www.google.com',
}

keywords = [
    'korea',
]
# Go to the following web and get your own api key
api_url = 'https://api.scrape-it.cloud/scrape/google'
headers = {'x-api-key': ''} # Enter your API Key here

# Create an empty dictionary to store the results
results = {website: {} for website in websites}

for website_name, website_domain in websites.items():
    for keyword in keywords:
        params = {
            'q': keyword,
            'site': website_domain,
            'tbm': 'nws'
        }
        try:
            response = requests.get(api_url, params=params, headers=headers)
            if response.status_code == 200:
                data = response.json()
                news = data['newsResults']
                results[website_name][keyword] = [article['title'] for article in news]
        except Exception as e:
            print(f'Error scraping {website_name} for keyword {keyword}:', e)

# Create a Pandas DataFrame from the results dictionary
df = pd.DataFrame(results)

# Write the DataFrame to an Excel file
df.to_excel("results.xlsx", index_label="Keyword")

print("Results saved to news_results.xlsx")
