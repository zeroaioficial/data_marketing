#import pacotes
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from parsel import Selector
import csv

# arquivo csv
writer = csv.writer(open('output.csv', 'w', encoding='utf-8'))
writer.writerow(['Nome', 'Headline', 'URL'])

#chrome driver
driver = webdriver.Chrome(r"C:XXXXXXXXXX\chromedriver.exe")

#acessar o linkedin
driver.get("https://www.linkedin.com")
sleep(1)

#usuario
usuario_input = driver.find_element('name', 'session_key')
usuario_input.send_keys("XXXXXXX@XXXXXXX")

#senha
senha_input = driver.find_element('name', 'session_password')
senha_input.send_keys("XXXXXXXXX")

#clicar para logar
senha_input.send_keys(Keys.RETURN)
sleep(3)

#Google
driver.get("https://www.google.com")
sleep(1)

#selecionar o buscador
busca_input = driver.find_element('name', 'q')

#fazer a busca
busca_input.send_keys('site:linkedin.com/in AND "data scientist" AND "Criciúma"')
busca_input.send_keys(Keys.RETURN)
sleep(2)

#extrair lista de perfil
lista_perfil = driver.find_elements('xpath','//div[@class="yuRUbf"]/a')
lista_perfil = [perfil.get_attribute('href') for perfil in lista_perfil]

#extrair informações individuais
for perfil in lista_perfil:
    driver.get(perfil)
    sleep(4)

    response = Selector(text=driver.page_source)
    nome = response.xpath('//title/text()').extract_first().split(" | ")[0]
    headline = response.xpath('//div[@class="text-body-medium break-words"]//text()').extract()
    url_perfil = driver.current_url

    #escrever no arquivo csv
    writer.writerow([nome, headline, url_perfil])

#sair do driver
driver.quit() 
