# AWS CDK Localstack 

### Prequisites
1. Install CDK Localstack CLI
```shell
npm install -g aws-cdk-local aws-cdk
```
2. Start localstack 
```shell
localstack start # do not use localstack with docker-compose due to issues with ecr

# Status
localstack status services

# Check availability
http://localhost:4566/health
```
> [Localstack Guide](https://github.com/HakimiX/localstack-playground)

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
curl -XPOST "https://<api-gateway>.localhost.localstack.cloud:4566/prod/something" -d "{\"name\":\"bob\"}"

# endpoint: /another
curl "https://<api-gateway>.localhost.localstack.cloud:4566/prod/another"
```

### Destroying and deploying again
Whenever you destroy the stack, you HAVE to bootstrap the environment
again before deploying.
```shell
cdklocal destroy
cdklocal bootstrap
cdklocal deploy
```

### Sources

* [Localstack Guide](https://dev.to/_mikigraf/localstack-cdk-local-aws-development-58ff)