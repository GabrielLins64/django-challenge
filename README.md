<h1>Vulnerability Management System</h1>

<h2>Sumário</h2>

- [Sobre](#sobre)
- [Dependências](#dependências)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Como usar](#como-usar)
  - [Instalação e execução](#instalação-e-execução)
  - [Entrando no front-end](#entrando-no-front-end)
  - [Testando o back-end](#testando-o-back-end)
- [Documentações do sistema](#documentações-do-sistema)
  - [Swagger](#swagger)
  - [Docstrings](#docstrings)
- [Trabalhos futuros](#trabalhos-futuros)
  - [Melhoras de segurança](#melhoras-de-segurança)
  - [Features](#features)

---

## Sobre

O *Vulnerability Management System* é um sistema web para gestão de dados sobre vulnerabilidades. Dentre suas características, temos:

- Importação de CSV para a base de dados.
- Exibição de tabelas e gráficos de vulnerabilidades.
- Geração de relatório com:
  - Métricas de risco para o host.
  - Média de risco do ambiente.
- Controle de vulnerabilidades corrigidas ou pendentes.

---

## Dependências

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/install/)

---

## Tecnologias Utilizadas

- Docker (infraestrutura e compatibilidade do projeto)
- Django, DRF, Swagger (Back-end)
- PostgreSQL (Banco de Dados)
- React, TypeScript, Bootstrap, Font Awesome, Sweetalert2 e Axios (Front-end)

---

## Como usar

### Instalação e execução

Navegue até o diretório raiz deste repositório por um terminal, então execute:

```shell
docker compose up -d
```

Alternativamente, baixe o Docker Desktop GUI e siga as instruções, apontando para o arquivo `docker-compose.yml` deste repositório.

### Entrando no front-end

Navegue até http://localhost:3000/ e faça login com as credenciais:

**usuário:** admin
**senha:** admin

Uma vez no sistema, a interface é bem intuitiva.

### Testando o back-end

Para testar os endpoints da API pelo Swagger, navegue até http://localhost:8000/docs/

Alternativamente, no caminho `backend/assets/` há uma coleção do Postman com os endpoints, testes e templates já configurados.

---

## Documentações do sistema

### Swagger

A API possui uma documentação com Swagger. Para acessá-la, após [executar os containers](#instalação-e-execução), navegue até http://localhost:8000/docs.

### Docstrings

A API segue a maioria dos padrões da [PEP 8](https://peps.python.org/pep-0008/) e possui Docstrings para facilitar a navegação pelo código e sua documentação.

---

## Trabalhos futuros

Pontos a serem adicionados no futuro.

### Melhoras de segurança

- [ ] Salvar o JWT de maneira mais segura para evitar ataques XSS.
- [ ] Adicionar integração de reCAPTCHA para evitar spam de requisições.
- [ ] Autenticação por 2 fatores.

### Features

- [ ] Tela e endpoints para geração de relatórios de vulnerabilidades.
- [ ] Adicionar responsividade para dispositivos móveis pequenos.
- [ ] Integração do front-end com o endpoint para atualizar o status (corrigida ou não) de uma vulnerabilidade (o endpoint já existe, mas não a feature do front).
- [ ] Integração da barra de pesquisa do front-end com os filtros de busca do back-end (estão implementados no back, mas não há integração com o front no momento).
