from selenium import webdriver
from time import sleep


not_following_back =[]
class InstaPyBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome()
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]")\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        sleep(2)

    def find_unfollowers(self):
        self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username))\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
            .click()
        following = self._find_names()
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]")\
            .click()
        followers = self._find_names()
        not_following_back = [user for user in following if user not in followers]
        print(not_following_back)

    def _find_names(self):
        sleep(2)
        scrollingBox = self.driver.find_element_by_class_name("isgrP")
        self.driver.execute_script('arguments[0].scrollIntoView()', scrollingBox)
        sleep(2)
        scroll_box = self.driver.find_element_by_class_name("isgrP")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']

        # close button
        self.driver.find_element_by_class_name("wpO6b")\
            .click()
        return names

    def unfollow(self):
        sleep(2)
        for user in not_following_back:
            self.driver.get("https://instagram.com" + user)
            sleep(2)
            self.driver.find_element_by_class_name("_5f5mN    -fzfL     _6VtSN     yZn4P   ")\
                .click()



arminInsta = InstaPyBot('arminlokvancic', "#")
arminInsta.find_unfollowers()
webdriver.Chrome.close()