# twAuto - Twitter Automation Tool v0.3.9 🦆 ![PyPI](https://img.shields.io/pypi/v/twauto) [![Downloads](https://static.pepy.tech/badge/twauto)](https://pepy.tech/project/twauto)


twAuto is a library for "Tweeting", "Retweeting", "Replying", "Tweet Quoting", "Tweet Liking" without any API requirements using Selenium.

<br/>

Note: While using this library I didnt encounter any problems/bad response from Twitter like banning account etc. but please use at your own risk.


## Requirements

- Python 3.7+

- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)

- [selenium 4.4.3](https://pypi.org/project/selenium/4.4.3/)

- [webdriver-manager](https://pypi.org/project/webdriver-manager/)

## Installation

**Pip:**

```bash
pip3 install twAuto
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
  chromeDriverMode="manual" or "auto", #if you use auto twAuto will automatically download the chrome driver for you,
                                       #if you use the manual option, you need to provide the driver path in driverPath parameter.
  driverPath="your drivers path", #use only if you are using the chromeDriverMode in manual mode 
  pathType="testId" or "xPath", #It is testId by default. I highly recommend you to use testId instead of xPath. If you had any problems with library you can try the xPath mode too.
  headless=True/False, #Headless is true by default.
  debugMode= True/False #Really poorly implemented debug mode, this is for reading occured errors.
                        #It is not reliable right now but you can give it a try if you want to.
  createCookies= True/False #True by default.
)

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

**- Login Errors:** If you encounter any errors in the login process, you can use manualCookieCreation() to get your cookie file manually.
Run the function after tw.start() line. Then after the browser window opened, login to account you want to automate, then enter any character in the terminal. This will create a cookie file after this, you can use the library.

Note: Headless must be False to use this function.

```python
tw.manualCookieCreation()
```

Example:

First run this code to get your cookie file.

```python
tw = twAuto.twAuto(
  username="Your Twitter Username",
  email="Your Twitter E-Mail",
  password="Your Twitter Password",
  chromeDriverMode="auto",
  pathType="xPath",
  headless=False #Headless must be False to use this function.
)

tw.start()
tw.manualCookieCreation()
```

After doing the steps that is described above, you can run your main code.

```python
tw = twAuto.twAuto(
  username="Your Twitter Username",
  email="Your Twitter E-Mail",
  password="Your Twitter Password",
  chromeDriverMode="auto",
  pathType="xPath"
)

tw.start()
tw.login()
#other functions...
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
tw.reply(url="", imgpath="", text="")
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
tw.quoteTweet(url="", imgpath="" ,text="")
```

<br/>

**- Retweet:** Retweets the tweet in the given url.\
->Returns: True/False as Success/Failed

```python
tw.retweet(url="")
```

<br/>

**- Unretweet:** Unretweets the tweet in the given url.\
->Returns: True/False as Success/Failed

```python
tw.unretweet(url="")
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

## Example Code

```python
tw = twAuto.twAuto(
  username="",
  email="",
  password="",
  headless=True,
  chromeDriverMode="auto",
  pathType="testId")

tw.start()
tw.login()

tw.reply(url="",imgpath="", text="")

tw.close()

```

## To Do's 📝 :

- [x] Send image with Quote, Reply.
- [ ] Send gif with Quote, Reply.
- [x] Retweet without adding url at the end.
- [ ] Linux integration(not tested yet).
