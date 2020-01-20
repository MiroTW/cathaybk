import unittest
import time
from selenium import webdriver

class cathaybk(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        #chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get('https://www.cathaybk.com.tw/cathaybk/')

    def tearDown(self):
        self.driver.quit()

    #homepage
    # def test_001(self):
    #     self.driver.get_screenshot_as_file('D://cathaybk_home.png')

    #logo
    # def test_002(self):
    #     Logo = self.driver.find_element_by_xpath('//*[@id="img_87B76E5243D74163B1282B0048D0A216"]')
    #     Logo.click()
    #     self.assertEqual(self.driver.current_url, 'https://www.cathaybk.com.tw/cathaybk/')

    #SiteMenuLink
    # def test_003(self):
    #     SiteMenuLink = self.driver.find_elements_by_id('lnk_pc-megamenu_SiteMenuLink')
    #     SiteMenuLink[0].click()
    #     self.assertEqual(self.driver.current_url, 'https://www.cathaybk.com.tw/cathaybk/personal/')
    # def test_004(self):
    #     SiteMenuLink = self.driver.find_elements_by_id('lnk_pc-megamenu_SiteMenuLink')
    #     SiteMenuLink[1].click()
    #     self.assertEqual(self.driver.current_url, 'https://www.cathaybk.com.tw/cathaybk/corp/')
    # def test_005(self):
    #     SiteMenuLink = self.driver.find_elements_by_id('lnk_pc-megamenu_SiteMenuLink')
    #     SiteMenuLink[2].click()
    #     for handle in self.driver.window_handles:
    #         window_after = self.driver.window_handles[1]
    #         self.driver.switch_to.window(window_after)
    #     self.assertEqual(self.driver.current_url, 'https://www.cathaybk.com.tw/cathaybk/private-bank/default.asp')
    # def test_006(self):
    #     SiteMenuLink = self.driver.find_elements_by_id('lnk_pc-megamenu_SiteMenuLink')
    #     SiteMenuLink[3].click()
    #     for handle in self.driver.window_handles:
    #         window_after = self.driver.window_handles[1]
    #         self.driver.switch_to.window(window_after)
    #     self.assertEqual(self.driver.current_url, 'https://www.cathaybk.com.tw/cathaybk/csr/index.html')
    # def test_007(self):
    #     SiteMenuLink = self.driver.find_elements_by_id('lnk_pc-megamenu_SiteMenuLink')
    #     SiteMenuLink[4].click()
    #     for handle in self.driver.window_handles:
    #         window_after = self.driver.window_handles[1]
    #         self.driver.switch_to.window(window_after)
    #     self.assertEqual(self.driver.current_url, 'https://recruit.cathaybk.com.tw/CathaybkHR/servlet/HttpDispatcher/EZA0_0000/index')
    # def test_008(self):
    #     SiteMenuLink = self.driver.find_elements_by_id('lnk_pc-megamenu_SiteMenuLink')
    #     SiteMenuLink[5].click()
    #     self.assertEqual(self.driver.current_url, 'https://www.cathaybk.com.tw/en-us/cathaybk/english/about-us/about-us/company-history/')

    #LV01MenuLink
    def test_009(self):
        LV01MenuLink = self.driver.find_elements_by_id('lnk_pc-megamenu_LV01MenuLink')
        LV01MenuLink[0].click()
        self.assertEqual(self.driver.current_url, 'https://www.cathaybk.com.tw/cathaybk/personal/credit-card/')






if __name__ == '__main__':
    unittest.main()