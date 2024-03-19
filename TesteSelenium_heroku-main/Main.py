from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service(executable_path='C:\\Users\\LabInfo\\Downloads\\chromedriver-win32 (2)\\chromedriver-win32\\chromedriver.exe')
options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=service, options=options)
driver.get("https://cliente.americanas.com.br/minha-conta/entrar?next=https://www.americanas.com.br/")
try:
        email_login = driver.find_element(By.XPATH,'//*[@id="input-border"]/input')
        email_login.send_keys("gabrieltedescopires@gmail.com")
        print("0")
        print("1")
        senha_login = driver.find_element(By.XPATH,'//*[@id="input-border"]/input')
        senha_login.send_keys("Gtpz2006")
        btn_login = driver.find_element(By.XPATH,'//*[@id="root"]/main/div/div[2]/div/form/div[4]/button')
        btn_login.click()
        driver.implicitly_wait(5)  
       
    
        print("Todos os testes concluídos com sucesso!")

except:
    print("Teste Falhou! Erro na execução")

driver.quit()