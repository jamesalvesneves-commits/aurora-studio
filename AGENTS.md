# Contrato de desenvolvimento do AURORA Studio

Estas instruções regem alterações neste repositório. Não substituem revisão humana nem garantem ausência de erros.

1. O usuário final instala e usa um aplicativo Windows. Nunca exigir que monte fontes, crie pastas, compile, configure Python ou execute comandos no terminal.
2. Ignorar anexos visuais de conversas enquanto o usuário não revogar expressamente essa instrução. Não usá-los como requisitos visuais.
3. Preservar o objetivo: Cockpit próprio, Ollama local, Ardour, ACE-Step e Demucs, instalação automatizada e launcher. Nenhuma remoção de escopo sem aprovação explícita.
4. C++/Qt para o Cockpit. Adaptadores Python isolados somente quando necessários aos motores. Um repositório integrado não significa um único arquivo nem uma única linguagem para dependências de terceiros.
5. Antes de alterar: consultar arquivos vigentes, identificar requisitos afetados e planejar testes. Não assumir que trechos anteriores estão implementados.
6. Distinguir sempre planejado, implementado, compilado, testado em CI e homologado no hardware. Nunca usar progresso fictício nem afirmar integração com base em botões.
7. Cada capacidade entregue deve ter evidência verificável. Falha de compilação ou teste bloqueia sua classificação como validada. CI verde não é homologação musical.
8. Nunca executar comandos livres produzidos pelo LLM. Usar ações tipadas, validação de parâmetros e confirmação para operações destrutivas.
9. Ardour é autoridade da sessão musical; SQLite registra tarefas e artefatos do AURORA. Monitor de arquivos não garante sincronização de edição. Não editar XML de sessão aberta.
10. Integrações devem ser validadas com as APIs reais. Demucs não possui GUI nativa; seu painel deve ser implementado no Cockpit. Não prometer acesso universal às funções de programas externos.
11. Instalação exige manifesto de versões, fontes oficiais, licenças, hashes, reparação e testes. Não presumir que Chocolatey instala runtimes privados nem que git clone entrega motores prontos.
12. Não presumir letras de unidade, VRAM livre, desempenho, certificados de assinatura ou compatibilidade do ACE-Step com a GTX 1660 Super. Validar no equipamento. Falta de evidência é bloqueio, não motivo para declarar sucesso.
13. Não publicar como estúdio completo sem integração ponta a ponta, instalador validado, manual correspondente, testes de recuperação e homologação. Toda entrega parcial deve ser identificada.
14. Segredos nunca entram no chat nem no repositório. Escritas externas dependem da aprovação da ferramenta.

## Lista obrigatória antes de declarar uma entrega
- Requisitos afetados identificados.
- Código vigente consolidado.
- Testes correspondentes presentes e resultados reais registrados.
- Nenhuma função simulada descrita como funcional.
- Instalação e uso sem tarefas de desenvolvimento para o usuário.
- Limitações e bloqueios explicitados.

## Situação desta alteração
Cockpit inicial e teste de abertura implementados nos fontes. Compilação e teste ainda dependem de execução confirmada do GitHub Actions. Motores, sincronização, instalador e assinatura não implementados. Não há pacote para usuário final.
