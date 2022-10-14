# AWS CDK Localstack 

### Prequisites
1. Install CDK Localstack CLI
```shell
npm install -g aws-cdk-local aws-cdk
```
2. Start localstack 
```shell
cd localstack-playground
docker-compose up

# check availability
http://localhost:4566/health
```
3. Bootstrap CDK environment _(localstack must be running)_
```shell
cdklocal bootstrap

> "CDKToolkit: creating CloudFormation changeset..."
  "✅  Environment aws://000000000000/eu-west-1 bootstrapped."
```

### Deploy 
**Deploy** CDK infrastructure 
```shell
cdklocal deploy
```
**Invoke** API Gateway
```shell
# endpoint: /something 
curl -XPOST "https://<api-gateway>.localstack.cloud:4566/prod/something" -d "{\"name\":\"bob\"}"

# endpoint: /another
curl "https://<api-gateway>.localhost.localstack.cloud:4566/prod/another"
```


### cdklocal commands
```shell
cdklocal ls
cdklocal synth
cdklocal diff
cdklocal deploy
cdklocal destroy
```

### Sources

* [Localstack Guide](https://dev.to/_mikigraf/localstack-cdk-local-aws-development-58ff)