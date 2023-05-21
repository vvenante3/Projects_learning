from selenium import webdriver
from selenium.common.exceptions import WebDriverException, ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import re
import time
import pandas as pd

class ScraperVivaReal:
    wait_time = 5

    def __init__(self, url):
        # Initializing the webdriver (Inicializando o webdriver)

        servico = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=servico)
        self.driver.maximize_window()
        self.driver.get(url)
        time.sleep(self.wait_time)

        # Handling cookies acception (Lidando com a aceitação de cookies)
        WebDriverWait(self.driver, self.wait_time).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="cookie-notifier-cta"]'))).click()
        time.sleep(self.wait_time/2)

    def __scrape_page__(self):
        result = []

        # Extracting data from the page (Extraindo dados da página)
        try:
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        except WebDriverException:
            print('Webdriver was manually quit by the user!') # I configure this exception before adding the option -headless to webdriver
            # Eu configuro esta exceção antes de adicionar a opção -headless ao webdriver
            return result

        # Finding property cards containing search results
        # Encontrar cartões de propriedade contendo resultados de pesquisa
        div_list = soup.find_all('div', {'class':'property-card__content'})

        # Iterating each card
        # Iterando cada cartão
        for d in div_list:

            # Extracting info from card
            # Extraindo informações do cartão
            title = d.find('span', {'class': 'property-card__title js-cardLink js-card-title'}).get_text().strip()
            complete_address = d.find('span', {'class': 'property-card__address'}).get_text().strip()
            area = d.find('span', {'class': 'property-card__detail-value js-property-card-value property-card__detail-area js-property-card-detail-area'}).get_text().strip()
            rooms = d.find('li', {'class': 'property-card__detail-item property-card__detail-room js-property-detail-rooms'}).find('span', {'class': 'property-card__detail-value js-property-card-value'}).get_text().strip()
            baths = d.find('li', {'class': 'property-card__detail-item property-card__detail-bathroom js-property-detail-bathroom'}).find('span', {'class': 'property-card__detail-value js-property-card-value'}).get_text().strip()
            garage = d.find('li', {'class': 'property-card__detail-item property-card__detail-garage js-property-detail-garages'}).find('span', {'class': 'property-card__detail-value js-property-card-value'}).get_text().strip()

            # Extracting the price
            # Extraindo o preço
            try:
                price = d.find('div', {'class':'property-card__price js-property-card-prices js-property-card__price-small'}).find('p').get_text().strip()
            except AttributeError:
                price = "N/I"

            # Splitting the address
            # Dividindo o endereço
            add_list = re.split(',|-', complete_address)
            add_list = [ item.strip() for item in add_list ]

            address = 'N/I'
            number = 'N/I'
            
            if len(add_list) == 2:
                city, st = add_list
                neibhood = 'N/I'
                number = 'N/I'
            if len(add_list) == 3:
                neibhood, city, st = add_list
                number = 'N/I'
            if len(add_list) == 4:
                address, neibhood, city, st = add_list
                number = 'N/I'
            elif len(add_list) == 5:
                address, number, neibhood, city, st = add_list

            # Adding the result into a dicionary and appending the dict to a result list
            # Adicionar o resultado a um dicionário e anexar o dict a uma lista de resultados
            row = { 'Título': title, 'Endereço': address, 'Número': number, 'Bairro': neibhood, 'Cidade': city, 'Estado': st, 'Área': area, 'Quartos': rooms, 'Banheiros': baths, 'Vagas': garage, 'Preço': price }
            result.append(row)
        return result

    def __next_page__(self):
        # Finding the "Next Page" button element
        # Encontrando o elemento do botão "Próxima página"
        next_element = self.driver.find_element(By.XPATH, '//*[@id="js-site-main"]/div[2]/div[1]/section/div[2]/div[2]/div/ul/li[9]/button')


        try:
            # Trying to click it (Tentando clicar nele)
            next_element.click()
            time.sleep(self.wait_time)
            return True
        # Treating some exceptions (element not found and element not clickable)
        # Tratando algumas exceções (elemento não encontrado e elemento não clicável)
        except ElementClickInterceptedException:
            print('"Próxima Página" element is not clickable!')
        except NoSuchElementException:
            print('"Próxima Página" element not found!')
        return False

    def run(self, output):
        has_next = True
        final_result = []
        # Getting the information!
        # Obtendo as informações!
        while has_next:
            results = self.__scrape_page__()
            final_result.extend(results)
            print('Got {} results! Total Found: {}'.format(len(results), len(final_result)))
            if len(results) == 0:
                break
            has_next = self.__next_page__()
        # Quitting Chrome
        # Saindo do Chrome
        self.driver.quit()
        # Exporting results to CSV
        # Exportando resultados para CSV
        df = pd.DataFrame(final_result)
        df.to_csv(output, sep=',')

S = ScraperVivaReal('https://www.vivareal.com.br/venda/parana/curitiba/apartamento_residencial/?pagina=#onde=Brasil,Paran%C3%A1,Curitiba,,,,,,BR%3EParana%3ENULL%3ECuritiba,,,')
S.run('output.csv')