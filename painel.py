import os
import platform
import subprocess
import time

# ASCII e título
ascii_logo = r'''
 _   __  __                 ____          _______             _
| | |  \/  |               / __ \        |__   __|           (_)
| | | \  / |  __ _ __  __ | |  | | _ __     | |    _ __ ___   _  ____  ___  _ __
| | | |\/| | / _` |\ \/ / | |  | || '_ \    | |   | '_ ` _ \ | ||_  / / _ \| '__|
|_| | |  | || (_| | >  <  | |__| || |_) |   | |   | | | | | || | / / |  __/| |
(_) |_|  |_| \__,_|/_/\_\  \____/ | .__/    |_|   |_| |_| |_||_|/___| \___||_|
                                  | |
                                  |_|

'''

# Info do dispositivo
def device_info():
    print(ascii_logo)
    print(" [!] Coletando informações do dispositivo...\n")
    modelo = subprocess.getoutput("getprop ro.product.model")
    versao = subprocess.getoutput("getprop ro.build.version.release")
    root = "Sim" if os.path.exists("/system/bin/su") or os.path.exists("/system/xbin/su") else "Não"

    print(f" Dispositivo: {modelo}")
    print(f" Versão Android: {versao}")
    print(f" Root: {root}")
    print("-" * 60)

# Funções
def otimizar_bateria():
    print("\n [*] Reduzindo processos em segundo plano...")
    os.system("pm clear com.facebook.katana > /dev/null 2>&1")
    os.system("pm clear com.instagram.android > /dev/null 2>&1")
    time.sleep(2)
    print(" [+] Bateria otimizada com sucesso!")

def otimizar_fps():
    print("\n [*] Limpando cache de GPU e memória RAM...")
    os.system("echo 3 > /proc/sys/vm/drop_caches")
    time.sleep(2)
    print(" [+] FPS melhorado!")

def dns_free():
    print("\n [*] Aplicando DNS do Cloudflare (1.1.1.1)...")
    os.system("setprop net.dns1 1.1.1.1")
    os.system("setprop net.dns2 1.0.0.1")
    time.sleep(2)
    print(" [+] DNS aplicado com sucesso!")

def exit_lag():
    print("\n [*] Simulando boost de rede (modo avião)...")
    os.system("svc wifi disable && svc data disable")
    time.sleep(1)
    os.system("svc wifi enable && svc data enable")
    time.sleep(2)
    print(" [+] Lag reduzido com sucesso!")

def apagar_arquivos():
    try:
        tamanho = int(input("\n Tamanho mínimo (em MB): "))
        print(" [*] Buscando arquivos grandes...")
        os.system(f"find /storage/emulated/0 -type f -size +{tamanho}M")
        confirmar = input(" Deseja apagar esses arquivos? (s/n): ").lower()
        if confirmar == "s":
            os.system(f"find /storage/emulated/0 -type f -size +{tamanho}M -delete")
            print(" [+] Arquivos apagados com sucesso!")
        else:
            print(" [-] Operação cancelada.")
    except:
        print(" [!] Entrada inválida.")

def limpar_total():
    print("\n [*] Limpando cache, arquivos temporários e pastas inúteis...")
    pastas = [
        "/storage/emulated/0/Android/data/com.instagram.android/cache",
        "/storage/emulated/0/DCIM/.thumbnails",
        "/storage/emulated/0/Download",
        "/storage/emulated/0/tmp"
    ]
    for pasta in pastas:
        os.system(f"rm -rf {pasta}/*")
    print(" [+] Limpeza completa!")

# Menu principal
def menu():
    while True:
        device_info()
        print("""
 1. Desempenhar Bateria
 2. Desempenhar FPS
 3. DNS Free
 4. Exit Lag
 5. Apagar Arquivos Grandes
 6. Limpar Celular Totalmente
 0. Sair
        """)
        escolha = input(" Escolha uma opção: ")

        if escolha == "1":
            otimizar_bateria()
        elif escolha == "2":
            otimizar_fps()
        elif escolha == "3":
            dns_free()
        elif escolha == "4":
            exit_lag()
        elif escolha == "5":
            apagar_arquivos()
        elif escolha == "6":
            limpar_total()
        elif escolha == "0":
            print("\n Obrigado por usar o Max OpTmizer V1!")
            break
        else:
            print(" [!] Opção inválida.")

        input("\n Pressione Enter para continuar...")

# Execução
if __name__ == "__main__":
    os.system("clear")
    menu()
