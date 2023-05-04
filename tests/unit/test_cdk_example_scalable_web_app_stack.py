import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_example_scalable_web_app.cdk_example_scalable_web_app_stack import CdkExampleScalableWebAppStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_example_scalable_web_app/cdk_example_scalable_web_app_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkExampleScalableWebAppStack(app, "cdk-example-scalable-web-app")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
