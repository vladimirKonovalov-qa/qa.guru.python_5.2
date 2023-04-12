from selene.support.shared import browser
from selene import be, have


def test_search(browser_size):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_search_without_result(browser_size):
    browser.element('[name="q"]').should(be.blank).type('fjkfdsjk').press_enter()
    browser.element('[id="cnt"]').should(have.text('По запросу fjkfdsjk ничего не найдено.'))
    print('По данному запросу ничего не найдено')