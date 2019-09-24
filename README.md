# ralph-lauren-el-scraper
Scrape early links from the Ralph Lauren site

# Requirements:
pip install requests

Before using the script, find the largest PID on the site and set starting_pid to that value. You can set the range to however many 100s of PIDs you want to test.

# How it Works:
Web scraping is a common practice across many different niches. Within the sneaker community, "early links" are of particular interest. Getting links that are yet to be live is a bit of a different process than just simply parsing through the front end of a site and seeing what you can find. "Scraping" within the sneaker community requires a process I like to call *"brute scraping"*. In order to find product IDs which have been added through the site through the backend, but are still inaccessible through the front end, you must [brute force](https://en.wikipedia.org/wiki/Brute-force_attack) hundreds to thousands of product IDs to find what you are searching for. 

For some particular sites you must POST your brute forced guesses to a particular API endpoint, hoping for a response which returns JSON data containing data relating to the product you are searching for. For ralph lauren however, its a bit more simple. We are simply looking for a 200 response from a normal product URL, and taking the redirected URL to find the name of the product you have brute forced.

Hopefully this explanation can help explain a little bit about how scraping for early links works.
