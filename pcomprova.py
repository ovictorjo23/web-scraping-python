from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import openpyxl

# Criando Planilha

planilha = openpyxl.Workbook()

planilha.create_sheet('Planilha de Resultados', 0)

adicionar_na_planilha = planilha['Planilha de Resultados']

adicionar_na_planilha.append(['Data', 'Título', 'Link'])

# Filtrando informações

driver = ChromeDriverManager().install()

opcao = Options()
opcao.add_argument('--headless')

navegador = webdriver.Chrome(service=Service(driver), options=opcao)

navegador.get('https://projetocomprova.com.br/?filter=eleicoes')

for (data_publicacao, titulo_link) in zip(navegador.find_elements(by=By.XPATH, value='//span[@class="answer__credits__date "]'), navegador.find_elements(by=By.CLASS_NAME, value='answer__title__link')):
    print()
    print(data_publicacao.get_attribute("textContent"))
    print([titulo_link.text for titulo_link in navegador.find_elements(By.TAG_NAME, "h1")])    
    print(titulo_link.get_attribute('href'))

    #adicionar_na_planilha.append([data_publicacao.get_attribute("textContent"), [titulo_link.text for titulo_link in navegador.find_elements(By.TAG_NAME, "h1")], titulo_link.get_attribute('href')])


planilha.save('Planilha de Resultados.xlsx')
