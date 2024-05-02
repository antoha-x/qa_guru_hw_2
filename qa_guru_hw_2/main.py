from selene import browser, be, have


def test_google_should_find_selene():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_duck_duck_go_should_find_selene():
    browser.open('https://duckduckgo.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('.react-results--main').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_yandex_should_find_selene():
    browser.open('https://ya.ru')
    browser.element('[name="text"]').should(be.blank).type('yashaka\selene').press_enter()
    browser.element('[id="search-result"]').should(have.text('GitHub - yashaka/selene: User-oriented Web UI browser...'))


def test_google_should_no_find_selene():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.no.text('abra-cadabra'))
