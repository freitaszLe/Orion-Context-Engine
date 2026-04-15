# Estágio 1: Build com Maven
FROM maven:3.9.6-eclipse-temurin-21 AS build
WORKDIR /app

# Força o encoding para evitar o erro MalformedInputException
ENV MAVEN_OPTS="-Dfile.encoding=UTF-8"

# Copia apenas o POM primeiro para aproveitar o cache das dependências
COPY pom.xml .
RUN mvn dependency:go-offline

# Copia o código fonte e compila
COPY src ./src
RUN mvn clean package -DskipTests

# Estágio 2: Execução
FROM eclipse-temurin:21-jre-jammy
WORKDIR /app

# Instala curl para o healthcheck
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

COPY --from=build /app/target/*.jar app.jar

EXPOSE 8081

# Configurações de performance da JVM
ENTRYPOINT ["java", "-Dfile.encoding=UTF-8", "-XX:+UseContainerSupport", "-XX:MaxRAMPercentage=75.0", "-jar", "app.jar"]