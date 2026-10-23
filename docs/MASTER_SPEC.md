# Aurora Studio — Especificação Master

## Regra de entrega
- A branch `main` só receberá a versão master quando estiver completa e testada.
- Nenhuma versão parcial será apresentada como entrega final.
- O rascunho v0.1 será substituído integralmente.

## Componentes obrigatórios
1. Interface central gráfica (PySide6)
2. Ollama (interpretação e orquestração local)
3. Ardour (DAW de edição, interface original preservada)
4. Motor de produção musical (arranjo, harmonia, bateria, baixo, melodia)
5. Separação de stems (Demucs ou equivalente open-source)
6. Instalação automática (Chocolatey ou equivalente)
7. Pacote autocontido Windows
8. Exportação WAV/MP3
9. Controle OSC do Ardour
10. Histórico de projetos e versões

## Interface central
- Lista todos os softwares do stack.
- Abre a interface original de cada software com um clique.
- Mostra progresso da produção em tempo real.
- Recebe instruções em português.
- Permite regenerar trechos e ajustar parâmetros.

## Integração Ardour
- Criação automática de sessão .ardour.
- Criação de faixas MIDI/áudio.
- Importação automática dos arquivos gerados.
- Controle de transporte, faixas, volume e pan via OSC.
- Edição profissional feita pelo usuário na interface original do Ardour.

## Critérios de aceite
- Instalação automática funcional no Windows.
- Geração musical de ponta a ponta.
- Sessão Ardour criada e aberta automaticamente.
- Stems separados e reimportados.
- Exportação WAV e MP3 funcional.
- Todos os componentes do stack presentes e operantes.
