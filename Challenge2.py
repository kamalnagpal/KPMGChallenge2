
import boto3
import json

user_con = boto3.Session(profile_name="default",region_name="eu-west-2")

ec2_con = user_con.resource(service_name="ec2")

print(ec2_con.instances)
#Getting data only for stopped instances by applying a filter
f1 = {
    'Name': 'instance-state-name', 
    'Values': ['stopped']
}

instances = ec2_con.instances.filter(
    Filters=[f1]
)
metadata = {} 

for instance in instances:
    metadata["instanceId"] = instance.id
    metadata["instanceType"] = instance.instance_type
    metadata["state"] = instance.state

json_object = json.dumps(metadata, indent = 4) 
print(json_object)