import pywhatkit as kit
import datetime

# Defina o número de telefone e o horário desejado
numero_whatsapp = "+5592981812027"  # Substitua pelo número desejado
hora_envio = datetime.time(21, 45)  # Hora em que deseja enviar (no exemplo, 10:00)

# Envie a imagem
kit.sendwhats_image(numero_whatsapp, "D:\CROL\Python\MEUSPROJETOS\envia_whatsapp\img\crol_foto.jpeg", "teste de envio no whatsapp")
# "caminho/para/sua/imagem.jpg"

print("Imagem enviada com sucesso!")

