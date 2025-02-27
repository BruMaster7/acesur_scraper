import json
import re

import concurrent.futures
import requests

from .equivalencia_scraper import EquivalenciaScraper
from .scraper_base import ScraperBase
from repuesto import Repuesto
from equivalencia import Equivalencia


class RepuestoScraper(ScraperBase):
    PRODUCT_BASE_URL = "http://www.acesur.com.uy/"

    def __init__(self, base_url):
        super().__init__(base_url)
        self.session = requests.Session()  # Usamos una sesión persistente

    def get_product_links(self, page):
        """Obtiene los enlaces de los productos en una página dada."""
        soup = self.get_soup(f"{self.base_url}{page}")
        if not soup:
            return []

        return [
            product.find("a", class_="product-link")["href"]
            for product in soup.find_all("div", class_="product")
            if product.find("a", class_="product-link") and product.find("a", class_="product-link")["href"]
        ]

    def scrape_product(self, url):
        """Scrapea los detalles de un producto desde su página individual."""
        soup = self.get_soup(url)
        if not soup:
            return None, None

        try:
            nombre = soup.find("h1", class_="title").text.strip()
            codigo = ""
            details_list = soup.find("ul", id="productDetailsList")
            if details_list:
                for li in details_list.find_all("li"):
                    if "Código:" in li.text:
                        codigo = li.text.replace("Código:", "").strip()
                        break

            precio = 0.0
            price_div = soup.find("div", class_="single_price")
            if price_div:
                precio_text = price_div.text.replace("$", "").replace(",", "").strip()
                precio = float(precio_text)

            tipo = ""
            breadcrumb = soup.find("div", id="navBreadCrumb")
            if breadcrumb:
                breadcrumb_items = breadcrumb.find_all("li")
                if len(breadcrumb_items) > 2:
                    tipo = breadcrumb_items[-2].text.strip()

            descripcion = ""
            desc_div = soup.find("div", id="description")
            if desc_div and desc_div.find("p"):
                descripcion = desc_div.find("p").text.strip()

            marca = ""
            for li in details_list.find_all("li") if details_list else []:
                if "Fabricado en:" in li.text:
                    marca = li.text.replace("Fabricado en:", "").strip()
                    break

            if not marca:
                match = re.search(r"MARCA:\s*([^\n]+)", descripcion, re.IGNORECASE)
                if match:
                    marca = match.group(1).strip()

            imagen_url = ""
            zoom_link = soup.find("a", id="zoom01")
            if zoom_link and "href" in zoom_link.attrs:
                imagen_url = self.PRODUCT_BASE_URL + zoom_link["href"]
            else:
                noscript_tag = soup.find("noscript")
                if noscript_tag:
                    img_tag = noscript_tag.find("img")
                    if img_tag and "src" in img_tag.attrs:
                        imagen_url = self.PRODUCT_BASE_URL + img_tag["src"]

            equivalencia_scraper = EquivalenciaScraper(soup)
            equivalencias = equivalencia_scraper.get_equivalencias()

            repuesto = Repuesto(codigo, nombre, descripcion, marca, tipo, precio, stock=0, ubicacion="", imagen_path=imagen_url)
            equivalencia = Equivalencia(codigo, equivalencias)

            return repuesto.to_json(), equivalencia.to_json()

        except AttributeError:
            print(f"⚠️ Error extrayendo datos de: {url}")
            return None, None

    def scrape_all(self, max_pages=3, max_workers=24):
        """Scrapea múltiples páginas en paralelo y guarda los datos en JSON."""
        all_repuestos = []
        all_equivalencias = []

        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = []

            for page in range(1, max_pages + 1):
                print(f"📄 Scrapeando página {page}...")
                product_links = self.get_product_links(page)

                for link in product_links:
                    full_url = self.PRODUCT_BASE_URL + link
                    futures.append(executor.submit(self.scrape_product, full_url))

            for future in concurrent.futures.as_completed(futures):
                repuesto, equivalencia = future.result()
                if repuesto:
                    all_repuestos.append(repuesto)
                if equivalencia:
                    all_equivalencias.append(equivalencia)

        with open("repuestos.json", "w", encoding="utf-8") as f:
            json.dump(all_repuestos, f, indent=4, ensure_ascii=False)

        with open("equivalencias.json", "w", encoding="utf-8") as f:
            json.dump(all_equivalencias, f, indent=4, ensure_ascii=False)

        print("✅ Datos guardados en 'repuestos.json'.")
        print("✅ Datos guardados en 'equivalencias.json'.")


    

        
    
        
