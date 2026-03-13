# 🚀 Stack Técnica & Diferenciais de Engenharia

Este projeto consolida o domínio de tecnologias modernas e práticas de arquitetura robusta, focadas em escalabilidade e segurança.

## 🛠️ Tecnologias e Implementações

*   **Frontend (HTML/CSS/JS):** 
    *   Interface responsiva com manipulação de DOM via **Vanilla JS**.
    *   Gestão de estado client-side para cálculos em tempo real e validação de regras de negócio.
    *   Comunicação assíncrona com a API utilizando a **Fetch API**.
    *   Criação de Dashboards Administrativos isolados para gestão e monitoramento de pedidos.
    *   Uso de funções de alta ordem (Map/Join) para transformar dados complexos em interfaces legíveis.
    *   Gestão de Estado (State Management) para controles dinâmicos de paginação assíncrona na Interface.

*   **Backend (FastAPI):** 
    *   Criação de API RESTful de alta performance com tipagem rigorosa via **Pydantic**.
    *   Arquitetura modularizada (Separation of Concerns) separando modelos, rotas e banco de dados.
    *   Servidor ASGI configurado com **Uvicorn** para suporte a concorrência.
    *   Desenvolvimento de rotas de leitura (Read) , atualização (Update) e exclusão (Delete) seguindo o padrão RESTful.
    *   Aplicação do conceito de **Single Source of Truth (SSOT)**, centralizando regras de negócio e preços na API.
    *   Validação rigorosa e **recálculo de valores financeiros** no servidor para evitar manipulação de dados (*Payload Tampering*).
    *   Implementação de Autenticação utilizando o protocolo nativo **HTTP Basic Auth**, protegendo rotas administrativas.
    *   Uso de validação de parâmetros de requisição via **FastAPI Query**, barrando volumes abusivos de chamadas de dados.

*   **Persistência (SQLite):** 
    *   Implementação de banco de dados relacional com **SQL parametrizado** (blindagem contra SQL Injection).
    *   Uso de Gerenciadores de Contexto (`with`) para garantir integridade de conexões e memória.
    *   Tratamento de dados complexos (listas) via serialização **JSON**.
    *   Paginação otimizada com controle de **LIMIT** e **OFFSET**, aliado à ordenação na extração temporal dos dados (ORDER BY).

*   **Segurança & Configuração (Dotenv):** 
    *   Isolamento de credenciais sensíveis (Webhooks) em variáveis de ambiente.
    *   Uso da biblioteca `python-dotenv` para carregamento dinâmico de configurações.
    *   Armazenamento do catálogo de preços estruturado como JSON no cofre (`.env`), facilitando atualizações ágeis sem recompilar código.
    *   Uso da biblioteca `secrets` nativa do Python para comparação segura de strings (prevenção contra **Timing Attacks**).

*   **Integração (Discord Webhook):** 
    *   Mensageria automatizada via requisições HTTP assíncronas (**HTTPX**).
    *   Formatação de notificações inteligentes com templates Markdown para monitoramento.

*   **Qualidade & Testes Automatizados (Pytest):**
    *   Implementação de rotinas de testes garantindo estabilidade do código contra regressões.
    *   Uso do **FastAPI TestClient** para simulação de servidor e validação de Endpoints (Testes de Integração).
    *   Testes Unitários aplicando funções matemáticas de domínio para validar reajustes de preços e taxas.
    *   Injeção de Mocks e **Dependency Overrides** nativo do framework para burlar camadas de autenticação de forma isolada sem vazar credenciais.

## 🛡️ Fundamentos de Engenharia Aplicados

*   **Tratamento de Exceções:** Uso de blocos `try/except` para garantir a resiliência da API em casos de falhas externas.
*   **Acesso por Path Parameters:** Uso de rotas RESTful com IDs na URL para operações precisas de deleção (ex: `/pedidos/{id}`).
*   **Prevenção de Payload Tampering:** Recálculo cego de totais financeiros em backend ignorando origens não confiáveis de frontend.
*   **Defensive Programming (Prevenção DoS):** Proteção sistemática contra *Out of Memory* no banco e servidor aplicando paginação obrigatória e validação estrita (`ge=1, le=100`) via *FastAPI Query*, cortando requisições abusivas antecipadamente com HTTP 422.
*   **Testes Automatizados (Garantia de Comportamento):** Validação programática (Unitária e Integração) provando a resistência de lógicas de negócio e barreiras de acesso contra entradas maliciosas ou alterações não intencionais.
*   **Fail Fast (Falha Rápida):** A aplicação quebra a execução durante a inicialização (Erro Crítico) caso as credenciais obrigatórias não tenham sido configuradas no Ambiente, prevenindo instabilidades no faturamento.
*   **Single Source of Truth (SSOT):** O frontend obtém configurações (preços) na inicialização ao invés de utilizar dicionários *hardcoded*.
*   **Princípio SRP (Responsabilidade Única):** Separação rigorosa de scripts por funcionalidade (`criar_pedido.js` vs `manejar_pedidos.js`) para evitar acoplamento.
*   **API Decoupled:** Separação total entre a entrega do visual (HTML) e os dados (JSON), permitindo escalabilidade para futuros apps mobile.
*   **Código Limpo (Clean Code):** Nomenclatura semântica de variáveis e funções, visando legibilidade e manutenção.
*   **Controle de Execução:** Implementação do padrão `if __name__ == "__main__":` para controle fino de inicialização de scripts.
*   **Gestão de Dependências:** Projeto estruturado com pré requisítos (requirements.txt) e ambiente virtual (.venv).