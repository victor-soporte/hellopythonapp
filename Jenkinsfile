node {
  stage('Construir y Desplegar') {
    openshiftBuild bldCfg: 'hellopythonapp',
      namespace: 'development02',
      showBuildLogs: 'true'
    openshiftVerifyDeployment depCfg: 'hellopythonapp',
      namespace: 'development02'
  }
  stage('Aprobar (Pruebas)') {
    input message: 'Aprobado para Pruebas?',
      id: 'approval'
  }
  stage('Desplegar en Pruebas') {
    openshiftTag srcStream: 'hellopythonapp',
      namespace: 'development02',
      srcTag: 'latest',
      destinationNamespace: 'testing00',
      destStream: 'hellopythonapp',
      destTag: 'test'
    openshiftVerifyDeployment depCfg: 'hellopythonapp',
      namespace: 'testing02'
  }
  stage('Aprobar (Produccion)') {
    input message: 'Aprobado para Produccion?',
      id: 'approval'
  }
  stage('Desplegar en Produccion') {
    openshiftTag srcStream: 'hellopythonapp',
      namespace: 'development02',
      srcTag: 'latest',
      destinationNamespace: 'production02',
      destStream: 'hellopythonapp',
      destTag: 'prod'
    openshiftVerifyDeployment depCfg: 'hellopythonapp',
      namespace: 'production02'
  }
}
