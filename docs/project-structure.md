# Estrutura do Projeto

## Raiz

```
sirros/
├── backend/
├── frontend/
├── docs/
├── migrations/          # Alembic migrations
├── docker-compose.yml
├── .env.example
└── CLAUDE.md
```

## Backend

```
backend/
└── app/
    ├── main.py
    ├── database.py
    └── modules/
        ├── auth/
        │   ├── routes.py
        │   ├── service.py
        │   ├── repository.py
        │   ├── models.py
        │   ├── schemas.py
        │   └── tests/
        ├── trainings/
        │   ├── routes.py
        │   ├── service.py
        │   ├── repository.py
        │   ├── models.py
        │   ├── schemas.py
        │   └── tests/
        ├── pdf_processing/
        │   ├── routes.py
        │   ├── service.py
        │   ├── repository.py
        │   ├── models.py
        │   ├── schemas.py
        │   └── tests/
        ├── progress/
        │   ├── routes.py
        │   ├── service.py
        │   ├── repository.py
        │   ├── models.py
        │   ├── schemas.py
        │   └── tests/
        └── quizzes/
            ├── routes.py
            ├── service.py
            ├── repository.py
            ├── models.py
            ├── schemas.py
            └── tests/
```

## Frontend

```
frontend/
└── src/
    ├── main.tsx
    ├── App.tsx
    ├── pages/           # Uma pasta por rota principal
    │   ├── Login/
    │   ├── Trainings/
    │   ├── Training/
    │   └── Quiz/
    ├── components/      # Componentes reutilizáveis
    ├── hooks/           # Custom hooks (estado, dados)
    ├── services/        # Chamadas à API (axios/fetch)
    ├── types/           # Tipos e interfaces TypeScript
    └── lib/             # Utilitários e configurações
```

## Cada módulo deve conter

- `routes.py` — endpoints FastAPI (sem lógica)
- `service.py` — regras de negócio
- `repository.py` — queries ao banco via SQLAlchemy
- `models.py` — modelos ORM
- `schemas.py` — schemas Pydantic (request/response)
- `tests/` — testes do módulo
