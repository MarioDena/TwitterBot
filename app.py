from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Twitbot:
    def __init__(self,user,password):
        self.user = user
        self.password = password
        self.bot = webdriver.Firefox()

    def Login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(5)
        user = bot.find_element_by_class_name('email-input')
        password = bot.find_element_by_name('session[password]')
        user.send_keys(self.user)
        password.send_keys(self.password)

        password.send_keys(Keys.RETURN)
        time.sleep(5)

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



#newBot = Twitbot("YOUR USER","YOUR PASSWORD")
newBot.Login()
newBot.GetTweets('webdeveloper')
newBot.LikeLinks()

