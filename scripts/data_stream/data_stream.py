import requests 
from bs4 import BeautifulSoup 

url = "https://www.baseball-reference.com/teams/ATL/2024-schedule-scores.shtml"
res = requests.get(url)
htmlData = res.content
parsedData = BeautifulSoup(htmlData, "html.parser") 

#prettify() to get a general idea of the response data 
print(parsedData.prettify())
