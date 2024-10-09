import os
import shutil

# Caminho da pasta de origem e destino
pasta_origem = r"d:\cftv"
pasta_destino = r"C:\caminho\para\nova_pasta"

# Lista todos os arquivos na pasta de origem
for nome_arquivo in os.listdir(pasta_origem):
    caminho_arquivo_origem = os.path.join(pasta_origem, nome_arquivo)
    caminho_arquivo_destino = os.path.join(pasta_destino, nome_arquivo)

    # Copia o arquivo para a pasta de destino
    shutil.copy(caminho_arquivo_origem, caminho_arquivo_destino)
    print(f"Arquivo {nome_arquivo} copiado para {pasta_destino}")
