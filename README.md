## Scraping for sports data
Initially need to determine the setup of my python microservice. I ideally want to run this script with a cron scheduler and port all scraped data to a cloud enabled relational DB like [supabase](https://supabase.com/docs). There needs to be some thought given to the architecture of this script and thinking about the correct way to bundle this with the REST api built with Node.js

### Project Structure
There needs to be a include research on best approach for managing a python microservice, a node.js api, and a [insert frontend js-framework here] web app. For the python microservice I will be using Git for version control and host my python service/node.js backend app on a virtual private server; I can use nginx to host the front-end on the same vps but on a different exposed port

- Python Scraper: First part of the process is setting up a pipeline for pulling scraped data into supabase.
- Adding Sources: The first scraper will use PrizePicks as it's initial data source, then we will look to add more.
- VPS Environment: Setup the cron scheduler and hosting options once the scraper and data source have been configured.  

### Improvement and Testing
There will be a number of issues with consistency and security (i.e. handling login requirements and authentication). Initially we need to find ways to build out a testing system so that logging and monitoring can be a fundamental piece of this app

### Scraping with BS4, and a look at alternatives
> Official documentation for [BeautifulSoup4](https://beautiful-soup-4.readthedocs.io/en/latest/#)

Web Scraping foundations: extracting HTML => filtering for data => managing data streams

BeautifulSoup is used for HTML parsing and MechanicalSoup is used for form interactions. Both are useful when parsing HTML pages and extracting content (some content is locked behind interactive walls - i.e. login pages - and mechanicalSoup helps to get around that issue)

Web scraping is more thanr just parsing HTML - in order to write scripts, manage schedulers and generate feed exports, you will need a complete toolkit for data extraction: [Scrapy](https://scrapy.org/).

#### Baseball Data `deep-dive`
This is a data capture breakdown of the website [Baseball Reference](https://www.baseball-reference.com/)

The response data can be dissected and better understood using the  "html.parser" method that BeautifulSoup offers. 
