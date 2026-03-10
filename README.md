# Orion-Context-Engine

O Orion Context Engine é uma Prova de Conceito (PoC) avançada que demonstra a viabilidade de IA Agêntica na automação de processos de gestão acadêmica. Diferente de chatbots convencionais, o Orion utiliza Function Calling para interagir diretamente com bancos de dados relacionais e regras de negócio, servindo como uma camada inteligente entre o usuário e o sistema legado.

### 🛠️ Stack Tecnológica
Backend: Java 21, Spring Boot 3.x, Spring Data JPA, H2 Database, Lombok.

AI Agent: Python 3.12, FastAPI, Google GenAI SDK (Gemini 2.5 Flash).

Frontend: Angular, TypeScript, SCSS.

### 🚀 Diferenciais Técnicos
Processamento de Linguagem Natural (NLP): Conversão de comandos textuais em operações de banco de dados (CRUD).

Arquitetura de Microsserviços: Desacoplamento total entre a interface, a lógica de IA e a persistência de dados.

Persistência Relacional: Mapeamento de entidades complexas e relacionamentos entre Editais e Bolsistas.

### 🔧 Como Executar o Laboratório
Core API: Execute o projeto Spring Boot na porta 8081.

AI Bridge: Configure sua GEMINI_API_KEY e execute o FastAPI na porta 8000.

Web Portal: Execute npm start ou ng serve e acesse localhost:4200
