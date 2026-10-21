# AURORA Studio

AURORA Studio é um estúdio de produção musical profissional para Windows, orquestrado por Ollama, que integra Ardour, ACE-Step e Demucs em um único ecossistema controlado por uma interface gráfica própria (Cockpit Central).

## Visão geral

- **Cockpit Central (Qt 6 / C++)**: interface única onde o usuário escreve comandos em linguagem natural, acompanha o projeto em tempo real e dispara ações.
- **Interfaces originais dos componentes**: Ardour, ACE-Step e Demucs continuam com suas janelas nativas, acessíveis por botões no Cockpit, sempre sincronizadas ao mesmo projeto.
- **Ollama**: cérebro orquestrador que interpreta os comandos do usuário e emite ordens para as pontes de cada ferramenta.
- **Barramento de Projeto**: SQLite + File Watcher + Event Bus que mantêm todos os componentes sincronizados sobre uma única pasta de projeto.

## Stack

| Componente | Função |
|---|---|
| Ardour | DAW central: gravação, edição, mixagem, arranjo |
| ACE-Step | Geração de música completa a partir de texto |
| Demucs | Separação de stems (vocal, bateria, baixo, outros) |
| Ollama | Orquestrador / cérebro |
| Cockpit Central | Interface gráfica própria e camada de controle |

## Instalação

O produto final será distribuído como um único `AURORAStudio-Setup.exe` (Inno Setup), que instala automaticamente todos os componentes do stack via Chocolatey, git clone com tag fixa e download verificado por hash — sem exigir qualquer intervenção técnica do usuário.

## Status

Projeto em fase de fundação. Consulte `docs/ARQUITETURA.md` para o plano completo e fechado.
