# Hospital PUC System

A modular hospital management system implementing Clean Architecture, Clean Code and design patterns to support core clinical and administrative workflows (patients, doctors, specialties, consultations, exams, prescriptions, hospitalizations, beds, medications, insurance plans, billing).

---

## 🧠 Problem Overview

Context  
Hospitals handle many interconnected entities (patients, doctors, appointments, billing, beds). Legacy or monolithic systems are hard to evolve and test.

Real Need  
Provide a maintainable, testable, extensible backend that separates business rules from infrastructure concerns, enabling safe evolution (new modules, integrations, notifications).

Target Stakeholders  
- Administrative staff (billing, insurance, sector management)  
- Medical staff (doctors, prescriptions, exams)  
- Nursing staff (hospitalization, bed allocation)  
- IT / Dev teams (extensibility & reliability)  
- Management (reporting & data consistency)  

---

## 🎯 System Objectives

Primary Objective  
Provide a cohesive backend API for complete hospital operational management.

Secondary Objectives  
- Enforce domain rules consistently  
- Reduce coupling via explicit boundaries  
- Enable automated tests with repository spies  
- Allow future integrations (email, messaging, analytics)  

---

## ✅ Functional Requirements

| Code  | Requirement                     | Description |
|-------|---------------------------------|-------------|
| RF01  | Patient Registration            | Register, list, update, delete patients. |
| RF02  | Doctor Registration             | Manage doctors and link to specialties. |
| RF03  | Specialty Management            | CRUD of medical specialties. |
| RF04  | Consultation Scheduling         | Create consultation with future-or-today date, validate participants. |
| RF05  | Examination Management          | Register and list exams tied to patient & doctor. |
| RF06  | Prescription Management         | Link medications, patient, doctor. |
| RF07  | Medication Catalog              | CRUD medications. |
| RF08  | Hospitalization (Internação)    | Register, update, discharge hospitalization records. |
| RF09  | Bed (Leito) Management          | Track bed type, status (available/occupied). |
| RF10  | Sector Management               | Manage hospital sectors. |
| RF11  | Insurance (Convênio)            | CRUD of insurance plans. |
| RF12  | Billing (Financeiro)            | Insert & update financial records with validation. |
| RF13  | Address Linking                 | Associate patient addresses. |
| RF14  | Validation Layer                | Reject malformed inputs (Cerberus validators). |
| RF15  | Consistent Error Responses      | Standard HTTP error envelope. |
| RF16  | Future Email Notifications      | Pluggable email sender port (planned). |

---

## 🔐 Non-Functional Requirements

| Code  | Category         | Requirement |
|-------|------------------|-------------|
| NFR01 | Architecture     | Clean Architecture layering. |
| NFR02 | Testability      | Use repository spies for unit tests. |
| NFR03 | Maintainability  | Separation of domain vs infra code. |
| NFR04 | Extensibility    | New modules via composer pattern. |
| NFR05 | Consistency      | Uniform HTTP envelope & validators. |
| NFR06 | Observability    | Central error handler + console traces. |
| NFR07 | Security (future)| Add authentication & RBAC layer. |
| NFR08 | Portability      | Environment via `.env` (not committed). |
| NFR09 | Data Integrity   | Enforce foreign keys & domain checks. |

---

## 🏛 Clean Architecture Layers

- domain/  
  - Entities (models) + use case interfaces  
- data/  
  - Use case implementations + repository interfaces  
- infra/  
  - DB repositories (SQLAlchemy / PyMySQL)  
- presentation/  
  - Controllers + HTTP request/response abstractions  
- validation/  
  - Cerberus schemas per operation  
- main/  
  - Routes, composers (dependency wiring), server bootstrap  
- errors/  
  - Typed HTTP/domain error classes & handler  

Flow: Route → request_adapter → Controller → UseCase → Repository → DB → format response.

---

## 🧩 Design Patterns

- Factory / Composer pattern (dependency injection per use case)
- Repository pattern (abstract persistence)
- Adapter pattern (request adapter decouples FastAPI)
- DTO-like formatting in use cases (uniform response)
- Strategy-ready (email sender interface)
- Centralized error handling (single responsibility)

---

## 📂 Key Modules

- Patients (paciente)
- Doctors (medico)
- Specialties (especialidade)
- Consultations (consulta)
- Exams (exame)
- Prescriptions (prescricao)
- Medications (medicamento)
- Hospitalizations (internacao)
- Beds (leito)
- Sectors (setor)
- Insurance (convenio)
- Finance (financeiro)
- Address (endereco)

---

## ⚙️ Error Handling

Custom exceptions (e.g. HttpBadRequestError) bubble to `handle_errors`, which:
- Maps known errors to specific status codes
- Logs stack trace (console)
- Returns JSON body:  
```
{
  "error": [
    {"title": "<ErrorType>", "message": "<details>"}
  ]
}
```

---

## 🧪 Testing

