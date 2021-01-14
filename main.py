#===========================
# Imports
#===========================

import pyinputplus as pyip
from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys

#===========================
# Main App
#===========================

class Google_Search:
    def __init__(self, query):
        self.driver = wd.Firefox(executable_path=r'C:\\Python\\Selenium\\Firefox\\geckodriver.exe')
        self.google_url = 'https://www.google.com/'
        self.query = query
        self.search()

    def search(self):
        """Simulate Google search."""
        self.driver.maximize_window()
        self.driver.get(self.google_url)

        selector = self.driver.find_element_by_name('q')
        selector.clear()
        selector.send_keys(self.query)
        selector.send_keys(Keys.ENTER)

def main():
    query = pyip.inputStr('Search: ')
    app = Google_Search(query)

#===========================
# Start App
#===========================

if __name__ == '__main__':
    main()