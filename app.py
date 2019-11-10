from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

class Twitbot:
  def __init__(self, user, password, email):
    self.user = user
    self.password = password
    self.email = email
    self.driver = webdriver.Firefox()

  def Login(self):
    bot = self.driver
    bot.get('https://twitter.com/login')
    bot.implicitly_wait(10) # seconds

    emailInput = bot.find_element_by_class_name('js-username-field')
    emailInput.send_keys(self.user)

    passwordInput = bot.find_element_by_class_name('js-password-field')
    passwordInput.send_keys(self.password)
    passwordInput.send_keys(Keys.RETURN)

    print(bot.current_url)

# TODO: Solves the challenge page
# def solveChallenge():
#   dom contains 'Help us keep your account safe.'
#   url contains login_challenge

def GetTweets(self,hashtag):
    bot = self.bot
    bot.get("https://twitter.com/search?q=" + hashtag + "&src=typeahead_click")
    time.sleep(2)
    for i in range(1,3):
        bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(2)

def LikeLinks(self):
    tweetLinks=[]
    bot = self.bot
    try:
        tweetLinks = [i.get_attribute('href')
            for i in bot.find_elements_by_xpath("//a[@role='link']")]
    except Exception as e:
        print("Something went wrong getting tweet links:", e)

    if (len(tweetLinks) == 0):
        return []

    filteredLinks = list(filter(lambda x: 'status' in x,tweetLinks))
    print("Got {} tweet links".format(len(filteredLinks)))
    print(filteredLinks)

    for link in filteredLinks:
        bot.get(link)
        time.sleep(2)
        try:
            bot.find_element_by_xpath("//div[@data-testid='like']").click()
            print ("liked tweet")
            time.sleep(10)
        except Exception as ex:
            time.sleep(60)



newBot = Twitbot("EbRobot", "TestingPass", "example@email.com")
newBot.Login()
newBot.GetTweets('webdeveloper')
newBot.LikeLinks()

