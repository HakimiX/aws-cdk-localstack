#!/usr/bin/env python3
import os

import aws_cdk as cdk

from aws_cdk_localstack.aws_cdk_localstack_stack import AwsCdkLocalstackStack
from aws_cdk_localstack.lambda_stack import LambdaStack

app = cdk.App()
#AwsCdkLocalstackStack(app, "AwsCdkLocalstackStack")

LambdaStack(app, 'LambdaStack')

app.synth()
