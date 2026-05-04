import os
import json
import time
import requests
from datetime import datetime
from flask import Flask

# Inicializa o Flask para que o servidor gratuito (como a Render) 
# identifique um serviço ativo e não derrube a aplicação.
app = Flask(__name__)

# CONFIGURAÇÕES (O usuário deve preencher o Webhook no ambiente do servidor)
WEBHOOK_URL = os.environ.get("WEBHOOK_URL", "COLOQUE_SEU_WEBHOOK_AQUI")

@app.route('/')
def health_check():
    return "Trend Machine is Running!", 200

def get_trends():
    """Simula a captura de tendências reais."""
    # Aqui poderíamos integrar bibliotecas de scraping específicas
    return [
        {"title": "IA que cria vídeos de avatares", "traffic": "High", "niche": "IA/Tech"},
        {"title": "Como organizar rotina com Notion em 2026", "traffic": "Medium", "niche": "Produtividade"},
        {"title": "Nova regra de monetização do YouTube Shorts", "traffic": "Viral", "niche": "Finanças/Creator"}
    ]

def generate_premium_prompt(trend):
    """Gera um prompt de alta performance com técnicas de retenção."""
    prompt = f"""
--- PROMPT DE OURO: ROTEIRO VIRAL 2026 ---
Atue como o maior roteirista de Short-form Content do mundo, especialista em retenção extrema.

TENDÊNCIA: {trend['title']}
NICHO: {trend['niche']}

ESTRUTURA OBRIGATÓRIA:
1. O GANCHO (0-3s): Use um 'Visual Hook' descrito em parênteses e uma frase que quebre o padrão (Pattern Interrupt). Ex: "Pare de fazer [X] se você quer [Y]".
2. O CONFLITO (3-15s): Apresente o problema que essa tendência resolve ou a curiosidade que ela desperta.
3. A SOLUÇÃO (15-40s): Entrega rápida, sem enrolação, com 3 pontos chave.
4. O LOOP (40-50s): Termine com uma frase que conecte perfeitamente com o início do vídeo para incentivar o replay.

TONALIDADE: Enérgico, Autoridade, Minimalista.
REGRAS: Sem introduções como "Olá pessoal". Vá direto ao ponto.

Gere o roteiro agora para meu canal de {trend['niche']}.
-----------------------------------------
"""
    return prompt

def run_trend_machine():
    """Lógica principal de monitoramento."""
    print(f"[{datetime.now()}] Iniciando ciclo de monitoramento...")
    trends = get_trends()
    
    for trend in trends:
        prompt = generate_premium_prompt(trend)
        payload = {
            "username": "Trend Machine Bot",
            "avatar_url": "https://cdn-icons-png.flaticon.com/512/2103/2103633.png",
            "content": f"🚨 **NOVA TENDÊNCIA DETECTADA: {trend['title']}**",
            "embeds": [{
                "title": "📋 Prompt de Ouro Gerado",
                "description": f"```\n{prompt}\n```",
                "color": 15844367,
                "footer": {"text": "Copie e cole no ChatGPT Enterprise ou Gemini Pro"}
            }]
        }
        
        if "http" in WEBHOOK_URL:
            try:
                requests.post(WEBHOOK_URL, json=payload)
                print(f"Sucesso ao enviar: {trend['title']}")
            except Exception as e:
                print(f"Erro ao enviar: {e}")
        else:
            print("Webhook não configurado. Exibindo no log:")
            print(json.dumps(payload, indent=2))
        
        time.sleep(2) # Evita spam no Webhook

if __name__ == "__main__":
    # Em servidores como Render, o Flask roda em background
    # enquanto a lógica de monitoramento pode ser disparada por um timer ou thread.
    # Para este exemplo, vamos apenas iniciar o Flask.
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
