# Projeto

Plataforma de treinamentos baseada em PDFs.

# Docs

Documentação detalhada em `docs/`:
- `docs/architecture.md` — fluxo de camadas e processamento de PDFs
- `docs/api-contracts.md` — contratos de todos os endpoints
- `docs/project-structure.md` — estrutura de pastas do backend e frontend
- `docs/domain-model.md` — entidades e relações do banco de dados
- `docs/coding-standards.md` — padrões de código e ferramentas

# Stack

Frontend:
- React
- Vite
- TypeScript
- Tailwind
- TanStack Query

Backend:
- FastAPI
- PostgreSQL
- SQLAlchemy
- JWT (access token + refresh token)
- Alembic
- PyMuPDF4LLM (extração de texto de PDFs)

# Módulos

- `auth` — autenticação e autorização
- `trainings` — gestão de treinamentos
- `pdf_processing` — upload e processamento de PDFs em background via PyMuPDF4LLM
- `progress` — progresso do usuário por treinamento
- `quizzes` — quizzes associados aos treinamentos

# Arquitetura

- Repository pattern
- Service layer
- Controllers finos
- DTOs via Pydantic
- Sem lógica de negócio em rotas

# Regras

- Nunca usar any
- Nunca acessar banco diretamente nas rotas
- Sempre criar schemas separados
- Toda feature deve ter testes
- Toda API deve ter tipagem completa
- Componentes React devem ser pequenos
- Evitar arquivos > 300 linhas
- A cada tarefa executada, verificar se o código compila antes de considerar a tarefa concluída

# Convenções

- snake_case no backend
- camelCase no frontend
- Services terminam com Service
- Repositories terminam com Repository

# Comandos

```bash
# Backend
uvicorn app.main:app --reload        # servidor de desenvolvimento
pytest                               # rodar testes
alembic upgrade head                 # aplicar migrations

# Frontend
npm run dev                          # servidor de desenvolvimento
npm run build                        # build de produção
npm run lint                         # lint
```

# Variáveis de Ambiente

```
DATABASE_URL=postgresql://user:pass@localhost:5432/sirros
SECRET_KEY=sua-chave-secreta
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7
```

# PDFs

- PDFs são processados em background (tecnologia de fila a definir)
- Extração de texto via PyMuPDF4LLM
- Texto é dividido em chunks
- Chunks serão usados futuramente para IA/RAG