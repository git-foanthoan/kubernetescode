node {
    def app

    stage('Clone repository') {
        checkout scm
    }

    stage('Build image') {
        app = docker.build("foanthoan/test")
    }

    stage('Push image') {
        docker.withRegistry('', 'dockerhub') {
            // Use --password-stdin for better security
            app.push("${env.BUILD_NUMBER}", "--password-stdin")
        }
    }

    stage('Trigger ManifestUpdate') {
        echo "triggering updatemanifestjob"
        build job: 'updatemanifest', parameters: [string(name: 'DOCKERTAG', value: env.BUILD_NUMBER)]
    }
}
