import aws_cdk as core
import aws_cdk.assertions as assertions

from un_injection.un_injection_stack import UnInjectionStack

# example tests. To run these tests, uncomment this file along with the example
# resource in un_injection/un_injection_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = UnInjectionStack(app, "un-injection")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
