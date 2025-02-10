from pages.scraping_page import ScrapingPage

def test_scrape_books(browser):
    scraping_page=ScrapingPage(browser)
    scraping_page.open()

    books_data=scraping_page.scrape_books()

    scraping_page.save_to_csv(books_data,"books.csv")

    assert len(books_data)>0,"No books were scraped!"
