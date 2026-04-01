#  Orion Context Engine
### Agente Autônomo Inteligente para Integração com Sistemas Corporativos

O **Orion Context Engine** é uma Prova de Conceito (PoC) desenvolvida como Trabalho de Conclusão de Curso (TCC), que propõe a utilização de **Inteligência Artificial Generativa como agente autônomo** para interação com sistemas corporativos reais.

O projeto transforma um modelo de linguagem (LLM) em um **orquestrador inteligente de processos**, capaz de interpretar linguagem natural, executar ações no sistema e respeitar regras de negócio institucionais.

---

## Objetivo

Demonstrar a viabilidade de utilização de **IA Agêntica** em ambientes corporativos, promovendo:

- Automação de fluxos complexos
- Redução da dependência de interfaces tradicionais
- Interação natural com sistemas legados
- Respeito rigoroso às regras de negócio

---

## Conceito Central

Diferente de chatbots tradicionais, o Orion atua como um:

> **Agente Cognitivo Autônomo baseado em Model Context Protocol (MCP)**

Ou seja, ele:
- Interpreta intenção do usuário
- Decide qual ação executar
- Chama funções reais do sistema (API)
- Interpreta respostas (inclusive erros de negócio)
- Responde de forma natural

---

## 🏗️ Arquitetura do Sistema

A arquitetura segue o princípio de **separação total de responsabilidades**:

### 🔹 1. Web Portal (Frontend)
Interface Angular responsável pela interação com o usuário.

### 🔹 2. AI Bridge (Orquestrador - MCP)
Middleware em Python que:
- Recebe prompts
- Disponibiliza ferramentas (tools)
- Encaminha chamadas para o backend
- NÃO contém regras de negócio

### 🔹 3. Core API (Backend Java)
Responsável por:
- Regras de negócio
- Persistência de dados
- Validações institucionais

### 🔹 4. LLM (Camada Cognitiva)
Modelo Llama 3.1 rodando localmente via Ollama.

---

## 🛠️ Stack Tecnológica

| Camada | Tecnologia |
|------|--------|
| Backend | Java 21 + Spring Boot |
| IA Bridge | Python + FastAPI |
| LLM | Llama 3.1 (Ollama) |
| Frontend | Angular + TypeScript |
| Banco | H2 / PostgreSQL |

---

## ⚙️ Funcionalidades Implementadas

- 📄 Listagem de editais
- 👨‍🎓 Listagem de bolsistas
- 🔗 Vinculação de bolsistas a editais
- 🧠 Interpretação de regras de negócio via IA
- 🚫 Bloqueio automático (ex: IRA insuficiente)
- 🔄 Tradução de erros técnicos em linguagem natural

---

## Diferenciais Técnicos

### ✔️ IA sem acesso direto à regra de negócio
A IA **não toma decisões críticas diretamente** — ela apenas orquestra.

### ✔️ Segurança institucional
As regras são validadas exclusivamente no backend Java.

### ✔️ Combate à alucinação
Uso de ferramentas explícitas (Function Calling controlado).

### ✔️ Arquitetura escalável
Separação em camadas permite evolução independente.

---

## 🔄 Fluxo de Execução

1. Usuário envia comando em linguagem natural  
2. IA interpreta intenção  
3. IA escolhe ferramenta (tool)  
4. Orquestrador chama API Java  
5. Backend valida regras  
6. Resposta retorna (sucesso ou erro)  
7. IA traduz para linguagem natural  
<img width="1976" height="2743" alt="mermaid-diagram-2026-04-01-121943" src="https://github.com/user-attachments/assets/ddcb9610-a7b5-4fc3-85a2-83023caf5824" />

---

## Como Executar o Projeto

### Pré-requisitos
- Java 21
- Python 3.12
- Node.js 18+
- Angular CLI
- Acesso ao servidor do Llama (SSH)

---

### 🔹 1. Backend (Spring Boot)

```bash
cd core-api
./mvnw spring-boot:run
```

Rodando em: http://localhost:8081

### 🔹 2. Túnel SSH (LLM)

### 🔹 3. AI Bridge (FastAPI)
```bash
cd ai-bridge
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8002
```

### 🔹 4. Frontend (Angular)
```bash
cd web-portal
npm install
ng serve
```

Acesse: http://localhost:4200

## 🧪 Como Testar

#### Exemplos de prompts:

- Liste os editais disponíveis
- Liste os bolsistas
- Vincule João da Silva ao edital de pesquisa

#### Comportamento esperado:

execução de ações válidas;
bloqueio de ações inválidas;
explicação natural quando houver impedimento por regra de negócio.

## 📊 Contribuição Acadêmica

Este trabalho contribui para estudos relacionados a:

- IA aplicada a sistemas corporativos;
- arquiteturas baseadas em agentes autônomos;
- integração de LLMs com APIs reais;
- uso de MCP (Model Context Protocol) em cenários institucionais.

### 👩‍💻 Autora

Letícia Arruda de Freitas
Engenharia da Computação - IFMT

### 📌 Status do Projeto

Em desenvolvimento — versão acadêmica funcional.
