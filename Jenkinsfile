pipeline{
    agent any
    stages{
        stage("Checkout"){
            steps{
                git 'https://github.com/cubesrepo/openCartAwesomeQA.git'
            }
        }
        stage("Install dependencies and setup"){
            steps{
                bat 'python -m venv opencartVENV'
                bat 'opencartVENV\\Scripts\\activate and pip install -r requirements.txt'
            }
        }
        stage("Run test"){
            steps{
                bat 'opencartVENV\\Scripts\\activate and pytest -v --html=report.html'
            }
        }
    }
}