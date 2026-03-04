# 🇨🇭 SwissDev Hub - Manual de Consulta Python

Este é o guia de bolso para os fundamentos de engenharia de software aplicados no projeto.

---

## 🏗️ Pilar 1: Infraestrutura (O Alicerce)

### 1. Ambiente Virtual (.venv)
Isolamento total das bibliotecas do projeto para evitar conflitos no sistema global.
*   **Exemplo 1 (Criação):** `python -m venv .venv`
*   **Exemplo 2 (Ativação PowerShell):** [.\.venv\Scripts\Activate.ps1](cci:7://file:///c:/Users/HD1T/Desktop/Gabriel/GIT_HUB/The-SwissDev-Hub/.venv/Scripts/Activate.ps1:0:0-0:0)

### 2. Gestão de Dependências (pip)
O gerenciador de pacotes do Python. Usamos o [requirements.txt](cci:7://file:///c:/Users/HD1T/Desktop/Gabriel/GIT_HUB/The-SwissDev-Hub/requirements.txt:0:0-0:0) como a nossa "lista de ingredientes".
*   **Exemplo 1 (Instalar lista):** `pip install -r requirements.txt`
*   **Exemplo 2 (Atualizar pip):** `python -m pip install --upgrade pip`

---

## 🧠 Pilar 2: Fundamentos e Memória

### 3. Dicionários e o Método `.get()`
Estruturas de Chave:Valor. O `.get()` é a "vacina" contra erros de chaves inexistentes.
*   **Exemplo 1 (Acesso Seguro):** `usuario.get("email")` (retorna `None` se não existir)
*   **Exemplo 2 (Valor Padrão):** `usuario.get("idioma", "pt-br")` (usa "pt-br" se não achar a chave)

### 4. Tipagem (Type Hints) - PEP 484
Dizer ao Python o que esperar de cada variável, facilitando a manutenção e o autocompletar do editor.
*   **Exemplo 1 (Variável):** `nome: str = "Gabriel"`
*   **Exemplo 2 (Função):** `def somar(a: int, b: int) -> int:`

### 5. Tuplas (Imutabilidade)
Coleções que não mudam. Ideais para configurações e constantes do sistema.
*   **Exemplo 1 (Criação):** `STATUS_OK = (200, 201, 204)`
*   **Exemplo 2 (Pesquisa):** `if 404 in STATUS_ERRO:`

---

## ⚡ Pilar 3: Performance

### 6. Sets (Conjuntos)
Coleções de alta velocidade que ignoram elementos duplicados automaticamente.
*   **Exemplo 1 (Limpando listas):** `unicos = set([1, 1, 2, 3])` -> `{1, 2, 3}`
*   **Exemplo 2 (Transformação):** `tags = set(lista_suja)`

### 7. Slicing (Fatiamento)
Extrair pedaços de objetos ordenados (listas, strings, tuplas).
*   **Exemplo 1 (Os 3 primeiros):** `primeiros = lista[:3]`
*   **Exemplo 2 (Do 2º em diante):** `resto = lista[1:]`

### 8. List Comprehensions
A forma mais rápida e elegante de criar ou filtrar listas em uma única linha.
*   **Exemplo 1 (Transformar):** `[n.upper() for n in nomes]`
*   **Exemplo 2 (Filtrar):** `[p for p in produtos if p > 100]`
