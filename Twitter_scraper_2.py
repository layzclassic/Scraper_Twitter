import csv
from getpass import getpass
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# extract data from tweet data
def get_tweet_datda(card):
    # user name
    username = card.find_element_by_xpath('/div[2]/div[1]/span').text
    # handle (.// -abbrevation to find the first span tag after the current tag
    handle = card.find_element_by_xpath('.//span[contains(text(),"@")]').text
    # post date
    # sponsor content has no datatime / filter them out using date
    try:
        postdate = card.find_element_by_xpath('.//time').get_attribute('datetime')
    except NoSuchElementException:

    # content - comment & responding comment
    comment = card.find_element_by_xpath('.//div[2]/div[2]/div[1]').text
    responding = card.find_element_by_xpath(('.//div[2]/div[2]/div[2]').text
    text = comment + responding
    # reply count
    reply_count = card.find_element_by_xpath('.//div[@data-testid-"reply"]').text
    # retweet count
    retweet_count = card.find_element_by_xpath('.//div[@data-testid-"retweet"]').text
    # likes
    like_count = card.find_element_by_xpath('.//div[@data-testid-"like"]').text

    # tuple tweet data
    tweet = (username, handle, postdate, text, reply_count, retweet_count, like_count)

    return tweet

# create instance of web driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.twitter.com/login')

# login
username = driver.find_element_by_xpath('//input[@name="seeion[username_or_email]"]')
username.send_keys('')

password = driver.find_element_by_xpath('//input[@name="seeion[session[password]"]')
password.send_keys('')

password.send_keys(Keys.RETURN)

# add search term
search_term = '#AMZN'
search_input = driver.find_element_by_xpath('//input[@ara-label="Search query"]')
search_input.send_keys(search_term)
search_input.send_keys((Keys.RETURN))

# choose tag for historial data
driver.find_element_by_link_text('latest').click()

# iterate each tweet
data = []
tweet_id = set()
# javascript - keep track of the position before and after the scroll
last_position = driver.execute_script("return window.pageYOffset;")

while scrolling:
    # plural method - to return a list of elements
    cards = driver.find_elements_by_xpath('//div[@data-testid="tweet"]')
    #only extract the latest 10 tweets
    for card in cards[-10:]:
        tweet = get_tweet_data(card)
        if data:
            tweet_id = ''.join(tweet)
            #keep track of tweets already scraped by turning tweet into a string idenifier
            if tweet_id not in tweet_ids:
                tweet_ids.add(tweet_id)
                data.append(tweet)

    # use scroll attempt to prevent reading the same scroll position due to unstable internet
    scroll_attempt = 0
    while True:
        # check scroll postion
        # javascript scroll down page
        driver.execute.script('window.scrollTo(0,document.body.scrollHeight);')
        # pause the programe to pause to load before scraping the data
        sleep(1)
        current_position = driver.execute_script("return window.pageYOffset;")
        # reach the end of scrolling once last == current
        if last_position == current_position:
            scroll_attempt += 1

            # end of scroll region
            if scroll_attempt >= 3:
                scrolling = False
                break
            else:
                # attempt to scroll again
                sleep(2)
        else:
            break

    # save data to csv file
    with open('C:/Users/suen6/PycharmProjects/Scraper_Twitter_1/data/amazon.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Description', 'Quantity', 'Price', 'Rating', 'Review Count', 'Url'])
        writer.writerows(data)










