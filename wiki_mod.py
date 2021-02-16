from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class Selenium_Driver:
    def __init__(self, search_query):
        self.PATH = 'C:\Program Files (x86)\chromedriver.exe'
        self.options = Options()
        self.options.headless = True

        self.driver = webdriver.Chrome(self.PATH, options=self.options)

        self.driver.get('https://www.wikipedia.org/')

        self.search_bar = self.driver.find_element_by_xpath('//*[@id="searchInput"]')
        self.search_q = search_query

        self.search_bar.send_keys(self.search_q)
        self.search_bar.send_keys(Keys.RETURN)

    def get_results(self):
        try:
            main_page = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="mw-content-text"]/div[1]'))
            )

            for stuff in main_page:
                title = stuff.find_elements_by_tag_name('h2')

                content = stuff.find_elements_by_tag_name('p')

                biography_card = stuff.find_elements_by_xpath('//*[@id="mw-content-text"]/div[1]/table[1]')

                contents_content = []
                for stuff in content:
                    contents_content.append(stuff.text)

                contents_biogr = []
                for others in biography_card:
                    contents_biogr.append(others.text)

                contents_title = []
                for ncr in title:
                    contents_title.append(ncr.text)

            return contents_content, contents_biogr, contents_title

        except Exception as E:
            print(E)

    def exit_driver(self):
        self.driver.quit()

if __name__ == '__main__':
    import sys
    args = sys.argv[2:]
    args_n = sys.argv

    if len(args_n) < 2:
        print('Usage: wiki_mod.py -opt search_query')
        exit(0)

    string = ' '.join(map(str, args))
    # print(string)

    new_driver = Selenium_Driver(string)
    container = new_driver.get_results()

    try:
        if args_n[1] == '-h':
            print('Usage: wiki_mod.py -opt search_query')

        elif args_n[1] == '-b':
            for boxes in container[1]:
                print(boxes)
                print()

            print('\n\n\n')

        elif args_n[1] == '-c':
            for boxes in container[0]:
                print(boxes)
                print()

            print('\n\n\n')

        new_driver.exit_driver()

    except Exception as E:
        print(E)
        print('The result you searched for was probably not found. Try searching something else')

        exit(1)
        x.exit_driver()
