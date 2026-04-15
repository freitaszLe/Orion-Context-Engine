# Estágio de build - Usando Node 22 para compatibilidade
FROM node:22 AS build
WORKDIR /app

# Copia arquivos de dependência
COPY package*.json ./
RUN npm install

# Copia o código e gera o build
COPY . .
RUN npm run build

# Estágio de execução - Servidor Nginx
FROM nginx:alpine

# O NOME DA PASTA NO DIST: 
# O seu log mostrou "chat-ui@0.0.0 build". 
# Geralmente o Angular gera a pasta com o nome que está no package.json.
# Vou usar um curinga (*) para garantir que ele ache a pasta certa.
COPY --from=build /app/dist/*/browser /usr/share/nginx/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]