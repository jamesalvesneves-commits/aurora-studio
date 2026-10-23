# Arquitetura Aurora Studio Master

## Camadas
1. Interface Central (PySide6)
2. Orquestrador (Python)
3. IA Local (Ollama)
4. Motor Musical (MIDI/áudio)
5. Integração Ardour (OSC + sessão)
6. Separação de Stems (Demucs)
7. Instalador (Chocolatey/PowerShell)
8. Exportador (WAV/MP3)

## Fluxo
Prompt -> Ollama -> Especificação musical -> Motor musical -> Sessão Ardour -> Edição -> Stems -> Exportação

## Módulos
- aurora_master/gui: interface central
- aurora_master/orchestrator: coordenação
- aurora_master/ai: cliente Ollama
- aurora_master/music: geração musical
- aurora_master/ardour: sessão e OSC
- aurora_master/stems: separação
- aurora_master/installer: instalação automática
- aurora_master/export: exportação

## Regra
- Nenhum módulo é entregue como final sem teste real.
- A branch main só recebe a versão master completa.
