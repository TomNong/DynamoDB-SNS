#In this code, you will create a table named "message" in DynamoDB, creating a item containing time information and a random value every 20 seconds in that table, while push nortification to the topic, which sends messages to the end platforms

from random import randint
from time import gmtime, strftime
import boto.sns
import time
import boto.dynamodb

#set SNS region connection
connSNS = boto.sns.connect_to_region("us-east-1")
topicArn = 'TheArnOfYourSNSTopic'

#set DynamoDB connection
connDDB = boto.dynamodb.connect_to_region(
        'us-east-1',
        aws_access_key_id='YourAccessKey',
        aws_secret_access_key='YourSecretAccessKey')

#set table schema
message_table_schema = connDDB.create_schema(
        hash_key_name='forum_name',
        hash_key_proto_value=str,
        range_key_name='time',
        range_key_proto_value=str
    )

#create a table named message on DynamoDB, and set the provisioned throughput capacity and schema
table = connDDB.create_table(
        name='messages',
        schema=message_table_schema,
        read_units = 20,
        write_units = 20
    )

#get the time and random number as content
timeString = strftime("%Y-%m-%d %H:%M:%S", gmtime())
randomNum = randint(0,100)

#set the item data
item_data = {
        'Body': str(randomNum),
        'SentBy': 'EdisonA',
    }

#left time for creating table
time.sleep(5)

#push the item to the table "messages"
table = conn.get_table('messages')
item = table.new_item(
        # Our hash key is 'forum'
        hash_key='Edison Forum',
        # Our range key is 'subject'
        range_key = timeString,
        # This has the
        attrs=item_data
    )
item.put()

#push nortification to the topic
publication = connSNS.publish(topicArn, "A new item: " + str(randomNum) + " is added on Dynamo DB", subject = timeString)

#push the item and nortification in a loop
for tmp in range(0, 20):
	time.sleep(20)
	timeString = strftime("%Y-%m-%d %H:%M:%S", gmtime())
	randomNum = randint(0,100)
	item['Body'] = str(randomNum)
	item['time'] = timeString
	item.put()
	publication = conn.publish(topicArn, "A new item: " + str(randomNum) + " is added on Dynamo DB", subject = timeString)
	print "send " + str(randomNum) + " at " + timeString