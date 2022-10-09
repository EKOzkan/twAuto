
  

# twAuto - Twitter Automation Tool 🦆

  

twAuto is a library for "Tweeting", "Retweeting", "Replying", "Tweet Quoting", "Tweet Liking" without any API requirements using Selenium.

  
<br/>


Note: While using this library I didnt encounter any problems/bad response from Twitter like banning account etc. but please use at your own risk.

## Requirements

- Python 3.6

- beautifulsoup4

- selenium

  

## Installation
 **Pip:**
```bash
pip3 install twAuto
```

**After Pip:**
Download chromium driver from https://chromedriver.chromium.org/downloads and place the chromedriver.exe file to same place as your code.
```bash
https://chromedriver.chromium.org/downloads
```

After this two steps, your directory should look like this:
```
Project File
│   yourcode.py
│   chromedriver.exe    
```

## Functions
**- Import:**
```python
import twAuto
```

<br/>

**- Configure:**
```python
tw = twAuto.twAuto(
username="Your Twitter Username",
email="Your Twitter E-Mail",
password="Your Twitter Password",
headless=True/False)
#Headless is true by default.
```

<br/>


**- Start:** Start functions runs the selenium driver.
```python
tw.start()
```

<br/>


**- Login:** Logs in to the Twitter account
```python
tw.login()
```

<br/>


**- Like:** Likes tweet in the given url \
->Returns: True/False as Success/Failed
```python
tw.like(url="")
```

<br/>


**- Reply:** Replies to the tweet in the given url with given text.\
->Returns: Reply URL/False
```python
tw.reply(url="", text="")
```

<br/>


**- Tweet:** Tweets the text and image if given.\
->Returns: Tweet URL/False
```python
tw.tweet(text="",imgpath="")
```

<br/>


**- Quote Tweet:** Quotes the tweet in the given url with the given text.\
->Returns: Quoted Tweet URL/False
```python
tw.quoteTweet(url="", text="")
```

<br/>


**- Retweet:** Retweets the tweet in the given url.\
->Returns: True/False as Success/Failed
```python
tw.retweet(url="")
```

<br/>


**- Logout:** Logs out from current Twitter account and deletes the cookies file.
```python
tw.logout()
```

<br/>


**- Quit/Close:** Ends the session, closes the selenium driver application
```python
tw.close()
```
## To Do's 📝 : 
- [ ] Send image with Quote, Reply, Retweet.
- [ ] Send gif with Quote, Reply and Retweet
- [ ] Retweet without adding url at the end.
- [ ] Linux integration.
