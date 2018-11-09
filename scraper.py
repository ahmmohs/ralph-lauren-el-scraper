import requests
import threading

url = 'https://www.ralphlauren.com/p/p/'
starting_pid = 480057

print("--------------------------------------------")
print("      RALPH LAUREN EARLY LINK SCRAPER       ")
print("                by @ahmMohs                 ")
print("--------------------------------------------")

def checkUrl(x):
    try:
        r = requests.get(x)
        if 'hidden' in r.url:
            print(r.url)
    except:
        pass

for x in range(starting_pid, 481100):
    curl = url + str(x) + '.html'
    t = threading.Thread(target=checkUrl, args=(curl,))
    t.start()
