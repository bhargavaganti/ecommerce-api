
function run_dev() {
    echo "Starting development project..."
    docker-compose down
    docker-compose -f docker-compose.yml -f docker-compose.dev.yml up --build
}

function run_prod() {
    echo "Starting production project..."
    docker-compose down
    docker-compose -f docker-compose.yml -f docker-compose.prod.yml up --build
}

function clean_up() {
    echo "Cleaning containers..."
    docker-compose down
}

function help_menu() {
cat << EOF
Usage: ${0} (d | p | c | h)

OPTIONS:
    d|dev       Run development environment
    p|prod      Run production environment
    c|clean     Stop and clean docker containers
    h|help      Show this message
EOF
}


if [[ $# == 0 ]]; then
    help_menu
elif [[ $1 == "prod" ]] || [[ $1 == "p" ]]; then
    run_prod
elif [[ $1 == "dev" ]] || [[ $1 == "d" ]]; then
    run_dev
elif [[ $1 == "clean" ]] || [[ $1 == "c" ]]; then
    clean_up
else
    help_menu
fi
