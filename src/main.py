
from scrapers.repuestos_scraper import RepuestoScraper


if __name__ == "__main__":
    scraper = RepuestoScraper("http://www.acesur.com.uy/index.php?main_page=products_all&disp_order=1&page=")
    scraper.scrape_all(max_pages=1)