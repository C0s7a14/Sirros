# Padrões de Código

## Backend (Python)

- Type hints obrigatórios em todas as funções
- Sem funções > 50 linhas
- Sem lógica em routes — apenas chamada ao service
- Services devem ser pequenos e coesos
- Queries complexas ficam em repositories
- Arquivo de teste: `tests/test_<módulo>.py`

### Ferramentas
- **ruff** — linting e formatação
- **pytest** — testes

## Frontend (TypeScript)

- Tipagem obrigatória — proibido usar `any`
- Sem lógica pesada em componentes
- Hooks para estado e efeitos colaterais
- Componentes devem ser funções puras sempre que possível

### Ferramentas
- **eslint** — linting
- **prettier** — formatação

## Commits

Usar [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: adiciona upload de PDF
fix: corrige validação de token expirado
refactor: extrai lógica de chunking para service
docs: atualiza contratos de API
test: adiciona testes para progress service
```
