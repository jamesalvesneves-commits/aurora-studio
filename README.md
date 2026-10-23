# Aurora Studio

Estúdio musical local para Windows controlado por linguagem natural.

- Escreva um prompt (ex.: "crie uma balada em Ré menor com piano, bateria e baixo, 80 BPM").
- O Aurora Studio usa o Ollama local para interpretar o pedido.
- O motor musical gera arquivos MIDI (bateria, baixo, acordes, melodia).
- O Aurora abre o Ardour para edição profissional completa com mouse.
- A ponte OSC controla transporte (play/stop) no Ardour.

## Requisitos
- Windows 10/11
- Python 3.11+
- Ollama instalado (https://ollama.com/download)
- Ardour instalado (https://ardour.org/download.html)

## Instalação
1. Dê dois cliques em `install_aurora.bat`.
2. Aguarde a mensagem "Aurora Studio pronto".
3. Dê dois cliques em `run_aurora.bat`.

## Uso
1. Abra o Aurora Studio.
2. Escreva o prompt musical.
3. Clique em "Gerar música".
4. Clique em "Abrir no Ardour".
5. Edite livremente no Ardour com o mouse.

## Limitações da v0.1
- Gera MIDI; áudio/síntese e criação automática de sessão .ardour virão nas próximas versões.
- Requer Ollama e Ardour já instalados.
