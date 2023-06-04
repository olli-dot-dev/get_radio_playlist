import requests
from bs4 import BeautifulSoup
from datetime import datetime


def get_playlist(station):
    URL="https://myonlineradio.de/"+station+"/playlist"
    website = requests.get(URL)
    results = BeautifulSoup(website.content, 'html.parser')
    results = results.find("div", {"class": "js-songListC"})

    for span in results.find_all('span',{'class': 'txt2 mcolumn'}):
        times = [span.string for span in results.find_all('span',{'class': 'txt2 mcolumn'})]

    for span in results.find_all('span',itemprop="byArtist"):
        artists = [span.string for span in results.find_all('span',itemprop="byArtist")]
        
    for span in results.find_all('span',itemprop="name"):
        songs = [span.string for span in results.find_all('span',itemprop="name")]


    times = [sub.replace('LIVE - ', '') for sub in times]
    tmp_replace=".23 "
    times = [sub.replace(' ', tmp_replace) for sub in times]

    for x in range(len(artists)):
        tmp_time=datetime.strptime(times[x], '%d.%m.%y %H:%M')
        print (x," ",tmp_time,":",artists[x],":", songs[x])
        
get_playlist("radio-bollerwagen")
