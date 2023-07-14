class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.imlicitely_wait(timeout)

    def open(self):
        self.browser.get(self.url)