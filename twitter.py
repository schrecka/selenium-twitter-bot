from selenium import webdriver
#from getpass import getpass
from time import sleep

username = "thegreeksneak"
password = "thegreeksneak"
tweet = raw_input('Input tweet : ')
#username = raw_input('Please enter your username: ')
#password = raw_input('Please enter your password: ')
#password = getpass('Please enter your password: ')

driver = webdriver.Chrome("/Users/Adam/Desktop/ind_projects/chromedriver")
driver.get('https://twitter.com/login?lang=en')

username_box = driver.find_element_by_class_name('js-username-field')
username_box.send_keys(username)
sleep(1)

password_box = driver.find_element_by_class_name('js-password-field')
password_box.send_keys(password)
sleep(1)

login_button = driver.find_element_by_css_selector('button.submit.EdgeButton.EdgeButton--primary.EdgeButtom--medium')
login_button.submit()
sleep(1)

text_box = driver.find_element_by_id('tweet-box-home-timeline')
text_box.send_keys(tweet)
sleep(1.5)


tweet_button = driver.find_element_by_css_selector('button.tweet-action.EdgeButton.EdgeButton--primary.js-tweet-btn')
tweet_button.click()
sleep(3)

like_tweet = driver.find_element_by_css_selector('button.ProfileTweet-actionButton.js-actionButton.js-actionFavorite')
like_tweet.click()
sleep(5)

