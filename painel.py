import json
import os
import platform
import subprocess
import psutil
from datetime import datetime, timedelta

# Função para carregar as keys
def carregar_keys():
    try:
        with open("keys.json", "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"Erro ao carregar keys: {e}")
        return {}

# Função para verificar se a key é válida
def verificar_key(key):
    keys = carregar_keys()

    if key not in keys:
        return False
    
    data_ativacao = keys[key]['ativado_em']
    tipo = keys[key]['tipo']

    # Verifica validade da key
    if tipo == "7d" and (datetime.now() - datetime.strptime(data_ativacao, "%Y-%m-%d")).days > 7:
        return False
    elif tipo == "30d" and (datetime.now() - datetime.strptime(data_ativacao, "%Y-%m-%d")).days > 30:
        return False
    elif tipo == "inf":
        return True

    return False

# Função para obter informações do dispositivo
def obter_info_dispositivo():
    sistema = platform.system()
    versao = platform.version()
    dispositivo = platform.machine()
    return sistema, versao, dispositivo

# Função para gerar um painel com arte ASCII
def painel():
    os.system("clear")
    
    # Arte ASCII
    print("""
 _   __  __                 ____          _______             _
| | |  \/  |               / __ \        |__   __|           (_)
| | | \  / |  __ _ __  __ | |  | | _ __     | |    _ __ ___   _  ____  ___  _ __
| | | |\/| | / _` |\ \/ / | |  | || '_ \    | |   | '_ ` _ \ | ||_  / / _ \| '__|
|_| | |  | || (_| | >  <  | |__| || |_) |   | |   | | | | | || | / / |  __/| |
(_) |_|  |_| \__,_|/_/\_\  \____/ | .__/    |_|   |_| |_| |_||_|/___| \___||_|
                                  | |
                                  |_|
    """)
    
    # Informações do dispositivo
    sistema, versao, dispositivo = obter_info_dispositivo()
    print(f"\nSeu Dispositivo: {dispositivo}")
    print(f"Versão do Sistema: {sistema} {versao}")
    print(f"Root: {'Sim' if os.geteuid() == 0 else 'Não'}\n")
    
    # Menu de opções
    print("1. Desempenhar Bateria")
    print("2. Desempenhar Fps")
    print("3. Dns Free")
    print("4. Exit Lag")
    print("5. Apagar Arquivos")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        otimizar_bateria()
    elif opcao == "2":
        otimizar_fps()
    elif opcao == "3":
        configurar_dns()
    elif opcao == "4":
        exit_lag()
    elif opcao == "5":
        apagar_arquivos()
    else:
        print("Opção inválida!")

# Função para otimizar a bateria
def otimizar_bateria():
    print("Otimização da Bateria em andamento...")
    # Exemplo de otimização para dispositivos Android (necessário root)
    os.system("echo 1 > /sys/class/power_supply/battery/charge_control_limit")
    print("Modo de bateria otimizado!")

# Função para otimizar FPS
def otimizar_fps():
    print("Otimização do Fps em andamento...")
    # Exemplo de FPS boost - habilitar modo de alto desempenho
    # Para dispositivos Android (usando root)
    os.system("echo performance > /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor")
    print("FPS otimizado!")

# Função para configurar o DNS (utilizando DNS público do Google)
def configurar_dns():
    print("Configurando DNS Free...")
    # Exemplo de alteração de DNS para o DNS público do Google
    os.system("echo 'nameserver 8.8.8.8' > /etc/resolv.conf")
    print("DNS configurado para Google DNS (8.8.8.8)!")

# Função para otimizar o lag (Exemplo simples de melhoria)
def exit_lag():
    print("Reduzindo o Lag...")
    # Desativando animações e otimizações simples
    os.system("settings put global transition_animation_scale 0")
    os.system("settings put global animator_duration_scale 0")
    os.system("settings put global window_animation_scale 0")
    print("Lag otimizado!")

# Função para apagar arquivos antigos
def apagar_arquivos():
    tamanho_min = input("Digite o tamanho mínimo para apagar arquivos (em MB): ")
    tamanho_min_bytes = int(tamanho_min) * 1024 * 1024  # Convertendo MB para bytes
    print(f"Apagando arquivos com tamanho mínimo de {tamanho_min}MB...")
    
    # Encontrando e apagando arquivos grandes
    for root, dirs, files in os.walk("/"):
        for file in files:
            caminho_arquivo = os.path.join(root, file)
            try:
                tamanho = os.path.getsize(caminho_arquivo)
                if tamanho >= tamanho_min_bytes:
                    os.remove(caminho_arquivo)
                    print(f"Arquivo {caminho_arquivo} apagado.")
            except Exception as e:
                pass

# Função para exibir os créditos
def exibir_creditos():
    print("\n\nCréditos:")
    print("Desenvolvido por Max OpTmizer")
    print("Agradecimentos ao GitHub e comunidade Python!")
    print("E ao Python.org pela incrível biblioteca!")
    print("Versão 1.0 - 2025")

# Entrada da key
key = input("Digite sua key: ")

# Verificando se a key é válida
if verificar_key(key):
    painel()
else:
    print("Key inválida ou expirada!")
    exit()

# Exibir créditos ao final
exibir_creditos()
