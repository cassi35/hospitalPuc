# Hospital PUC System

Backend modular para gestão hospitalar aplicando Clean Architecture, separação clara de camadas, repositórios, casos de uso e pontos de extensão (e-mail, automação, analytics).

---

## 1. Objetivo Geral
Fornecer API coerente para operações clínicas, administrativas, financeiras, monitoramento operacional e geração de indicadores analíticos.

## 2. Escopo Macro
- Cadastros: pacientes, médicos, convênios, setores, leitos, medicamentos, especialidades
- Operações: consultas, internações, prescrições, exames, faturamento
- Notificações: e-mail (port SMTP)
- Analytics e Automação: relatórios, métricas assistenciais, eventos operacionais

---

## 3. Requisitos Funcionais

| Código | Requisito | Descrição Resumida |
|--------|-----------|--------------------|
| RF01 | Cadastro Paciente | CRUD completo + vínculo a endereços |
| RF02 | Cadastro Médico | CRUD + vínculo especialidades |
| RF03 | Especialidades | CRUD |
| RF04 | Agendamento Consulta | Valida data >= hoje; médico & paciente existem |
| RF05 | Exames | Registro e listagem por paciente/médico |
| RF06 | Prescrições | Vincula medicamentos, paciente, médico |
| RF07 | Medicamentos | CRUD catálogo |
| RF08 | Internações | Abrir, atualizar, dar alta |
| RF09 | Leitos | Controle status (ocupado / livre) |
| RF10 | Setores | CRUD setorial |
| RF11 | Convênios | CRUD planos |
| RF12 | Financeiro | Lançamentos e atualização validada |
| RF13 | Endereço | Associação a paciente |
| RF14 | Validação | Schemas (Cerberus) por operação |
| RF15 | Respostas de Erro | Envelope padronizado |
| RF16 | Notificação E-mail | Envio (boas-vindas, token, reset, reenvio) |
| RF17 | Relatórios Ocupação | Taxa de ocupação por setor / dia / semana |
| RF18 | Estatísticas Atendimentos | Agrupado por médico / especialidade / período |
| RF19 | Análise Financeira | Faturamento por convênio, inadimplência, ticket médio |
| RF20 | Tempo Médio Internação | Média (alta - admissão) por diagnóstico / período |
| RF21 | Indicadores Readmissão | Pacientes que retornam em < X dias |
| RF22 | Lembrete Consulta (Automação) | Gatilho e-mail/webhook X horas antes |
| RF23 | Alerta Leito Disponível (Evento) | Emissão de evento quando leito libera |
| RF24 | Gatilho Faturamento Automático | Ao dar alta → gerar lançamento financeiro |
| RF25 | Relatório Diário Automático | Gera PDF/Excel e envia para gestão |
| RF26 | Monitoramento Exceções | Log + alerta em dados inconsistentes |

### 3.1 Automação / Eventos (RF22–RF26)
| Código | Automação | Ação Técnica |
|--------|-----------|--------------|
| RF22 | Lembrete Consulta | Job scheduler (cron/async task) consulta consultas futuras |
| RF23 | Alerta Leito Livre | Observer publica evento (ex: in-memory bus) |
| RF24 | Faturamento Automático | Hook pós-alta gera registro financeiro |
| RF25 | Relatório Diário | Task gera dataset + exportador (PDF/CSV) + envio |
| RF26 | Monitor Exceções | Middleware / error handler → canal (log + futuro webhook) |

---

## 4. Requisitos Não Funcionais

| Código | Categoria | Descrição |
|--------|-----------|-----------|
| NFR01 | Arquitetura | Clean Architecture em camadas |
| NFR02 | Testabilidade | Spies e mocks para casos de uso / repositórios |
| NFR03 | Manutenibilidade | Domínio isolado de infra |
| NFR04 | Extensibilidade | Composers para injeção |
| NFR05 | Consistência | Envelope HTTP uniforme |
| NFR06 | Observabilidade | Logs estruturados (extensível) |
| NFR07 | Segurança (Futuro) | Autenticação + RBAC |
| NFR08 | Portabilidade | Config via `.env` |
| NFR09 | Integridade | FKs e validações domínio |
| NFR10 | Evolução Analytics | Camada agregadora para métricas (futuro datamart) |
| NFR11 | Isolamento SMTP | Porta (interface) desacoplada |
| NFR12 | Automação Escalonável | Ponto para fila (ex: Celery / RQ) futuro |

