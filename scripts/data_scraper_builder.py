import requests 
from bs4 import BeautifulSoup 

url = "https://www.baseball-reference.com/teams/ATL/2024-schedule-scores.shtml"
res = requests.get(url)
htmlData = res.content
parsedData = BeautifulSoup(htmlData, "html.parser") 

# team page title
print(parsedData.title.string)

# section title 
sectionTitleContainer = parsedData.find('span', attrs={"id":"win_loss_link", "data-label":"Team Win/Loss Splits"})
print(sectionTitleContainer)
sectionTitle = sectionTitleContainer.find_next('h2')
print(sectionTitle.text)

# Overall Split Data 
overallTitleContainer = parsedData.find('div', attrs={"class":"data_grid_box", "id":"win_loss_1"})
print(overallTitleContainer)

#prettify() to get a general idea of the response data 
#print(parsedData.prettify())





# testing shit out 
#
#for titles in winTitleContainer:
#    print(titles.find_next('h2'))


#for titles in winTitle: 
#    print(titles.text)

# in order to better work with data that you want to scrape
# you need to implement a command line data viewer pip package 
# think pandas but maybe a lighter-weight alternative 