- tests/src/infra/db/tests/* repository spies
- Validate business logic without real DB
- Future expansion: controller + use case integration tests

---

## 🛠 Tech Stack

- Python 3.12
- FastAPI (routing layer abstraction)
- SQLAlchemy Core/ORM + PyMySQL
- Cerberus (validation)
- Uvicorn (ASGI server)

---

## 🔑 Environment (.env)

Example file: `src/.env.example`  
```
DB_USER=
DB_PASSWORD=
DB_HOST=localhost
DB_PORT=3306
DB_NAME=
```
Local secret file: `src/.env` (ignored via .gitignore)

---

## ▶️ Running

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp src/.env.example src/.env  # fill credentials
python run.py
```

API base: `http://127.0.0.1:8000/v1/`

---

## 🚦 Sample Endpoint Categories

| Group          | Methods |
|----------------|---------|
| /paciente      | POST, GET, PATCH, DELETE |
| /medico        | POST, GET, PATCH, DELETE |
| /consulta      | POST |
| /exame         | GET |
| /financeiro    | POST, PATCH |
| /leito         | POST, GET, PATCH, DELETE |
| /internacao    | POST, GET, PATCH, DELETE |
| ...            | (pattern consistent) |

---

## 🔄 Request Lifecycle (Example Insert)

POST /v1/medico  
1. Route → validator  
2. request_adapter builds HTTPRequest  
3. Controller maps body -> domain model  
4. Use case validates domain rules  
5. Repository persists  
6. Use case formats response → Controller → adapter returns JSON

---

## 🧱 Consistency Rules (Examples)

- Dates must follow YYYY-MM-DD
- Future constraints (e.g. finance emission date not future)
- Foreign keys validated via repository existence checks
- Enumerations validated in validator layer (status, tipo, etc.)

---

## 🌱 Future Improvements

- Authentication & JWT (RF future)
- Role-based access control
- Caching layer (bed / availability snapshots)
- Async DB and task queue for emails
- Auditing / event sourcing
- Metrics & structured logging

---

## 📌 Traceability Note

Functional requirement codes (RFxx) map to:
- Validators (validation/*)
- Use cases (data/usecases/*)
- Controllers (presentation/controllers/*)
- Routes (main/routes/*)  

---

## 📄 License

Internal / Educational (define if open-source later).

---

## 🧾 Summary

A structured, evolvable hospital backend applying Clean Architecture for separation of concerns, enabling safe scaling of features and maintenance.

```// filepath: /home/cassiano/github_projetos/hospitalPuc/README.md
# Hospital PUC System

A modular hospital management system implementing Clean Architecture, Clean Code and design patterns to support core clinical and administrative workflows (patients, doctors, specialties, consultations, exams, prescriptions, hospitalizations, beds, medications, insurance plans, billing).

---

## 🧠 Problem Overview

Context  
Hospitals handle many interconnected entities (patients, doctors, appointments, billing, beds). Legacy or monolithic systems are hard to evolve and test.

Real Need  
Provide a maintainable, testable, extensible backend that separates business rules from infrastructure concerns, enabling safe evolution (new modules, integrations, notifications).

Target Stakeholders  
- Administrative staff (billing, insurance, sector management)  
- Medical staff (doctors, prescriptions, exams)  
- Nursing staff (hospitalization, bed allocation)  
- IT / Dev teams (extensibility & reliability)  
- Management (reporting & data consistency)  

---

## 🎯 System Objectives

Primary Objective  
Provide a cohesive backend API for complete hospital operational management.

Secondary Objectives  
- Enforce domain rules consistently  
- Reduce coupling via explicit boundaries  
- Enable automated tests with repository spies  
- Allow future integrations (email, messaging, analytics)  

---

## ✅ Functional Requirements

| Code  | Requirement                     | Description |
|-------|---------------------------------|-------------|
| RF01  | Patient Registration            | Register, list, update, delete patients. |
| RF02  | Doctor Registration             | Manage doctors and link to specialties. |
| RF03  | Specialty Management            | CRUD of medical specialties. |
| RF04  | Consultation Scheduling         | Create consultation with future-or-today date, validate participants. |
| RF05  | Examination Management          | Register and list exams tied to patient & doctor. |
| RF06  | Prescription Management         | Link medications, patient, doctor. |
| RF07  | Medication Catalog              | CRUD medications. |
| RF08  | Hospitalization (Internação)    | Register, update, discharge hospitalization records. |
| RF09  | Bed (Leito) Management          | Track bed type, status (available/occupied). |
| RF10  | Sector Management               | Manage hospital sectors. |
| RF11  | Insurance (Convênio)            | CRUD of insurance plans. |
| RF12  | Billing (Financeiro)            | Insert & update financial records with validation. |
| RF13  | Address Linking                 | Associate patient addresses. |
| RF14  | Validation Layer                | Reject malformed inputs (Cerberus validators). |
| RF15  | Consistent Error Responses      | Standard HTTP error envelope. |
| RF16  | Future Email Notifications      | Pluggable email sender port (planned). |

---

## 🔐 Non-Functional Requirements

| Code  | Category         | Requirement |
|-------|------------------|-------------|
| NFR01 | Architecture     | Clean Architecture layering. |
| NFR02 | Testability      | Use repository spies for unit tests. |
| NFR03 | Maintainability  | Separation of domain vs infra code. |
| NFR04 | Extensibility    | New modules via composer pattern. |
| NFR05 | Consistency      | Uniform HTTP envelope & validators. |
| NFR06 | Observability    | Central error handler + console traces. |
| NFR07 | Security (future)| Add authentication & RBAC layer. |
| NFR08 | Portability      | Environment via `.env` (not committed). |
| NFR09 | Data Integrity   | Enforce foreign keys & domain checks. |

---

## 🏛 Clean Architecture Layers

- domain/  
  - Entities (models) + use case interfaces  
- data/  
  - Use case implementations + repository interfaces  
- infra/  
  - DB repositories (SQLAlchemy / PyMySQL)  
- presentation/  
  - Controllers + HTTP request/response abstractions  
- validation/  
  - Cerberus schemas per operation  
- main/  
  - Routes, composers (dependency wiring), server bootstrap  
- errors/  
  - Typed HTTP/domain error classes & handler  

Flow: Route → request_adapter → Controller → UseCase → Repository → DB → format response.

---

## 🧩 Design Patterns

- Factory / Composer pattern (dependency injection per use case)
- Repository pattern (abstract persistence)
- Adapter pattern (request adapter decouples FastAPI)
- DTO-like formatting in use cases (uniform response)
- Strategy-ready (email sender interface)
- Centralized error handling (single responsibility)

---

## 📂 Key Modules

- Patients (paciente)
- Doctors (medico)
- Specialties (especialidade)
- Consultations (consulta)
- Exams (exame)
- Prescriptions (prescricao)
- Medications (medicamento)
- Hospitalizations (internacao)
- Beds (leito)
- Sectors (setor)
- Insurance (convenio)
- Finance (financeiro)
- Address (endereco)

---

## ⚙️ Error Handling

Custom exceptions (e.g. HttpBadRequestError) bubble to `handle_errors`, which:
- Maps known errors to specific status codes
- Logs stack trace (console)
- Returns JSON body:  
```
{
  "error": [
    {"title": "<ErrorType>", "message": "<details>"}
  ]
}
```

---

## 🧪 Testing

- tests/src/infra/db/tests/* repository spies
- Validate business logic without real DB
- Future expansion: controller + use case integration tests

---

## 🛠 Tech Stack

- Python 3.12
- FastAPI (routing layer abstraction)
- SQLAlchemy Core/ORM + PyMySQL
- Cerberus (validation)
- Uvicorn (ASGI server)

---

## 🔑 Environment (.env)

Example file: `src/.env.example  
```
DB_USER=
DB_PASSWORD=
DB_HOST=localhost
DB_PORT=3306
DB_NAME=
```
Local secret file: `src/.env` (ignored via .gitignore)

---

## ▶️ Running

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp src/.env.example src/.env  # fill credentials
python run.py
```

API base: `http://127.0.0.1:8000/v1/`

---

## 🚦 Sample Endpoint Categories

| Group          | Methods |
|----------------|---------|
| /paciente      | POST, GET, PATCH, DELETE |
| /medico        | POST, GET, PATCH, DELETE |
| /consulta      | POST |
| /exame         | GET |
| /financeiro    | POST, PATCH |
| /leito         | POST, GET, PATCH, DELETE |
| /internacao    | POST, GET, PATCH, DELETE |
| ...            | (pattern consistent) |

---

## 🔄 Request Lifecycle (Example Insert)

POST /v1/medico  
1. Route → validator  
2. request_adapter builds HTTPRequest  
3. Controller maps body -> domain model  
4. Use case validates domain rules  
5. Repository persists  
6. Use case formats response → Controller → adapter returns JSON

---

## 🧱 Consistency Rules (Examples)

- Dates must follow YYYY-MM-DD
- Future constraints (e.g. finance emission date not future)
- Foreign keys validated via repository existence checks
- Enumerations validated in validator layer (status, tipo, etc.)

---

## 🌱 Future Improvements

- Authentication & JWT (RF future)
- Role-based access control
- Caching layer (bed / availability snapshots)
- Async DB and task queue for emails
- Auditing / event sourcing
- Metrics & structured logging

---

## 📌 Traceability Note

Functional requirement codes (RFxx) map to:
- Validators (validation/*)
- Use cases (data/usecases/*)
- Controllers (presentation/controllers/*)
- Routes (main/routes/*)  

---

## 📄 License

Internal / Educational (define if open-source later).

---

## 🧾 Summary

A structured, evolvable hospital backend applying Clean Architecture for separation of concerns, enabling safe scaling of features and maintenance.