---

## 5. Arquitetura (Visão de Camadas)

Flow: Route → Adapter → Controller → UseCase (data) → Repository Interface → Infra Repo → DB  
Componentes:
- domain/: modelos + contratos de casos de uso
- data/: implementações de casos de uso + interfaces de repositório/serviços
- infra/: persistência (SQLAlchemy), SMTP adapter, templates
- presentation/: controllers + http abstractions
- main/: composers (wire), rotas, servidor
- validation/: schemas de entrada
- errors/: tipos + handler

Automação & Analytics (novos):
- Camada futura: analytics/ (agregações, queries especializadas)
- Camada de eventos: event bus simples (futuro) p/ RF23/RF24
- Scheduler externo (cron ou lib) para RF22/RF25

---

## 6. Modelos de Dados (Exemplos Simples)
- Paciente: id, nome, data_nascimento, convênio_id
- Internação: id, paciente_id, leito_id, dt_admissao, dt_alta
- Leito: id, setor_id, tipo, status
- Financeiro: id, tipo, valor, convênio_id, status
- Consulta: id, paciente_id, medico_id, dt_consulta

(Métricas agregadas derivadas, não persistidas diretamente.)

---

## 7. Métricas / Analytics (RF17–RF21)

| Métrica | Fonte | Método |
|---------|-------|--------|
| Ocupação (% ocupados / total) | leitos + internações ativas | Query agregada por período |
| Atendimentos por especialidade | consultas + médicos | Group by especialidade_id |
| Faturamento por convênio | financeiro | SUM(valor) FILTER(status='CONFIRMADO') |
| Ticket médio | financeiro | SUM / COUNT lançamentos |
| Tempo médio internação | internação | AVG(dt_alta - dt_admissao) |
| Readmissão | internação | Self-join por paciente dentro janela X |

---

## 8. Automação (Execução Técnica)

| Gatilho | Implementação Base |
|---------|--------------------|
| Scheduler (consultas futuras) | Função iterando repositório consultas |
| Hook pós-alta | Método no usecase alta chama gerador financeiro |
| Evento leito liberado | Update status → publica callback (extensível) |
| Export diário | Query agregada + writer CSV/PDF + envio e-mail |
| Monitor exceções | Decorator / handler central + log estruturado |

---

## 9. Tratamento de Erros
Formato:
```
{
  "error": [
    {"title": "HttpBadRequestError", "message": "Detalhe"}
  ]
}
```
Mapeamento central em `errors/error_handler.py`.

---

## 10. Notificação / SMTP
Interface: `SMTPServiceInterface`  
Implementação: `SMTPEmailService`  
Templates: `infra/email/templates/*`  
Tipos: boas-vindas, token, reset, reenvio (RF16)  
Extensível para: lembretes (RF22), relatórios (RF25).

---

## 11. Estrutura Simplificada

```
src/
  domain/
  data/
  infra/
  presentation/
  main/
  validation/
  errors/
  (futuro) analytics/
```

---

## 12. Ambiente (.env)

```
DB_USER=
DB_PASSWORD=
DB_HOST=localhost
DB_PORT=3306
DB_NAME=
MAIL_USERNAME=
MAIL_PASS=
MAIL_FROM=
MAIL_FROM_NAME=Hospital
MAIL_PORT=587
MAIL_SERVER=smtp.gmail.com
```

---

