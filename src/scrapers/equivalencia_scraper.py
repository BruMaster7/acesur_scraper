class EquivalenciaScraper:
    def __init__(self, soup):
        self.soup = soup

    def get_equivalencias(self):
        equivalencias = []
        description_div = self.soup.find("div", id="description")
        
        if description_div:
            table = description_div.find("table", class_="table")
            if table:
                for row in table.find_all("tr"):
                    td_elements = row.find_all("td")
                    if td_elements and len(td_elements) > 0:
                        codigo_equivalente = td_elements[0].get_text(strip=True)
                        equivalencias.append(codigo_equivalente)

        return equivalencias
