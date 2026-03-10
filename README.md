# 🚀 Stack Técnica & Diferenciais de Engenharia

Este projeto consolida o domínio de tecnologias modernas e práticas de arquitetura robusta, focadas em escalabilidade e segurança.

## 🛠️ Tecnologias e Implementações

*   **Frontend (HTML/CSS/JS):** 
    *   Interface responsiva com manipulação de DOM via **Vanilla JS**.
    *   Gestão de estado client-side para cálculos em tempo real e validação de regras de negócio.
    *   Comunicação assíncrona com a API utilizando a **Fetch API**.
    *   Criação de Dashboards Administrativos isolados para gestão e monitoramento de pedidos.
    *   Uso de funções de alta ordem (Map/Join) para transformar dados complexos em interfaces legíveis.

*   **Backend (FastAPI):** 
    *   Criação de API RESTful de alta performance com tipagem rigorosa via **Pydantic**.
    *   Arquitetura modularizada (Separation of Concerns) separando modelos, rotas e banco de dados.
    *   Servidor ASGI configurado com **Uvicorn** para suporte a concorrência.
    *   Desenvolvimento de rotas de leitura (Read) , atualização (Update) e exclusão (Delete) seguindo o padrão RESTful.

*   **Persistência (SQLite):** 
    *   Implementação de banco de dados relacional com **SQL parametrizado** (blindagem contra SQL Injection).
    *   Uso de Gerenciadores de Contexto (`with`) para garantir integridade de conexões e memória.
    *   Tratamento de dados complexos (listas) via serialização **JSON**.

*   **Segurança & Configuração (Dotenv):** 
    *   Isolamento de credenciais sensíveis (Webhooks) em variáveis de ambiente.
    *   Uso da biblioteca `python-dotenv` para carregamento dinâmico de configurações.

*   **Integração (Discord Webhook):** 
    *   Mensageria automatizada via requisições HTTP assíncronas (**HTTPX**).
    *   Formatação de notificações inteligentes com templates Markdown para monitoramento.

## 🛡️ Fundamentos de Engenharia Aplicados

*   **Tratamento de Exceções:** Uso de blocos `try/except` para garantir a resiliência da API em casos de falhas externas.
*   **Código Limpo (Clean Code):** Nomenclatura semântica de variáveis e funções, visando legibilidade e manutenção.
*   **Controle de Execução:** Implementação do padrão `if __name__ == "__main__":` para controle fino de inicialização de scripts.
*   **Gestão de Dependências:** Projeto estruturado com pré requisítos (requirements.txt) e ambiente virtual (.venv).