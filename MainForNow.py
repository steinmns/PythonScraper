import requests, sys, webbrowser, bs4

print('Searching...')
res = requests.get('https://www.yahoo.com/')

#Makes sure that request succeeds before continuing
res.raise_for_status()  

#Creates a beautiful soup object
soup = bs4.BeautifulSoup(res.text, 'html.parser')

#Gets list of 10 Trending Topics from Yahoo
topics = soup.select('.Mstart\(2px\)')

#Prints Topics to Console
print('Current Trending Topics: ')
for topic in topics:
    print(topic.next)
