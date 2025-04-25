pipeline {
    agent any

    stages {
        stage('Verificar Python') {
            steps {
                // Verifica si Python 3 está instalado
                sh 'python3 --version'
            }
        }
        stage('Clonar código') {
            steps {
                git 'https://github.com/Jess1403/PruebaPython.git/'
            }
        }
        stage('Ejecutar calculadora') {
            steps {
                sh 'python3 main.py'
            }
        }
    }
}

