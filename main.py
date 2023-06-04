import requests
from bs4 import BeautifulSoup
from datetime import datetime
import mysql.connector

def get_playlist(station):
    db_connection()
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
        db_insert(station, tmp_time, artists[x], songs[x])
        
def db_connection():
    global mydb, mycursor
    mydb = mysql.connector.connect(
      host="YOUR_HOST",
      user="YOUR_USER",
      password="YOUR_PASSWORD",
      database="YOUR_DATABASE"
    )
    mycursor = mydb.cursor()

def db_insert(station, time_played, artist, song):
    sql = "INSERT IGNORE INTO `played_songs`(`station`, `time_played`, `artist`, `song`) VALUES (%s, %s, %s, %s)"
    val = (str(station), str(time_played), str(artist), str(song))
    mycursor.execute(sql, val)
    mydb.commit()
    

get_playlist("radio-bollerwagen")