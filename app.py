#!/usr/bin/env python3
import os

import aws_cdk as cdk

from aws_cdk_localstack.aws_cdk_localstack_stack import AwsCdkLocalstackStack


app = cdk.App()
AwsCdkLocalstackStack(app, "AwsCdkLocalstackStack")

app.synth()
