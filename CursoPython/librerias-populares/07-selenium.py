# pipenv install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True) #para que no cierra la ventana tras la prueba

browser = webdriver.Chrome(options=options)
browser.implicitly_wait(time_to_wait=10) #esperar 10 segundos a que termine de cargar la pagina
browser.get("https://github.com")
link = browser.find_element(By.LINK_TEXT, "Sign in") #buscar un elemento con ese texto
link.click()

user_input = browser.find_element(By.ID, "login_field")
pass_input = browser.find_element(By.ID, "password")

user_input.send_keys("hola mundo")
pass_input.send_keys("contraseña")
pass_input.send_keys(Keys.RETURN)

#validamos si ha llegado mirando el nombre 
profile = browser.find_element(By.CLASS_NAME, "css-truncate.css-truncate-target.ml-1")

label = profile.get_attribute("innerHTML")
print(label)

assert "usuario" in label #test que da error si no funciona

browser.quit()
