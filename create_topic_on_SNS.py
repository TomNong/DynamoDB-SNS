#make a sns connection on us-east-1 server, create a topic named "sns_email", make subcription on your email, you may have to confirm on your email, if it doesn't work, enable the policy of topic for publish to everyone in AWS SNS console
import boto.sns

#set the SNS region
conn = boto.sns.connect_to_region("us-east-1")
topicname = "sns_email"
topicArn = conn.create_topic(topicname)['CreateTopicResponse']['CreateTopicResult']['TopicArn']
subscription = conn.subscribe(topicArn, "email", "YourEmail")
