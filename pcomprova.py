#importando bibliotecas

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import openpyxl

#criando planilha para adicionar resultados

planilha = openpyxl.Workbook()

planilha.create_sheet("Planilha de Resultados", 0)

adiciona_planilha = planilha['Planilha de Resultados']

adiciona_planilha.append(['Data', 'Título', 'Link'])

planilha.save("Planilha de Resultados.xlsx")



