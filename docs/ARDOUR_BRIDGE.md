# Contrato de validação da ponte Ardour

Estado: especificação de protótipo, sem implementação homologada. Não afirma compatibilidade integral no Windows.

## Fontes consultadas na revisão
- https://manual.ardour.org/using-control-surfaces/controlling-ardour-with-osc/
- https://manual.ardour.org/lua-scripting/
- https://manual.ardour.org/lua-scripting/class_reference/
- https://ardour.org/copying.html
A documentação orienta os candidatos técnicos; não substitui teste. A referência de bindings alerta sobre incompletude e mudanças. Licenças de binários e dependências devem ser auditadas na revisão distribuída.

## Limites e autoridades
Ardour mantém a sessão musical. AURORA mantém tarefas e vínculos. Não editar externamente XML de sessão aberta. Não confundir processo aberto com comunicação estabelecida. File watcher não comprova sincronização musical. Não sobrescrever edição manual para forçar consistência.

## Protocolo lógico proposto
Toda solicitação deve registrar request_id, project_id, session_id, operação, parâmetros e estado. Estados: pending, running, succeeded, failed, cancelled, unknown. Mensagem enviada não equivale a sucesso. Resultado deve incluir evidência verificável e vínculos dos recursos. Timeout ou desconexão geram unknown até reconciliação; não repetir automaticamente mutações sem verificar efeitos.
Esses campos descrevem o protocolo do adaptador AURORA, não endereços OSC nem métodos Lua existentes. O transporte para acionar operações Lua e receber respostas ainda é bloqueante e deve ser demonstrado.

## Ensaios de aceitação
B01 Comunicação: identificar sessão atendida e recusar sessão incorreta.
B02 Transporte: enviar play/stop por mecanismo documentado e confirmar estado retornado.
B03 Importação: importar áudio conhecido e conferir faixa, região, posição, duração e vínculo com request_id.
B04 Idempotência: repetir request_id e provar ausência de duplicação indevida, inclusive após reconexão.
B05 Edição manual: alterar a sessão, identificar o que pode ser observado e explicitar o que permanece desconhecido.
B06 Persistência: salvar, fechar, reabrir e conferir vínculos.
B07 Falhas: provocar desconexão e importação interrompida; reconciliar efeitos sem apagar edições.
B08 Integridade: comparar dados antes e depois e comprovar preservação da sessão original.

## Evidência exigida
Registrar commit AURORA, versão/revisão Ardour, Windows, entrada, passos, resultado esperado, resultado observado e diagnóstico. Executar em sessão descartável com cópia preservada. Não usar projeto musical do usuário como cobaia.

## Critério de passagem
Comunicação bidirecional, importação confirmada e repetição/reconexão sem duplicação precisam passar antes de implementar sincronização abrangente. Falha exige correção da arquitetura, não redução silenciosa a importação manual. Nenhum ensaio está marcado como aprovado nesta revisão.
