# `🎮 SenseCalculator`

Um conversor de sensibilidade de rato (mouse sensitivity) para terminal, otimizado para a transição entre o Counter-Strike 2 e o Rainbow Six Siege. 

Desenvolvido em Python, este script não se limita a calcular os graus de rotação puros (360º/cm). Ele tem em consideração o **FOV (Field of View)** e o **Aspect Ratio**, devolvendo uma *Sense Percebida* exata para manter a tua memória muscular visual intacta.

## ✨ Funcionalidades

* **Conversão Bidirecional:** De CS2 para R6S e vice-versa.
* **Cálculo de Barras In-Game:** Devolve o valor exato para colocares nas barras de configuração do Siege (escala 1-100).
* **Ajuste de FOV e Aspect Ratio:** Suporta inputs flexíveis (ex: `16:9`, `4:3`, `1920x1080`) e calcula a diferença de escala focal (0% Monitor Distance).
* **Interface Colorida no Terminal:** Feedback visual limpo e rápido através de códigos ANSI nativos, com uma pequena animação de cálculo.

## 🚀 Como Usar

### Pré-requisitos
Apenas precisas de ter o [Python 3](https://www.python.org/downloads/) instalado no teu sistema. Não são necessárias bibliotecas externas.

### Execução
1. Clona este repositório:
   ```bash
   git clone [https://github.com/icsousa/SenseCalculator.git](https://github.com/icsousa/SenseCalculator.git)
   ```
2. Navega para a pasta do projeto:
   ```bash
   cd SenseCalculator
   ```
3. Corre o script:
   ```bash
   python src.py
   ```

### Exemplo de Utilização

O terminal irá fazer-te uma série de perguntas rápidas. Podes responder com números decimais usando pontos ou vírgulas.

```text
Jogo de origem: cs2
A tua sense no CS2: 1.5
Aspect Ratio ou Resolução no CS2 [ex: 16:9 ou 1920x1080]: 4:3

Jogo de destino: r6s
O teu FOV no R6S [ex: 88]: 84
Aspect Ratio ou Resolução no R6S [ex: 4:3 ou 1280x960]: 16:9
```

O script irá processar a matemática e devolver algo como:
- O valor decimal exato da conversão.
- O valor inteiro recomendado para as barras do R6S.
- A **Sense Percebida** ajustada (Ajuste Visual), caso alteres a proporção de ecrã ou o FOV.

## 🧠 A Matemática por trás (Focal Length Scaling)

Quando mudas de um rácio de 4:3 para 16:9, os modelos e o cenário deixam de estar esticados na horizontal. Embora a distância no teu tapete de rato para dar um 360º seja a mesma, o teu cérebro vai sentir a câmara mais "lenta" ou mais "rápida". 

Este script utiliza as tangentes dos teus ângulos de visão para calcular a escala focal exata, garantindo que a velocidade percebida percorrida pelo rato entre o centro do teu monitor e o alvo permanece visualmente idêntica, independentemente da resolução.

---
*Desenvolvido para garantir que não falhas aquele flick por causa do motor do jogo.*
