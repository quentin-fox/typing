from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

TARGET_WPM = 150


def wpm_to_sleep(wpm):
    # 5 letters counts as one word
    seconds_per_letter = 1 / (wpm * 5 / 60)
    return seconds_per_letter


class Wpm:

    def __init__(self, wpm):
        self.delay = wpm_to_sleep(wpm)
        self.driver = webdriver.Firefox()
        self.driver.get('https://typing-speed-test.aoeu.eu')

    def get_current_word(self):
        try:
            cw = self.driver.find_element_by_id('currentword').text
        except NoSuchElementException:
            cw = ''
        return cw

    def letter_gen(self, word):
        for letter in word:
            yield letter
        yield ' '

    def type(self):
        textinput = self.driver.find_element_by_id('input')
        cw = self.get_current_word()

        while cw != '':
            gen = self.letter_gen(cw)
            for letter in gen:
                textinput.send_keys(letter)
                time.sleep(self.delay)

            cw = self.get_current_word()


if __name__ == '__main__':
    w = Wpm(TARGET_WPM)
    time.sleep(3)
