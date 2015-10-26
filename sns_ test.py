#this code will push a nortification to the subscribed platform
import boto.sns

#set the SNS region
conn = boto.sns.connect_to_region("us-east-1")
topicArn = 'TheArnOfYourTopic'

#configure the content of the nortification and push it to the topic
message = "hello, sns works"
message_subject = "aws sns"
publication = conn.publish(topicArn, message, subject=message_subject)