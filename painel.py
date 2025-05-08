lllllllllllllll, llllllllllllllI, lllllllllllllIl, lllllllllllllII, llllllllllllIll, llllllllllllIlI, llllllllllllIIl = input, int, Exception, exit, bool, print, open

from json import load as IlIlIllIlIIIll
from platform import machine as lIlIIIIllIIlll, version as IIIlIlIIIIIlll, system as lIlIlIIlllIIIl
from os import geteuid as lIllIIllIlIIll, remove as IlIIIIlIIIIlll, walk as lllIlIIllllIll, system as IIIllIIIIlIIll
from os.path import join as IlllIllIlIIlIl, getsize as IIllIlIlIllIlI
from datetime import datetime as lIlIIIlllllllI, timedelta as llllIIlIIIlIII

def IlllllIIIllIlIIIlI():
    try:
        with llllllllllllIIl('keys.json', 'r') as IlIllllllIllIIIIll:
            return IlIlIllIlIIIll(IlIllllllIllIIIIll)
    except lllllllllllllIl as IlllIIlIllllIllIII:
        llllllllllllIlI(f'Erro ao carregar keys: {IlllIIlIllllIllIII}')
        return {}

def lIlllllIIlIIIllIIl(llllIlllIIlIllllII):
    IIllIIIlIlIlIIllII = IlllllIIIllIlIIIlI()
    if llllIlllIIlIllllII not in IIllIIIlIlIlIIllII:
        return llllllllllllIll(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 0)
    lIlIlIllIIIIIllIII = IIllIIIlIlIlIIllII[llllIlllIIlIllllII]['ativado_em']
    IlIllllllIlIIIIIlI = IIllIIIlIlIlIIllII[llllIlllIIlIllllII]['tipo']
    if IlIllllllIlIIIIIlI == '7d' and (lIlIIIlllllllI.now() - lIlIIIlllllllI.strptime(lIlIlIllIIIIIllIII, '%Y-%m-%d')).days > 7:
        return llllllllllllIll(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 0)
    elif IlIllllllIlIIIIIlI == '30d' and (lIlIIIlllllllI.now() - lIlIIIlllllllI.strptime(lIlIlIllIIIIIllIII, '%Y-%m-%d')).days > 30:
        return llllllllllllIll(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 0)
    elif IlIllllllIlIIIIIlI == 'inf':
        return llllllllllllIll(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1)
    return llllllllllllIll(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 0)

def IlIIllllllIIIlIlIl():
    lIllIlIIIIIlIIIllI = IIIllIIIIlIIll()
    IllIIllllIlIIllllI = IIIlIlIIIIIlll()
    IlllIllIllIIIIlllI = lIlIIIIllIIlll()
    return (lIllIlIIIIIlIIIllI, IllIIllllIlIIllllI, IlllIllIllIIIIlllI)

def IllIIlllIIIlIIlIll():
    IIIllIIIIlIIll('clear')
    llllllllllllIlI("\n _   __  __                 ____          _______             _\n| | |  \\/  |               / __ \\        |__   __|           (_)\n| | | \\  / |  __ _ __  __ | |  | | _ __     | |    _ __ ___   _  ____  ___  _ __\n| | | |\\/| | / _` |\\ \\/ / | |  | || '_ \\    | |   | '_ ` _ \\ | ||_  / / _ \\| '__|\n|_| | |  | || (_| | >  <  | |__| || |_) |   | |   | | | | | || | / / |  __/| |\n(_) |_|  |_| \\__,_|/_/\\_\\  \\____/ | .__/    |_|   |_| |_| |_||_|/___| \\___||_|\n                                  | |\n                                  |_|\n    ")
    (lIllIlIIIIIlIIIllI, IllIIllllIlIIllllI, IlllIllIllIIIIlllI) = IlIIllllllIIIlIlIl()
    llllllllllllIlI(f'\nSeu Dispositivo: {IlllIllIllIIIIlllI}')
    llllllllllllIlI(f'Versão do Sistema: {lIllIlIIIIIlIIIllI} {IllIIllllIlIIllllI}')
    llllllllllllIlI(f"Root: {('Sim' if lIllIIllIlIIll() == 0 else 'Não')}\n")
    llllllllllllIlI('1. Desempenhar Bateria')
    llllllllllllIlI('2. Desempenhar Fps')
    llllllllllllIlI('3. Dns Free')
    llllllllllllIlI('4. Exit Lag')
    llllllllllllIlI('5. Apagar Arquivos')
    IIIlIIIllllIIIllIl = lllllllllllllll('Escolha uma opção: ')
    if IIIlIIIllllIIIllIl == '1':
        llIlllllIlIllIIIII()
    elif IIIlIIIllllIIIllIl == '2':
        lllIIlIIIIIIIlIlll()
    elif IIIlIIIllllIIIllIl == '3':
        IIIlIlIIIIIIlIIlll()
    elif IIIlIIIllllIIIllIl == '4':
        IIIlIIlIlIIllIllII()
    elif IIIlIIIllllIIIllIl == '5':
        IIIlIllllllllIlIll()
    else:
        llllllllllllIlI('Opção inválida!')

