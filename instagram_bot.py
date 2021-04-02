from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time, pickle

count = 0

class InstagramBot():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.error_log = ""
        
        self.browser = webdriver.Chrome("./chromedriver.exe")
        
    def wait_for_object(self, type, string):
        return WebDriverWait(self.browser, 3).until(EC.presence_of_element_located((type, string)))
    
    def wait_for_objects(self, type, string):
        return WebDriverWait(self.browser, 3).until(EC.presence_of_all_elements_located((type, string)))

    def login(self):
        self.browser.get("https://www.instagram.com/accounts/login")
        fensterOne = self.wait_for_object(By.CSS_SELECTOR, "button.aOOlW.bIiDR").click()
        # cockies #

        login_objects = self.wait_for_objects(By.CSS_SELECTOR, "input._2hvTZ.pexuQ.zyHYP")

        login_objects[0].send_keys(self.username)
        login_objects[1].send_keys(self.password)
        login_objects[1].send_keys(Keys.ENTER)
        
        time.sleep(10)
        fensterTwo = self.wait_for_object(By.CSS_SELECTOR, "button.sqdOP.yWX7d.y3zKF").click()
        # login daten speichern frage #

        fensterThree = self.wait_for_object(By.CSS_SELECTOR, "button.aOOlW.HoLwm").click()
        # notification on #

    def Search_hashtag(self, hashtag, analyse=False, like=True, fromList=False):
        def start_searching():
            try:
                time.sleep(3)
                search_entry.send_keys(Keys.ENTER)
                # select #
                search_entry.send_keys(Keys.ENTER)
                # confirm #
                time.sleep(50)
                self.browser.execute_script("window.scrollTo(0, 4000)")
                # läd mehr pics #
                all_photos = self.wait_for_objects(By.CSS_SELECTOR, "div.v1Nh3.kIKUG._bz0w")
                for photo in all_photos:
                    # geht alle bilder durch #
                    try:
                        photo.click()
                        if analyse:
                            name = self.wait_for_object(By.CSS_SELECTOR, "a.sqdOP.yWX7d._8A5w5.ZIAjV").text
                            text = self.wait_for_object(By.CSS_SELECTOR, ".C4VMK > span").text
                            data = pickle.load(open("instaData.txt", "rb"))
                            data[name] = text
                            pickle.dump(data, open("instaData.txt", "wb"))
                            time.sleep(50)

                        elif like:
                            self.wait_for_object(By.CSS_SELECTOR, "[aria-label='Gefällt mir']").click()
                            time.sleep(50)

                        self.wait_for_object(By.CSS_SELECTOR, "[aria-label='Schließen']").click()

                    except:
                        self.error_log += "ERROR 003: cant click photo"

            except:
                self.error_log += "ERROR 004: cant get photo"

        if fromList:
            hashtags = open("hashtags.txt", "r").readlines()
            hashtags = "".join(hashtags).replace("\n", "").split("#")
            for val in hashtags:
                self.browser.get("https://www.instagram.com/")
                search_entry = self.wait_for_object(By.CSS_SELECTOR, "input.XTCLo.x3qfX")
                print(val)
                search_entry.send_keys(f"#{val}")
                start_searching()
        else:
            search_entry = self.wait_for_object(By.CSS_SELECTOR, "input.XTCLo.x3qfX")
            search_entry.send_keys(f"#{hashtag}")
            start_searching()


    def check_storys(self):

        swipeUps = []
        storys = self.wait_for_objects(By.CSS_SELECTOR, "button.OE3OK")
        if len(storys):
            storys[0].click()
            time.sleep(5)
            def open_storys():
                global count
                count += 1
                try:
                    self.wait_for_object(By.CSS_SELECTOR, "button.FhutL").click()
                    #time.sleep(3)

                    try:
                        swipe_obj = self.wait_for_object(By.CSS_SELECTOR, "div.HDsRl")
                        swipeUps.append(swipe_obj._parent.current_url)
                        print(f"Storys checked: {count} Result: swipe up")

                    except:
                        print(f"Storys checked: {count} Result: NO swipe up")

                    open_storys()

                except:
                    print("no button to right click")
                    return

            open_storys()

            return set(swipeUps)

    def follow(self, name):
        self.browser.get(f"https://www.instagram.com/{name}/")

        try:
            self.wait_for_object(By.CSS_SELECTOR, "button._5f5mN.jIbKX._6VtSN.yZn4P").click()

        except:
            self.error_log += f"ERROR 001: failed to follow {name}\n"

    def unfollow(self, name):
        self.browser.get(f"https://www.instagram.com/{name}/")

        try:
            self.wait_for_object(By.CSS_SELECTOR, "button._5f5mN.-fzfL._6VtSN.yZn4P").click()

        except:
            self.error_log += f"ERROR 002: failed to unfollow {name}\n"

        time.sleep(3)
        self.wait_for_object(By.CSS_SELECTOR, "button.aOOlW.-Cab_").click()

    def check_posts(self, name):
        self.browser.get(f"https://www.instagram.com/{name}/")
        # öffnet seite des influencer #

        try:
            all_posts = self.wait_for_objects(By.CSS_SELECTOR, "div.v1Nh3.kIKUG._bz0w")

            for i in range(len(all_posts[:3])):
                # geht neusten 3 bilder durch #
                all_posts[i].click()
                name = self.wait_for_object(By.CSS_SELECTOR, "a.sqdOP.yWX7d._8A5w5.ZIAjV").text
                text = self.wait_for_object(By.CSS_SELECTOR, ".C4VMK > span").text
                link = self.browser.current_url

                data = pickle.load(open("instaData.txt", "rb"))

                if name in data:
                    data[name][f"{i+1}"] = [link, text]
                else:
                    data[name] = {"1":[link, text]}

                pickle.dump(data, open("instaData.txt", "wb"))
                # self.WaitForObject(By.CSS_SELECTOR, "[aria-label='Gefällt mir']").click()
                time.sleep(10)
                self.wait_for_object(By.CSS_SELECTOR, "[aria-label='Schließen']").click()

        except:
            pass

    def reset_data(self):
        pickle.dump({}, open("instaData.txt", "wb"))
        # setzt alle beschreibungen zurück #

    def check_links_of_swipe_up(self):
    # öffnet alle swipe_ups und returnt die links #
        storys = pickle.load(open("links.txt", "rb"))
        pages = []
        for swipe_up in storys:
            self.browser.get(swipe_up)
            time.sleep(3)
            self.wait_for_object(By.CSS_SELECTOR, "button.sqdOP.L3NKy.y1rQx.cB_4K").click()
            time.sleep(3)
            window = self.wait_for_object(By.CSS_SELECTOR, "div.HDsRl").click()
            time.sleep(3)
            self.browser.switch_to_window(self.browser.window_handles[0])

        return pages

def stuff():
    influencer = pickle.load(open("influencer.txt", "rb"))
    for name in [i for i in influencer]:
        try:
            Bot.check_posts(name)
            #time.sleep(10)
        except:
            continue

Bot = InstagramBot("name", "pw")
# account

Bot.login()
#Bot.reset_data()
Bot.Search_hashtag("lifestyle", fromList=True)
#links = Bot.check_storys()
#pickle.dump(links, open("links.txt", "wb"))
#ages = Bot.check_links_of_swipe_up()
#for i in pages:
    #print(i)
#stuff()

#Bot.browser.close()
pickle.dump(Bot.error_log, open("error_log.txt", "wb"))
