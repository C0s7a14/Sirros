# Modelo de Domínio

## Entidades

### User
| Campo         | Tipo      |
|---------------|-----------|
| id            | UUID (PK) |
| email         | str       |
| password_hash | str       |
| created_at    | datetime  |
| updated_at    | datetime  |

### Training
| Campo       | Tipo      |
|-------------|-----------|
| id          | UUID (PK) |
| title       | str       |
| description | str       |
| created_at  | datetime  |
| updated_at  | datetime  |

### TrainingDocument
| Campo       | Tipo               |
|-------------|--------------------|
| id          | UUID (PK)          |
| training_id | UUID (FK→Training) |
| filename    | str                |
| created_at  | datetime           |

### TrainingChunk
| Campo       | Tipo                        |
|-------------|-----------------------------|
| id          | UUID (PK)                   |
| document_id | UUID (FK→TrainingDocument)  |
| chunk_text  | str                         |
| chunk_index | int                         |

### Progress
| Campo       | Tipo               |
|-------------|--------------------|
| id          | UUID (PK)          |
| user_id     | UUID (FK→User)     |
| training_id | UUID (FK→Training) |
| percentage  | float              |
| updated_at  | datetime           |

### Quiz
| Campo       | Tipo               |
|-------------|--------------------|
| id          | UUID (PK)          |
| training_id | UUID (FK→Training) |
| title       | str                |
| created_at  | datetime           |
| updated_at  | datetime           |

---

## Relações

- `Training` 1→N `TrainingDocument`
- `TrainingDocument` 1→N `TrainingChunk`
- `User` N→N `Training` via `Progress`
- `Training` 1→N `Quiz`