## 13. Execução

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp src/.env.example src/.env
python run.py
```
API Base: http://127.0.0.1:8000/v1/

---

## 14. Testes

```
pytest -q
```
- Repositórios: spies
- Casos de uso: isolamento via interfaces
- Futuro: métricas e automações mockadas

---

## 15. Roadmap Incremental

| Fase | Entrega |
|------|---------|
| 1 | Núcleo CRUD + validações |
| 2 | E-mail + tokens |
| 3 | Métricas operacionais (RF17–RF21) |
| 4 | Automação básica (RF22–RF24) |
| 5 | Export diário + monitoração (RF25–RF26) |
| 6 | Async tasks + filas |
| 7 | Autenticação / RBAC |

---

## 16. Licença
Uso interno / educacional (definir formalização futura).

---

## 17. Resumo Técnico
Arquitetura desacoplada, preparada para escalar: inclusão de camadas de analytics e automações sem quebrar domínio central. Requisitos RF17–RF26 adicionam visão gerencial e operacional contínua. SMTP e eventos estruturam notificações e fluxos reativos.

---

## 18. Análises Planejadas (AD01–AD05)
Conjunto inicial de indicadores operacionais e assistenciais simples de implementar, visando dashboards e alertas leves:

| Código | Análise | Descrição Técnica | Insight / Alerta |
|--------|---------|-------------------|------------------|
| AD01 | Ocupação + Tendência | Ocupação por setor (dia / semana) + média móvel 7d | Alerta se ocupação > X% por 3 dias |
| AD02 | Consultas por Especialidade | Aggregation consultas GROUP BY especialidade + janela temporal | Queda >20% vs média 4 semanas |
| AD03 | Faturamento Convênio | SUM(valor), ticket médio, % pendente por convênio | Convênio com maior inadimplência |
| AD04 | Readmissões Rápidas | Reinternações < X dias (self join internação) | Top 3 diagnósticos recorrentes |
| AD05 | Consumo & Estoque Medicamentos | Dias de cobertura = estoque / consumo médio diário | Itens com cobertura < 5 dias |

### 18.1 Estratégia Técnica
* Criar camada `analytics/` (services + queries agregadas)
* Endpoints read-only: `GET /analytics/ocupacao`, `.../consultas-especialidade`, etc.
* Possível materialização diária (tabela ou view) para ocupação → reduz custo em tempo real
* Métricas calculadas em funções puras para fácil teste (mock repos)

---

## 19. Automações Planejadas (AUTO01–AUTO05)
Eventos e rotinas leves para suporte operacional sem complexidade de filas inicialmente.

| Código | Automação | Trigger / Regra | Ação |
|--------|-----------|-----------------|------|
| AUTO01 | Alerta Baixa Disponibilidade Leitos | Leitos livres setor < 10% | E-mail / webhook operacional |
| AUTO02 | Lembrete Fatura Pendente | N dias após vencimento sem pagamento | E-mail cobrança interna |
| AUTO03 | Nudge Exame Atrasado | Exame status 'em_andamento' > 48h | Notificação responsável |
| AUTO04 | Flag Estadia Prolongada | Duração > mediana + X dias | Inserir em fila revisão clínica |
| AUTO05 | Reposição Medicamento | Estoque < limite mínimo | E-mail farmácia + log evento |

### 19.1 Implementação Inicial
* Scheduler simples (ex: APScheduler ou loop thread) varrendo regras em intervalos
* Camada `automation/` com tasks puras consumindo interfaces de repositório
* Dispatcher central (ex: `AutomationDispatcher`) para envio (e-mail / log / webhook) abstrato
* Escalável futuramente para fila (Redis/Celery) sem alterar casos de uso

---

## 20. Incremento Gradual (Plano Técnico)
| Etapa | Incremento | Dependências |
|-------|------------|--------------|
| 1 | Criar diretório `analytics/` e endpoint ocupação (AD01) | Repositórios leito & internação |
| 2 | Adicionar AD02 & AD03 | Repositórios consulta & financeiro |
| 3 | Implementar scheduler básico (AUTO01 & AUTO05) | Métricas ocupação / estoque |
| 4 | Introduzir automações restantes (AUTO02–AUTO04) | Financeiro, exames, internação |
| 5 | Materializar métricas diárias e adicionar testes unitários analytics | Infra DB |
| 6 | Abstrair dispatcher → preparar plugin fila futura | Opcional (scalability) |

### 20.1 Considerações de Simplicidade
* Sem dependência inicial de ferramentas de Big Data
* Uso de queries SQL agregadas diretas
* Alertas via mesma infraestrutura SMTP existente
* Código focado em funções puras → fácil cobertura de testes

---