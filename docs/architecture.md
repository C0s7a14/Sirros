# Arquitetura

## Backend

FastAPI modular monolith.

Fluxo:
```
Routes → Services → Repositories → Database
```

Regras:
- Routes sem lógica — apenas recebe request e chama service
- Services contêm regras de negócio
- Repositories fazem queries via SQLAlchemy
- Background jobs processam PDFs (tecnologia a definir)

## Frontend

React SPA.

Fluxo:
```
Pages → Components → Hooks → API services → Backend
```

## Autenticação

1. Cliente envia `email` + `password` para `POST /auth/login`
2. Backend valida, retorna `access_token` (curta duração) e `refresh_token` (longa duração)
3. Cliente inclui `Authorization: Bearer <access_token>` em todas as requisições
4. Quando o `access_token` expira, cliente usa `POST /auth/refresh` para obter novos tokens

## PDF Processing

1. Upload via `POST /trainings/{id}/documents`
2. Persist metadata (filename, training_id)
3. Enfileirar background job
4. Extrair texto com **PyMuPDF4LLM**
5. Dividir texto em chunks
6. Persistir chunks em `TrainingChunk`

## Futuro IA

Chunks armazenados em `TrainingChunk` serão usados em pipeline RAG para responder perguntas contextualizadas sobre os treinamentos.
