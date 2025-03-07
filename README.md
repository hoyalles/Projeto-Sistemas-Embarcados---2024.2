# 🎮 Jogo de Reflexos com Raspberry Pi e Simulação no Wokwi

## 📖 Sobre o Projeto
Este projeto foi desenvolvido para a disciplina de **Sistemas Embarcados** na **UFC - Campus Itapajé**, ministrada pelo professor **Juan Sebastian Toquica Arenas**.  
O jogo de reflexos testa a rapidez dos jogadores ao pressionar um botão assim que o LED acende. Foi implementado e testado tanto no **simulador Wokwi** quanto em hardware real com a **Raspberry Pi 4 Model B**.

## 🛠️ Funcionalidades
✅ **Jogo de Reflexos:** O LED acende após um tempo aleatório, e o primeiro jogador a apertar o botão vence.  
✅ **Versões para 2 e 4 jogadores:** O código foi expandido para permitir mais jogadores.  
✅ **Simulação no Wokwi:** Testes foram realizados antes da implementação no hardware real.  
✅ **Execução na Raspberry Pi:** Código adaptado para funcionamento com **GPIO físico**.  

## 🔗 Links para Simulações
- 🕹️ **Versão para 2 jogadores:** [Acesse no Wokwi](https://wokwi.com/projects/422864524911188993)  
- 🕹️ **Versão para 4 jogadores:** [Acesse no Wokwi](https://wokwi.com/projects/422172454337844225)  

## 🖥️ Tecnologias Utilizadas
### **Hardware**
-  **Placa:** Raspberry Pi 4 Model B  
-  **Botões:** 2 ou 4 push buttons  
-  **LED:** Indicação do início do jogo  
-  **Resistores:** Pull-down para estabilizar os botões  
-  **Alimentação:** Fonte 5V via USB-C  

### **Software**
-  **Linguagem:** Python 3  
-  **Bibliotecas:** gpiozero, time, random  
-  **IDE usada na Raspberry:** Thonny Python  

##  Como Rodar  
### **Simulação no Wokwi**  
1. Acesse um dos links acima para a versão desejada.  
2. Clique em "Run" e interaja com os botões.  

### **Execução na Raspberry Pi**  
1. Instale as dependências:  
   ```bash
   sudo apt update && sudo apt install python3-gpiozero -y

2. Clone este repositório e execute:** 
    ```bash
    git clone https://github.com/hoyalles/Projeto-Sistemas-Embarcados---2024.2.git
    cd GameFinal
    python3 test2.py

## 🔍 **Comparação: Simulação vs. Raspberry Pi**
<img src= "https://drive.google.com/uc?export=view&id=1D-OSJNk90hn1i_tQ1IO1ziDNJ9Ht2DcN" width="400">

## **📷 Imagens**
### **Simulação no Wokwi**
#### **Simulação de 2 jogadores:**
<img src= "https://drive.google.com/uc?export=view&id=1KttgVh3cfpDpJGME2euNmH6TXQ4SFja2" width="400">

#### **Simulação de 4 jogadores:**
<img src= "https://drive.google.com/uc?export=view&id=10z0R2uNt-yKnEkRw4rD5KvJ_FeplgiZg" width="400">

### 🖥️ Execução na Raspberry Pi 
#### **Imagem ilustrando que o jogo foi embarcado na Raspberry Pi:**
<img src= "https://drive.google.com/uc?export=view&id=1u5mqmAliPXpgY_qHVdCgMlh95JQKp33M" width="400" height="570">

## 📜 Licença  
Este projeto está licenciado sob a [MIT License](LICENSE).  

## **Agradecimentos**
###
- **Professor Juan Sebastian Toquica Arenas**: Orientador do projeto e professor da disciplina de Sistemas Embarcados na UFC Itapajé
###
- **Equipe do Projeto:** Carlos Kaique Rosa Silva ([Kaique Silva](https://github.com/hoyalles)) e Nívea Morais Vaes ([Nívea Morais](https://github.com/Vaes3Nivea))
