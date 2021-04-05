from platform import uname
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time, pickle


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
        self.browser = webdriver.Chrome("./chromedriver")
        
    def __str__(self):
        return f"{self.username}"



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

    def reset_data(self, data):
        pickle.dump({}, open(f"{data}.json", "wb"))        

    def search_hashtag(self, hashtag, mode="like", sum=7):
        try:
            self.browser.get("https://www.instagram.com/")

        except:
            log = pickle.load(open("error_log.txt", "rb"))
            log.append(f"{time.strftime('%H:%M:%S')}\tCant open 'https://www.instagram.com/'\n")
            pickle.dump(log, open("error_log.txt", "wb"))


        try:
            search_entry = self.wait_for_object(By.CSS_SELECTOR, "input.XTCLo.x3qfX")
            time.sleep(5)
            search_entry.send_keys(f"#{hashtag}")
            time.sleep(5)  
            search_entry.send_keys(Keys.ENTER)
            search_entry.send_keys(Keys.ENTER)
            time.sleep(10)

        except:
            log = pickle.load(open("error_log.txt", "rb"))
            log.append(f"{time.strftime('%H:%M:%S')}\tCant open 'input.XTCLo.x3qfX' aka 'search_entry' for hashtags\n")
            pickle.dump(log, open("error_log.txt", "wb"))


        try:
            time.sleep(5)
            #self.browser.execute_script("window.scrollTo(0, 4000)")
            all_photos = self.wait_for_objects(By.CSS_SELECTOR, "div.v1Nh3.kIKUG._bz0w")
            time.sleep(5)

            for i in range(len(all_photos[:sum])):
                try:
                    all_photos[i].click()

                except:
                    log = pickle.load(open("error_log.txt", "rb"))
                    log.append(f"{time.strftime('%H:%M:%S')}\tCant click Photo num: {i}\n")
                    pickle.dump(log, open("error_log.txt", "wb"))


                if mode == "like":
                    try:
                        time.sleep(5)
                        self.wait_for_object(By.CSS_SELECTOR, "[aria-label='Gefällt mir']").click()
                        time.sleep(10)
                        
                        try:
                            self.wait_for_object(By.CSS_SELECTOR, "[aria-label='Schließen']").click()
                            time.sleep(5)

                        except:
                            log = pickle.load(open("error_log.txt", "rb"))
                            log.append(f"{time.strftime('%H:%M:%S')}\tCant open '[aria-label='Schließen']'\n")
                            pickle.dump(log, open("error_log.txt", "wb"))

                    except:
                        log = pickle.load(open("error_log.txt", "rb"))
                        log.append(f"{time.strftime('%H:%M:%S')}\tCant open '[aria-label='Gefällt mir']'\n")
                        pickle.dump(log, open("error_log.txt", "wb"))


                elif mode == "collect":
                    try:
                        time.sleep(5)
                        link = self.browser.current_url
                        name = self.wait_for_object(By.CSS_SELECTOR, "a.sqdOP.yWX7d._8A5w5.ZIAjV").text
                        description = self.wait_for_object(By.CSS_SELECTOR, ".C4VMK > span").text
                        time.sleep(5)

                        data = pickle.load(open("posts.json", "rb"))

                        if name in data:
                            data[name][f"{i + 1}"] = [link, description]

                        else:
                            data[name] = {"1": [link, description]}

                        pickle.dump(data, open("posts.json", "wb"))
                        time.sleep(10)

                        try:
                            self.wait_for_object(By.CSS_SELECTOR, "[aria-label='Schließen']").click()
                            time.sleep(5)

                        except:
                            log = pickle.load(open("error_log.txt", "rb"))
                            log.append(f"{time.strftime('%H:%M:%S')}\tCant open '[aria-label='Schließen']'\n")
                            pickle.dump(log, open("error_log.txt", "wb"))


                    except:
                        log = pickle.load(open("error_log.txt", "rb"))
                        log.append(f"{time.strftime('%H:%M:%S')}\tCant get 'link', 'name', 'description'\n")
                        pickle.dump(log, open("error_log.txt", "wb"))



        except:
            log = pickle.load(open("error_log.txt", "rb"))
            log.append(f"{time.strftime('%H:%M:%S')}\tCant open 'div.v1Nh3.kIKUG._bz0w' aka 'all_photos'\n")
            pickle.dump(log, open("error_log.txt", "wb"))

    def check_storys(self):
        swipeUps = []
        try:
            storys = self.wait_for_objects(By.CSS_SELECTOR, "button.OE3OK")

            if len(storys):
                storys[0].click()
                time.sleep(5)

                def open_storys(num=0):
                    try:
                        self.wait_for_object(By.CSS_SELECTOR, "button.FhutL").click()
                        # time.sleep(3)

                        try:
                            swipe_obj = self.wait_for_object(By.CSS_SELECTOR, "div.HDsRl")
                            swipeUps.append(swipe_obj._parent.current_url)
                            print(f"Storys checked: {num} Result: swipe up")

                        except:
                            print(f"Storys checked: {num} Result: NO swipe up")

                        open_storys(num + 1)

                    except:
                        log = pickle.load(open("error_log.txt", "rb"))
                        log.append(f"{time.strftime('%H:%M:%S')}\tNo button to right click in Storys\n")
                        pickle.dump(log, open("error_log.txt", "wb"))

                open_storys()

                pickle.dump(set(swipeUps), open("storys.json", "wb"))

        except:
            log = pickle.load(open("error_log.txt", "rb"))
            log.append(f"{time.strftime('%H:%M:%S')}\tNo Storys to check\n")
            pickle.dump(log, open("error_log.txt", "wb"))

    def follow(self, name):
        self.browser.get(f"https://www.instagram.com/{name}/")

        try:
            self.wait_for_object(By.CSS_SELECTOR, "button._5f5mN.jIbKX._6VtSN.yZn4P").click()

        except:
            log = pickle.load(open("error_log.txt", "rb"))
            log.append(f"{time.strftime('%H:%M:%S')}\tFailed to follow {name}\n")
            pickle.dump(log, open("error_log.txt", "wb"))
            return

    def unfollow(self, name):
        self.browser.get(f"https://www.instagram.com/{name}/")

        try:
            self.wait_for_object(By.CSS_SELECTOR, "button._5f5mN.-fzfL._6VtSN.yZn4P").click()

        except:
            log = pickle.load(open("error_log.txt", "rb"))
            log.append(f"{time.strftime('%H:%M:%S')}\tFailed to unfollow {name}\n")
            pickle.dump(log, open("error_log.txt", "wb"))
            return

        time.sleep(3)
        self.wait_for_object(By.CSS_SELECTOR, "button.aOOlW.-Cab_").click()

    def check_posts(self, name, sum=3):
        try:
            self.browser.get(f"https://www.instagram.com/{name}/")
            # öffnet seite des influencer #
        
        except:
            log = pickle.load(open("error_log.txt", "rb"))
            log.append(f"{time.strftime('%H:%M:%S')}\tCant open 'https://www.instagram.com/{name}/'\n")
            pickle.dump(log, open("error_log.txt", "wb"))
            return

        all_posts = self.wait_for_objects(By.CSS_SELECTOR, "div.v1Nh3.kIKUG._bz0w")

        for i in range(len(all_posts[:sum])):
            # geht neusten 3 bilder durch #
            all_posts[i].click()
            try:
                name = self.wait_for_object(By.CSS_SELECTOR, "a.sqdOP.yWX7d._8A5w5.ZIAjV").text
                text = self.wait_for_object(By.CSS_SELECTOR, ".C4VMK > span").text
                link = self.browser.current_url

            except:
                log = pickle.load(open("error_log.txt", "rb"))
                log.append(f"{time.strftime('%H:%M:%S')}\tCant get 'link', 'name', 'description'\n")
                pickle.dump(log, open("error_log.txt", "wb"))
                return


            data = pickle.load(open("posts.json", "rb"))

            if name in data:
                data[name][f"{i+1}"] = [link, text]
            else:
                data[name] = {"1":[link, text]}

            pickle.dump(data, open("posts.json", "wb"))
            time.sleep(10)

            try:
                self.wait_for_object(By.CSS_SELECTOR, "[aria-label='Schließen']").click()

            except:
                log = pickle.load(open("error_log.txt", "rb"))
                log.append(f"{time.strftime('%H:%M:%S')}\tCant open '[aria-label='Schließen']'\n")
                pickle.dump(log, open("error_log.txt", "wb"))
