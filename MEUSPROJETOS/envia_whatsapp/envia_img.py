from selenium import webdriver
import time

# Configurações
numero_whatsapp = "5592981812027"  # Substitua pelo número desejado
caminho_imagem = "D:\CROL\Python\MEUSPROJETOS\envia_whatsapp\img"

# Inicialize o navegador
driver = webdriver.Chrome(executable_path="caminho/para/chromedriver.exe")
driver.get("https://web.whatsapp.com/")

# Aguarde o usuário fazer o login escaneando o QR Code
input("Pressione Enter após fazer o login no WhatsApp Web...")

# Abra a conversa com o número desejado
driver.get(f"https://web.whatsapp.com/send?phone={numero_whatsapp}")

# Anexe a imagem
anexar = driver.find_element_by_xpath("//div[@title='Anexar']")
anexar.click()
imagem = driver.find_element_by_xpath("//input[@accept='image/*,video/mp4,video/3gpp,video/quicktime']")
imagem.send_keys(caminho_imagem)

# Aguarde um pouco para a imagem ser carregada
time.sleep(2)

# Clique no botão de envio
enviar = driver.find_element_by_xpath("//span[@data-icon='send']")
enviar.click()

print("Imagem enviada com sucesso!")

# Feche o navegador
driver.quit()
