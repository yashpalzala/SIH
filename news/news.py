from newsapi import NewsApiClient
from pprint import pprint
import datetime

#text = "Hello World"

#gs = goslate.Goslate()
#translatedText = gs.translate(text,'hi')

#print(translatedText)
# Init
newsapi = NewsApiClient(api_key='9933009e1f5842a4a71e9f927df871a3')

# set dates for articles
yesterday = (datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
buffer_date = (datetime.date.today() - datetime.timedelta(days=10)).strftime('%Y-%m-%d')
# print(yesterday)
# print(buffer_date)

# keywords or phrases for filtering news
phrases = 'farmers OR farming OR agriculture OR (crop AND production) OR crops OR (organic AND farming) OR (food AND crop)'

# /v2/everything
all_articles = newsapi.get_everything(qintitle=phrases,
                                      sources='the-hindu',
                                      domains='jagran.com,bhaskar.com,hindustantimes.com',
                                      from_param=buffer_date,
                                      to=yesterday,
                                      # language='en',
                                      sort_by='publishedAt',
                                      page=1,
                                      page_size=20)

filtered_articles = []
articles = all_articles['articles']
for article in articles:
    del article['author']
    del article['content']
    del article['publishedAt']
    del article['source']
    #del article['url']
    del article['urlToImage']
    filtered_articles.append(article)

pprint(filtered_articles[:5])

#for i in filtered_articles:

dislist=[]
one = filtered_articles[0]['description']
two = filtered_articles[1]['description']
three = filtered_articles[2]['description']
four = filtered_articles[3]['description']
five = filtered_articles[4]['description']
dislist.append(one)
dislist.append(two)
dislist.append(three)
dislist.append(four)
dislist.append(five)
pprint(dislist)





