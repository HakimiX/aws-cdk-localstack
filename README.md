# AWS CDK Localstack 


### Overview

### AWS CLI
It's possible to specify the endpoint when using the AWS CLI, so instead of sending the requests to the cloud directly, they will be sent to Localstack. 
```shell
aws --endpoint-url=http://localhost:4566 apigateway get-rest-apis
```

