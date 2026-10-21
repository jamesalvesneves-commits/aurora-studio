# Arquitetura do AURORA Studio

## Definição do produto

AURORA Studio é um aplicativo Windows profissional com duas camadas de interface:

1. **Cockpit Central AURORA** — interface gráfica única, própria, onde o usuário escreve comandos em texto, acompanha a produção em tempo real, vê o estado do projeto, dispara ações e acompanha o progresso.
2. **Interfaces originais dos componentes** — Ardour, ACE-Step e Demucs continuam existindo com suas interfaces nativas, abertas em janelas separadas, acessíveis por botões no Cockpit.

O usuário trabalha de duas formas complementares, sempre dentro do mesmo projeto:
- Pelo Cockpit, escrevendo em linguagem natural, sem tocar em nenhum programa individual.
- Pela interface original de qualquer componente, clicando no botão correspondente no Cockpit, para edição manual especializada.

As duas formas operam sobre o mesmo projeto, a mesma sessão e os mesmos arquivos, com sincronização automática.

## Decisão de engenharia fixa

As janelas do Ardour, ACE-Step e Demucs **não são embutidas visualmente** dentro do Cockpit. Elas são abertas como janelas separadas, gerenciadas e sincronizadas pelo Cockpit. Embutir janelas de terceiros quebraria isolamento, DPI e estabilidade.

## Componentes do barramento

- **Project State Database** — SQLite, fonte única de verdade do projeto.
- **File Watcher** — monitora a pasta do projeto e detecta alterações feitas por qualquer componente.
- **Event Bus** — publica eventos como "stem gerado", "faixa importada", "mixagem salva", "erro".
- **Ardour Bridge** — comunica-se com o Ardour via OSC e scripts Lua.
- **ACE-Step Bridge** — controla geração, edição e regeneração.
- **Demucs Bridge** — controla separação de stems.
- **Ollama Orchestrator** — interpreta texto do usuário e emite comandos aos bridges.

## Projeto único

Todo trabalho acontece dentro de uma única pasta de projeto, por exemplo:

```
C:\AURORA Studio\Projects\Minha Balada\
```

Dentro dela, gerenciados automaticamente:
- Sessão do Ardour.
- Áudio gerado pelo ACE-Step.
- Stems gerados pelo Demucs.
- Letras e prompts.
- Histórico de versões.
- Estado do projeto no SQLite.

Quando o ACE-Step gera uma música, o arquivo é salvo na pasta e o Event Bus avisa o Cockpit e o Ardour Bridge, que importa automaticamente o áudio como nova faixa na sessão aberta.

Quando o Demucs separa a faixa, os stems são salvos na mesma pasta e importados automaticamente como faixas separadas no Ardour.

Quando o usuário edita algo diretamente no Ardour, o File Watcher detecta a mudança e atualiza o estado no Cockpit.

## Interface do Cockpit Central

Regiões fixas:
- Barra de projetos — nome do projeto, botão novo, abrir, salvar, histórico.
- Barra de módulos — botões grandes: ACE-Step, Demucs, Ardour, Ollama, Biblioteca.
- Área de comando por texto.
- Tela central de execução — linha do tempo, faixas ativas, stems, status de geração e progresso.
- Painel de tarefas — fila, progresso, erros e botão cancelar.
- Painel de status — estado de cada componente (online, ocupado, erro).

Cada botão de módulo:
- Clique simples — abre a interface original daquele componente em janela separada, já apontada para o projeto atual.
- Clique longo ou botão "status" — mostra o estado daquele componente no Cockpit, sem abrir janela.

## Instalação

Instalador único `AURORAStudio-Setup.exe`, gerado com Inno Setup 7, assinado com Authenticode.

Regras fixas de instalação:
- Ollama — instalado via Chocolatey (`choco install ollama`).
- Git — instalado via Chocolatey.
- Python runtime privado — instalado via Chocolatey, versão fixa, isolado dentro da pasta do AURORA.
- ACE-Step — obtido por `git clone` com tag fixa, dependências instaladas no ambiente Python privado.
- Demucs — obtido por `git clone` com tag fixa, dependências instaladas no ambiente Python privado.
- Ardour — baixado do site oficial e instalado silenciosamente.
- Modelos — baixados das fontes oficiais, com hash verificado.

Todos os passos executam internamente, sem mostrar terminal ao usuário. O usuário vê apenas uma tela de progresso com nome da etapa e barra.

## Estrutura de pastas do produto instalado

```
C:\AURORA Studio\
  App\          — Cockpit Central e runtime Qt
  Engines\
    Ollama\
    ACE-Step\
    Demucs\
    Ardour\
  Models\
  Projects\
  Library\
  Logs\
  Cache\
  Backups\
```

Discos:
- SSD 400 GB — disco principal.
- SSD 80 GB — cache.
- HD 500 GB — backup e exportação.

## Sincronização com o Ardour

Dois canais complementares:
- OSC — comandos em tempo real (play, stop, seleção de faixa, transporte).
- Sessão XML + scripts Lua — criação de faixas, importação de áudio e salvamento estruturado.

## Segurança e integridade

- Todos os downloads com hash verificado.
- Instalador e executável assinados com Authenticode.
- Nenhum áudio ou projeto sai do computador.
- Internet usada apenas para download de componentes e atualizações.
- Chocolatey instalado pelo próprio instalador, se não existir, sem intervenção do usuário.

## Limites honestos

- Janelas dos componentes permanecem separadas, gerenciadas pelo Cockpit — não embutidas visualmente.
- GTX 1660 Super (6 GB VRAM) limita Ollama a modelos 7B/8B Q4 e o ACE-Step 1.5 (menos de 4 GB VRAM); os dois não rodam simultaneamente com folga — o orquestrador gerencia a liberação de VRAM.
- Sincronização em tempo real com Ardour via OSC/Lua no Windows é a área de maior risco técnico e será validada primeiro.

## Ordem de construção

1. Repositório GitHub com estrutura e CI.
2. Cockpit Central em Qt.
3. Barramento de Projeto e SQLite.
4. Integração com Ollama.
5. Integração com ACE-Step.
6. Integração com Demucs.
7. Ardour Bridge com OSC e Lua.
8. File Watcher e sincronização.
9. Instalador Inno Setup com Chocolatey e pull.
10. Testes no setup-alvo.
11. Assinatura, empacotamento e manual.

Cada etapa só é considerada concluída quando está compilada, testada e incluída no instalador.
