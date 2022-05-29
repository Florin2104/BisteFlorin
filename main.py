from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#Am descarcat chromedriver de pe internet ca sa putem accesa aplicatia google chrome
PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)
#Am accesat site-ul emag
driver.get("https://www.emag.ro/")

#Am folosit metoda click si find element by id/xpath, ca sa dam click pe site-urile chrome folosind Inspect element.
login = driver.find_element_by_id("my_account")
login.click()

#Am folosit metoda sleep ca sa dam timp la chrome sa intra pe pagina.

time.sleep(1)
login2 = driver.find_element_by_xpath("//html/body/div[1]/div[2]/div[2]/div[3]/a[2]")
login2.click()
username = driver.find_element_by_xpath("//*[@id='identifierId']")

#Am adaugat contul de test pe care l-am creat pentru acesst proiect
username.send_keys("testemag1771@gmail.com")
username.send_keys(Keys.RETURN)
time.sleep(2)
password = driver.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input")
password.send_keys("123Anaconda12")
password.send_keys(Keys.RETURN)

print("Logare reusita")
time.sleep(3)
security = driver.find_element_by_xpath('//*[@id="main-container"]/div[2]/div[2]/a[2]')
security.click()

time.sleep(3)

search = driver.find_element_by_id("searchboxTrigger")
search.send_keys("Laptop gaming")
search.send_keys(Keys.RETURN)
adauga = driver.find_element_by_xpath("//*[@id='card_grid']/div[1]/div/div/div[4]/div[2]/form/button")
adauga.click()
print("Adaugare reusita")

cos = driver.find_element_by_xpath("//*[@id='my_cart']/i")
cos.click()

time.sleep(3)
sterge = driver.find_element_by_xpath("//*[@id='vendorsContainer']/div/div[1]/div/div[2]/div[1]/div[3]/a[1]")
sterge.click()
print("Stergere reusita")
