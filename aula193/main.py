# Selenium - Automatizando tarefas no navegador

# Chrome Options
# https://peter.sh/experiments/chromium-command-line-switches/
# Doc Selenium
# https://selenium-python.readthedocs.io/locating-elements.html

import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# Caminho para a raiz do projeto
ROOT_FOLDER = Path(__file__).parent
# Caminho para a pasta onde o chromedriver está
CHROMEDDRIVER_EXEC = ROOT_FOLDER / 'drivers' / 'chromedriver.exe'


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    # Classe utilizada para passar as opições do chromedriver
    chrome_options = webdriver.ChromeOptions()

    # chrome_options.add_argument('--headless')
    if options is not None:
        for option in options:
            chrome_options.add_argument(option) # Metodo que adiciona argumentos a classe Options

    # Classe utilizada utilizada para iniciar e parar o chromedriver
    chrome_service = Service(executable_path=str(CHROMEDDRIVER_EXEC))

    # Classe que cria uma instancia do chromedriver, que basicamente cria uma instancia do navegador
    chrome_browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options,
    )

    return chrome_browser


if __name__ == '__main__':
    TIME_TO_WAIT = 10
    # Example
    # options = '--headless', '--disable-gpu'
    # options = ('--disable-gpu', '--no-sandbox')
    options = ()
    browser = make_chrome_browser(*options)

    # Como antes função que carrega/abre uma pagina web na sessao atual do navegador
    browser.get('https://www.google.com')

    # Espere para encontrar o input
    # A classe WebDriverWait finaliza a instancia do browser em segundos
    # O metodo until(até) chama o metodo passado como argumento ate o valor retornado não ser falso
    # O metodo presence_of_element_located é o metodo que fica sendo chamado pelo untill e ele só é executado quando o elemento passado estiver presente no DOM da pagina, que nesse caso é um input com o Name= 'q'
    # Classe By é utilizada para pegar algum dos verificadores dos elementos HTML como NAME, ID, CLASS_NAME, etc...
    search_input = WebDriverWait(browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located(
            (By.NAME, 'q')
        )
    )

    '''Então basicamente essa parte acima abre o browser depois de aberto ele ESPERA(WebDriverWait) ATÉ(until) a CONDIÇÃO PASSADA FOR VERDADEIRA(EC.presence_of_element_located)'''

    # Se o input for encontrado vai escrever 'Hello World' no input, entao basicamente essa classe seleciona teclas
    search_input.send_keys('Hello World!')
    search_input.send_keys(Keys.ENTER)

    results = browser.find_element(By.ID, 'search') # Metodo para procucarar um elemento
    links = results.find_elements(By.TAG_NAME, 'a')
    # print(results)
    # print(links[0])
    links[0].click() # metodo utilizado para clicar em um elemento da pagina web

    # Dorme por 10 segundos
    time.sleep(TIME_TO_WAIT)