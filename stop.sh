#!/bin/bash

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
RED='\033[0;31m'
NC='\033[0m'

echo ""
echo -e "${RED}→ Encerrando Orion Context Engine...${NC}"

cd "$PROJECT_ROOT"

if command -v docker-compose &> /dev/null; then
    docker-compose down
else
    docker compose down
fi

echo -e "${RED}✓ Todos os serviços foram parados.${NC}"
echo ""