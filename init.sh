#!/bin/bash

set -e

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Cores
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' 

echo -e "${BLUE}===========================================${NC}"
echo -e "${BLUE}        ORION CONTEXT ENGINE               ${NC}"
echo -e "${BLUE}===========================================${NC}"

check_docker() {
    if ! command -v docker &> /dev/null; then
        echo -e "${RED}[ERRO] Docker não instalado.${NC}"
        exit 1
    fi
    # Define o comando correto do compose
    if command -v docker-compose &> /dev/null; then
        DOCKER_COMPOSE_CMD="docker-compose"
    else
        DOCKER_COMPOSE_CMD="docker compose"
    fi
}

start_services() {
    echo -e "${YELLOW}→ Verificando integridade dos containers...${NC}"
    
    # O comando abaixo constrói silenciosamente. Se houver erro, ele para o script.
    $DOCKER_COMPOSE_CMD build -q
    
    # Sobe os containers em modo silencioso
    $DOCKER_COMPOSE_CMD up -d > /dev/null 2>&1

    echo -e "${YELLOW}→ Sincronizando microsserviços...${NC}"
    sleep 3
}

show_status() {
    echo ""
    echo -e "${BLUE}STATUS DO SISTEMA${NC}"
    echo -e "${BLUE}─────────────────────────────────────${NC}"
    # Formatação limpa dos containers ativos
    docker ps --format "  {{.Names}}" | grep "orion" | sed 's/^/  ✓ /'
}

show_urls() {
    echo ""
    echo -e "${BLUE}ENDPOINTS DISPONÍVEIS${NC}"
    echo -e "${BLUE}─────────────────────────────────────${NC}"
    echo -e "  🌐 Portal Chat:      ${GREEN}http://localhost:4200${NC}"
    echo -e "  🧠 AI Bridge:        ${GREEN}http://localhost:8002/docs${NC}"
    echo -e "  ☕ Core API (Java):   ${GREEN}http://localhost:8081/api/editais${NC}"
    echo -e "  📦 MinIO Storage:    ${GREEN}http://localhost:9001${NC}"
    echo ""
}

main() {
    check_docker
    start_services
    show_status
    show_urls
    echo -e "${GREEN}✓ Sistema operacional e pronto para uso!${NC}"
    echo ""
}

main