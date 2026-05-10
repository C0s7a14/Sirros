# API Contracts

## Autenticação

Todos os endpoints protegidos exigem o header:
```
Authorization: Bearer <access_token>
```

Padrão de erro:
```json
{ "detail": "mensagem de erro" }
```

---

## Auth

### POST /auth/login
Request:
```json
{ "email": "string", "password": "string" }
```
Response `200`:
```json
{ "access_token": "string", "refresh_token": "string" }
```

### POST /auth/refresh
Request:
```json
{ "refresh_token": "string" }
```
Response `200`:
```json
{ "access_token": "string", "refresh_token": "string" }
```

### POST /auth/logout
Header: `Authorization: Bearer <token>`
Response `204`: sem corpo

---

## Trainings

### GET /trainings
Header: `Authorization: Bearer <token>`
Response `200`:
```json
[{ "id": "uuid", "title": "string", "description": "string" }]
```

### POST /trainings
Header: `Authorization: Bearer <token>`
Request:
```json
{ "title": "string", "description": "string" }
```
Response `201`:
```json
{ "id": "uuid", "title": "string", "description": "string" }
```

### GET /trainings/{id}
Header: `Authorization: Bearer <token>`
Response `200`:
```json
{ "id": "uuid", "title": "string", "description": "string" }
```

### PUT /trainings/{id}
Header: `Authorization: Bearer <token>`
Request:
```json
{ "title": "string", "description": "string" }
```
Response `200`:
```json
{ "id": "uuid", "title": "string", "description": "string" }
```

### DELETE /trainings/{id}
Header: `Authorization: Bearer <token>`
Response `204`: sem corpo

---

## PDF Documents

### POST /trainings/{id}/documents
Header: `Authorization: Bearer <token>`
Content-Type: `multipart/form-data`
Body: `file` (PDF)
Response `202`:
```json
{ "id": "uuid", "training_id": "uuid", "filename": "string", "status": "processing" }
```

---

## Progress

### GET /progress/{training_id}
Header: `Authorization: Bearer <token>`
Response `200`:
```json
{ "training_id": "uuid", "user_id": "uuid", "percentage": 0.0 }
```

---

## Quizzes

### GET /quizzes
Header: `Authorization: Bearer <token>`
Response `200`:
```json
[{ "id": "uuid", "training_id": "uuid", "title": "string" }]
```

### POST /quizzes
Header: `Authorization: Bearer <token>`
Request:
```json
{ "training_id": "uuid", "title": "string" }
```
Response `201`:
```json
{ "id": "uuid", "training_id": "uuid", "title": "string" }
```

### GET /quizzes/{id}
Header: `Authorization: Bearer <token>`
Response `200`:
```json
{ "id": "uuid", "training_id": "uuid", "title": "string" }
```
