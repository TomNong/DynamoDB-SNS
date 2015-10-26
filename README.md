# DynamoDB-SNS
To run this examle, create the SNS topic first, run:

python create_topic_on_SNS.py

After creating the SNS topic, you can make the subscription to the end platform by comfiguring on console or run the sns_test.py, which send subscription request to the email, before that you need to find out the ARN of the topic created and replace it in responding part of the file, and don't forget input the email address, then run:

python sns_test.py

Then we can turn to DynamoDB&SNS.py, input the ARN and the credential keys firstly, then run:

python DynamoDB&SNS.py

This code will create a table while uploading items and push nortification dynamically.
