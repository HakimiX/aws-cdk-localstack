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
```shell
cdklocal ls
cdklocal diff
cdklocal deploy
cdklocal destroy
```

### Sources

* [Localstack Guide](https://dev.to/_mikigraf/localstack-cdk-local-aws-development-58ff)