def llIlllllIlIllIIIII():
    llllllllllllIlI('Otimização da Bateria em andamento...')
    IIIllIIIIlIIll('echo 1 > /sys/class/power_supply/battery/charge_control_limit')
    llllllllllllIlI('Modo de bateria otimizado!')

def lllIIlIIIIIIIlIlll():
    llllllllllllIlI('Otimização do Fps em andamento...')
    IIIllIIIIlIIll('echo performance > /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor')
    llllllllllllIlI('FPS otimizado!')

def IIIlIlIIIIIIlIIlll():
    llllllllllllIlI('Configurando DNS Free...')
    IIIllIIIIlIIll("echo 'nameserver 8.8.8.8' > /etc/resolv.conf")
    llllllllllllIlI('DNS configurado para Google DNS (8.8.8.8)!')

def IIIlIIlIlIIllIllII():
    llllllllllllIlI('Reduzindo o Lag...')
    IIIllIIIIlIIll('settings put global transition_animation_scale 0')
    IIIllIIIIlIIll('settings put global animator_duration_scale 0')
    IIIllIIIIlIIll('settings put global window_animation_scale 0')
    llllllllllllIlI('Lag otimizado!')

def IIIlIllllllllIlIll():
    llIlllIIllIIlIlllI = lllllllllllllll('Digite o tamanho mínimo para apagar arquivos (em MB): ')
    lIIIllIIlIllIlIIIl = llllllllllllllI(llIlllIIllIIlIlllI) * 1024 * 1024
    llllllllllllIlI(f'Apagando arquivos com tamanho mínimo de {llIlllIIllIIlIlllI}MB...')
    for (llIlllIllllIlIllII, IlIlIlIlllIlllllII, IlIIlllllIllIIIllI) in lllIlIIllllIll('/'):
        for IIlIIlIIIIlllllIIl in IlIIlllllIllIIIllI:
            lllIlIllIIllIIIlII = IlllIllIlIIlIl(llIlllIllllIlIllII, IIlIIlIIIIlllllIIl)
            try:
                IlIIllIIIlIlIIIIlI = IIllIlIlIllIlI(lllIlIllIIllIIIlII)
                if IlIIllIIIlIlIIIIlI >= lIIIllIIlIllIlIIIl:
                    IlIIIIlIIIIlll(lllIlIllIIllIIIlII)
                    llllllllllllIlI(f'Arquivo {lllIlIllIIllIIIlII} apagado.')
            except lllllllllllllIl as IlllIIlIllllIllIII:
                pass

def IllllllIlllIlIlIII():
    llllllllllllIlI('\n\nCréditos:')
    llllllllllllIlI('Desenvolvido por Max OpTmizer')
    llllllllllllIlI('Agradecimentos ao GitHub e comunidade Python!')
    llllllllllllIlI('E ao Python.org pela incrível biblioteca!')
    llllllllllllIlI('Versão 1.0 - 2025')
llllIlllIIlIllllII = lllllllllllllll('Digite sua key: ')
if lIlllllIIlIIIllIIl(llllIlllIIlIllllII):
    IllIIlllIIIlIIlIll()
else:
    llllllllllllIlI('Key inválida ou expirada!')
    lllllllllllllII()
IllllllIlllIlIlIII()
