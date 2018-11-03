import time


class MTPHelper:
    browser = None

    @staticmethod
    def open(address, trials=3, expire_time=120, timeout=600):
         MTPHelper.browser.set_page_load_timeout(timeout)
         trial = 1
         while trial <= trials:
             try:
                 start_time = time.time()
                 MTPHelper.browser.get(address)
                 stop_time = time.time()
                 load_time = round(stop_time - start_time, 2)
                 if load_time <= expire_time:
                     return "Service {} succesfully loaded in {}(s)".format(address, load_time)
             except:
                 trial += 1
    @staticmethod
    def type(selector, value):
        try:
            MTPHelper.browser.find_element_by_xpath(selector).send_keys(value)
        except:
            raise ValueError(selector + "can't be found!")

    @staticmethod
    def click(selector=None):
        try:
            MTPHelper.browser.find_element_by_css_selector(selector).click()
        except:
            raise ValueError(selector + "can't be found!")
