pipeline {
    agent any

    stages {
        stage('Clonar código') {
            steps {
                // Asegúrate de que la URL sea correcta y tu repositorio esté accesible
                git branch: 'main', url: 'https://github.com/Jess1403/PruebaPython.git'
            }
        }

        stage('Ejecutar calculadora') {
            steps {
                // Ejecutar el script de Python
                sh 'python3 main.py'
            }
        }
    }
}
