# Arquitetura consolidada do AURORA Studio

Revisão: 21 de outubro de 2026. Substitui as promessas não verificadas da versão anterior deste documento. Documento de requisitos e decisões, não declaração de funcionalidades entregues. AGENTS.md permanece obrigatório.

## Contrato de entrega
Aplicativo Windows com Cockpit próprio, instalação gráfica e atalho na área de trabalho. O usuário final não cria fontes, não compila, não prepara ambientes e não executa comandos. Desenvolvimento e testes ficam no repositório. O objetivo é um estúdio profissional integrado; etapas parciais não são o produto completo.

## Equipamento-alvo
Windows 11 Pro; Xeon E5-2630 v4; GTX 1660 Super 6 GB; 32 GB RAM; NVMe 400 GB; NVMe 80 GB; HDD SATA 500 GB. Não presumir letras de unidade, espaço livre, consumo nem desempenho. Identificar volumes antes de atribuir projetos, cache e backup.

## Responsabilidades
- Cockpit C++/Qt: interface própria, projetos, tarefas, recursos, diagnóstico e acesso a janelas externas.
- Ollama local: interpretar pedidos e propor ações estruturadas. Modelo e versão somente serão fixados após validação.
- Executor AURORA: validar ações cadastradas, controlar fila, recursos, cancelamento e resultados. Nunca executar comandos arbitrários produzidos pelo modelo.
- Ardour: autoridade da sessão musical e das edições manuais.
- SQLite: autoridade dos metadados, tarefas, artefatos e vínculos do AURORA; não substitui a sessão Ardour.
- ACE-Step: geração e transformação dentro das capacidades integradas e verificadas.
- Demucs: separação por adaptador isolado; painel próprio no Cockpit, sem presumir GUI nativa.
- Adaptadores Python: ambientes privados compatíveis com cada motor, sem pressupor um ambiente compartilhado.

## Interface e projeto
Uma janela central própria, com projetos, módulos, comandos, acompanhamento, tarefas e estado. Janelas originais disponíveis são abertas separadamente; não serão embutidas por manipulação de janelas externas. Não usar anexos visuais da conversa como requisitos.
Projeto único significa sessão Ardour, áudios, stems, prompts, parâmetros, histórico e vínculos reunidos logicamente. Não significa formato interno comum a todos os programas. Monitor de arquivos detecta alterações em arquivos, não representa observação integral da edição musical. Não editar XML de sessão aberta.

## Tempo real
Acompanhamento de eventos e progresso real durante processamento. Incorporação de áudio após conclusão e confirmação. Não prometer geração instantânea, simultaneidade de todos os motores nem reprodução ininterrupta durante qualquer alteração. Não exibir progresso fictício.

## Instalação e distribuição
Entrega final prevista: AURORAStudio-Setup.exe e launcher AURORA.exe. O instalador deve obter e validar componentes, modelos e dependências; verificar espaço; retomar downloads; reparar falhas; criar atalho; preservar projetos conforme política explícita.
Manifesto obrigatório com versões, origens, hashes, licenças e testes. Chocolatey e git clone não são soluções presumidas de isolamento e distribuição. Não exigir Git, compiladores nem Python global do usuário. Ferramenta e versão do instalador dependem de validação antes de congelamento. Assinatura exige certificado e processo próprios, ainda não disponíveis como entrega.
Origem do binário Ardour, fontes correspondentes e licenças das dependências são bloqueios de distribuição. Não contornar autenticação nem incluir credenciais.

## Segurança
Motores vinculados à interface local; nenhuma exposição à rede por padrão. Processamento musical local como requisito; verificar tráfego e desabilitar caminhos de nuvem. Operações destrutivas exigem confirmação. Logs não devem incluir segredos. Downloads e atualizações precisam de integridade verificada.

## Validação e bloqueios
Ardour: OSC/Lua são candidatos documentados; acionar scripts externamente, importar e retornar estado requer protótipo. Ver docs/ARDOUR_BRIDGE.md.
ACE-Step: API, ambiente Windows e memória da GTX precisam de verificação na versão escolhida; não garantir funcionamento por VRAM nominal.
Demucs: fixar revisão e dependências testadas; considerar manutenção limitada.
Ollama: validar ações estruturadas, modelo e consumo; não fixar 8B por estimativa.
Plugins e auxiliares: seleção final ainda bloqueada por compatibilidade Windows, licenças e testes. Não declarar o stack completo antes dessa seleção.

## Marcos de execução
1. Consolidar documentação e matriz de requisitos.
2. Provar ponte Ardour, distribuição e viabilidade dos motores.
3. Implementar persistência e executor validado.
4. Integrar motores e Cockpit incrementalmente.
5. Construir instalador completo e recuperação.
6. Homologar no setup-alvo e produzir manual correspondente.
Cada marco possui evidência própria. CI verde não comprova qualidade musical nem homologação. Não avançar sobre dependência bloqueante como se estivesse resolvida.

## Estado
Há fontes iniciais e workflows; integrações e instalador final não são declarados concluídos neste documento. Resultados de CI devem ser vinculados ao commit e à execução observada. Esta revisão não constitui novo teste.
