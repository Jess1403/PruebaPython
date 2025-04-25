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
                // Clona el repositorio desde GitHub
                git 'https://github.com/Jess1403/PruebaPython.git/'
            }
        }
        stage('Ejecutar calculadora') {
            steps {
                // Asegúrate de que el script main.py esté en el directorio correcto
                sh 'ls -l'  // Lista los archivos del directorio actual
                sh 'python3 Calc.py'  // Ejecuta el script Python
            }
        }
    }
}
