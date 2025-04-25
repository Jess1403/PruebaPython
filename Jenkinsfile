pipeline {
    agent any  // Esto indica que Jenkins puede usar cualquier agente disponible para ejecutar el pipeline.

    stages {
        stage('Clonar código') {
            steps {
                // Clona el repositorio desde GitHub
                git 'https://github.com/tu-usuario/tu-repositorio.git'  // Cambia la URL por tu repositorio
            }
        }
        stage('Ejecutar calculadora') {
            steps {
                // Ejecuta el script de Python que tienes (en este caso calc.py)
                sh 'python3 calc.py'  // Asegúrate de que Jenkins tenga Python 3 instalado
            }
        }
    }
}
