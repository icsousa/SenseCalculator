import sys
import math
import time

# Códigos ANSI para as cores no terminal
class Cor:
    AZUL = '\033[94m'
    CYAN = '\033[96m'
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    VERMELHO = '\033[91m'
    MAGENTA = '\033[95m'
    NEGRITO = '\033[1m'
    RESET = '\033[0m'

def animacao_calculo():
    """Animação simples de 'A calcular' na mesma linha"""
    caracteres = ['|', '/', '-', '\\']
    for _ in range(3):
        for char in caracteres:
            sys.stdout.write(f"\r{Cor.AMARELO}A calcular a tua sense perfeita... {char}{Cor.RESET}")
            sys.stdout.flush()
            time.sleep(0.1)
    # Limpar a linha da animação
    sys.stdout.write("\r" + " " * 40 + "\r")
    sys.stdout.flush()

def processar_aspect_ratio(input_str):
    input_str = input_str.lower().strip()
    try:
        if ':' in input_str:
            largura, altura = map(float, input_str.split(':'))
        elif 'x' in input_str:
            largura, altura = map(float, input_str.split('x'))
        else:
            return 16 / 9
        return largura / altura
    except ValueError:
        return 16 / 9

def principal():
    print(f"{Cor.MAGENTA}{Cor.NEGRITO}" + "\n")
    print("🎮 Sense Calculator")
    print("\n")
    
    # Adicionado o minecraft e mine aos jogos válidos
    jogos_validos = ['cs2', 'r6s', 'minecraft', 'mine']
    
    # 1. JOGO DE ORIGEM
    origem = input(f"{Cor.CYAN}Jogo de origem: {Cor.RESET}").strip().lower()
    if origem not in jogos_validos:
        print(f"{Cor.VERMELHO}Erro: Jogo não reconhecido. Escolhe 'cs2', 'r6s' ou 'minecraft'.{Cor.RESET}")
        sys.exit(1)
        
    if origem == 'mine':
        origem = 'minecraft'

    try:
        if origem == 'r6s':
            sense_origem = float(input(f"{Cor.CYAN}A tua sense no R6S (valor das barras 1-100): {Cor.RESET}").replace(',', '.'))
        elif origem == 'minecraft':
            sense_origem = float(input(f"{Cor.CYAN}A tua sense no Minecraft (valor do options.txt ou ex: 0.21 para 21%): {Cor.RESET}").replace(',', '.'))
        else:
            sense_origem = float(input(f"{Cor.CYAN}A tua sense no CS2: {Cor.RESET}").replace(',', '.'))
    except ValueError:
        print(f"{Cor.VERMELHO}Erro: Insere um número válido.{Cor.RESET}")
        sys.exit(1)

    # Determinar FOV e Aspect Ratio da Origem
    if origem == 'cs2':
        fov_origem = 73.739795
        print(f"{Cor.AZUL}-> Info: FOV do CS2 bloqueado a ~73.74 graus.{Cor.RESET}")
    elif origem == 'minecraft':
        try:
            fov_origem = float(input(f"{Cor.CYAN}O teu FOV no MINECRAFT {Cor.AMARELO}[ex: 70 a 110]{Cor.CYAN}: {Cor.RESET}").replace(',', '.'))
        except ValueError:
            fov_origem = 70.0
    else:
        try:
            fov_origem = float(input(f"{Cor.CYAN}O teu FOV no R6S {Cor.AMARELO}[ex: 88]{Cor.CYAN}: {Cor.RESET}").replace(',', '.'))
        except ValueError:
            fov_origem = 90.0

    ar_input_origem = input(f"{Cor.CYAN}Aspect Ratio ou Resolução no {origem.upper()} {Cor.AMARELO}[ex: 16:9 ou 1920x1080]{Cor.CYAN}: {Cor.RESET}")
    
    # 2. JOGO DE DESTINO
    print(f"\n{Cor.RESET}")
    destino = input(f"{Cor.CYAN}Jogo de destino: {Cor.RESET}").strip().lower()
    if destino not in jogos_validos:
        print(f"{Cor.VERMELHO}Erro: Jogo não reconhecido.{Cor.RESET}")
        sys.exit(1)
        
    if destino == 'mine':
        destino = 'minecraft'

    if destino == 'cs2':
        fov_destino = 73.739795
    elif destino == 'minecraft':
        try:
            fov_destino = float(input(f"{Cor.CYAN}O teu FOV no MINECRAFT {Cor.AMARELO}[ex: 70 a 110]{Cor.CYAN}: {Cor.RESET}").replace(',', '.'))
        except ValueError:
            fov_destino = 70.0
    else:
        try:
            fov_destino = float(input(f"{Cor.CYAN}O teu FOV no R6S {Cor.AMARELO}[ex: 88]{Cor.CYAN}: {Cor.RESET}").replace(',', '.'))
        except ValueError:
            fov_destino = 90.0

    ar_input_destino = input(f"{Cor.CYAN}Aspect Ratio ou Resolução no {destino.upper()} {Cor.AMARELO}[ex: 4:3 ou 1280x960]{Cor.CYAN}: {Cor.RESET}")

    # Acionar a pequena animação
    print("")
    animacao_calculo()

    # 3. MATEMÁTICA PURA DA ROTAÇÃO
    multiplicador_r6s = 3.839724
    
    # Converter para a base universal (CS2)
    if origem == 'cs2':
        sense_base_cs2 = sense_origem
    elif origem == 'r6s':
        sense_base_cs2 = sense_origem / multiplicador_r6s
    elif origem == 'minecraft':
        # Fórmula inversa: calcular a sense CS2 a partir da sense do Minecraft
        sense_base_cs2 = (1.2 * ((sense_origem * 0.6 + 0.2) ** 3)) / 0.022

    # Converter da base universal (CS2) para o Destino
    if destino == 'cs2':
        sense_destino_real = sense_base_cs2
    elif destino == 'r6s':
        sense_destino_real = sense_base_cs2 * multiplicador_r6s
    elif destino == 'minecraft':
        # Fórmula direta: calcular a sense do Minecraft a partir da sense do CS2
        valor_interno = (sense_base_cs2 * 0.022) / 1.2
        sense_destino_real = ((valor_interno ** (1/3)) - 0.2) / 0.6

    # 4. VELOCIDADE PERCEBIDA (FOV E ASPECT RATIO)
    ar_origem = processar_aspect_ratio(ar_input_origem)
    ar_destino = processar_aspect_ratio(ar_input_destino)
    
    tan_origem = math.tan(math.radians(fov_origem) / 2)
    tan_destino = math.tan(math.radians(fov_destino) / 2)
    
    ratio_fov = tan_destino / tan_origem
    ratio_aspect = ar_origem / ar_destino

    sense_percebida = sense_destino_real * ratio_fov * ratio_aspect

    # 5. MOSTRAR RESULTADOS
    print(f"{Cor.VERDE}{Cor.NEGRITO}")
    
    if destino == 'r6s':
        slider_int = round(sense_destino_real)
        print(f"-> Valor Decimal Exato: {Cor.AZUL}{sense_destino_real:.3f}{Cor.VERDE}")
        print(f"-> Barras In-Game (Horiz/Vert): {Cor.AMARELO}{slider_int}{Cor.VERDE} (escala 1-100)")
        
        if abs(fov_origem - fov_destino) > 0.1 or abs(ar_origem - ar_destino) > 0.01:
            print(f"-> Barras In-Game (Ajuste Visual): {Cor.AMARELO}{round(sense_percebida)}{Cor.VERDE} (escala 1-100){Cor.MAGENTA}")
            
    elif destino == 'minecraft':
        print(f"-> Valor Ficheiro (options.txt): {Cor.AZUL}{sense_destino_real:.5f}{Cor.VERDE}")
        print(f"-> Barra In-Game (Percentagem): {Cor.AMARELO}{round(sense_destino_real * 100)}%{Cor.VERDE}")
        
        if abs(fov_origem - fov_destino) > 0.1 or abs(ar_origem - ar_destino) > 0.01:
            print(f"-> Ajuste Visual (options.txt): {Cor.AMARELO}{sense_percebida:.5f}{Cor.VERDE}{Cor.MAGENTA}")
            
    else:
        print(f"-> Sense Pura: {Cor.AZUL}{sense_destino_real:.3f}{Cor.VERDE}")
        if abs(fov_origem - fov_destino) > 0.1 or abs(ar_origem - ar_destino) > 0.01:
            print(f"-> Sense Percebida (Fator Visual): {Cor.AMARELO}{sense_percebida:.3f}{Cor.MAGENTA}")

    print("\n")

if __name__ == "__main__":
    try:
        principal()
    except KeyboardInterrupt:
        print(f"\n{Cor.VERMELHO}Cancelado pelo utilizador.{Cor.RESET}")
        sys.exit(0)