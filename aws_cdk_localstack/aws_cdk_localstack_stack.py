from aws_cdk import (
    Duration,
    Stack,
    aws_iam as iam,
    aws_lambda as lambda_,
    aws_apigateway as api_gw
)
from constructs import Construct


class AwsCdkLocalstackStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        lambda_role = iam.Role(
            scope=self,
            id="lambdaRole",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "service-role/AWSLambdaBasicExecutionRole"
                ),
            ],
        )
        
        #lambda_function = lambda_.Function(
        #    self, 'localstackLambda',
        #    runtime=lambda_.Runtime.PYTHON_3_9,
        #    handler="lambda.handler",
        #    role=lambda_role,
        #    code=lambda_.Code.from_asset('lambda'))

        lambda_function = lambda_.DockerImageFunction(
            self,
            'localstackDockerLambda',
            timeout=Duration.minutes(15),
            code=lambda_.DockerImageCode.from_image_asset(
                directory='./lambda_container',
                file='Dockerfile'
            ),
            role=lambda_role,
            environment={
                "SOMETHING": "bob1234"
            }
        )
        
        api = api_gw.RestApi(
            self,
            "sampleApiGateway",
            policy=iam.PolicyDocument(),
            deploy_options=api_gw.StageOptions(tracing_enabled=True)
        )

        integration = api_gw.LambdaIntegration(
            handler=lambda_function,
            proxy=True,
            allow_test_invoke=True,
            request_templates={
                "application/json": "$input.body"
            }
        )

        resource = api.root.add_resource("something")
        resource.add_method(
            "POST",
            integration=integration
        )

        index_resource = api.root.add_resource('another')
        index_resource.add_method(
            "GET",
            integration=integration
        )
