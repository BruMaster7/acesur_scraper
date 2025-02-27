
from datetime import timedelta
import time

from scrapers.repuestos_scraper import RepuestoScraper



if __name__ == "__main__":
    start_time = time.time()
    
    scraper = RepuestoScraper("http://www.acesur.com.uy/index.php?main_page=products_all&disp_order=1&page=")
    scraper.scrape_all(max_pages=2)
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"⏱️ Tiempo total de ejecución: {timedelta(seconds=elapsed_time)}")
