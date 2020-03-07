import praw
import time
i = 0

reddit = praw.Reddit(client_id="NVnj5732Ao6JMg",
    client_secret="HRK5VB5bK-R8itDciSbDjBOIUJA",
    username="Danus_Arulnesan",
    password="dabonemhaters4786",
    user_agent="AppNana")

def SendThread(x):
    global i
    title = "f24289498"
    selftext = ''
    reddit.subreddit(x).submit(title,selftext)
    i += 1
    print(f"\n{i} message(s) have been sent.")
    time.sleep(3600)

appnana1 = reddit.subreddit('AppnanaInviteCodes')
appnana2 = reddit.subreddit('Appnana')
print(reddit.user.me())
for w in range(1,12):
    title='f24289498'
    selftext=""
    reddit.subreddit("appnana").submit(title,selftext)
    i += 1
    print(f'\n{i} message(s) have been sent.')
    time.sleep(3600)
