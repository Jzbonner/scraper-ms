import mechanicalsoup 
# import time

browser = mechanicalsoup.Browser()
# the below link gives a phishing warning due to lack of https
url = "http://olympus.realpython.org/login"
page = browser.get(url)
page_html = page.soup

form = page_html.select("form")[0] 
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"

profiles = browser.submit(form, page.url)

print(profiles.url)