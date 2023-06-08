import boto3

ec2_client = boto3.client('ec2', region_name="eu-central-1")
ec2_resource = boto3.resource('ec2', region_name="eu-central-1")

reservations = ec2_client.describe_instances()

# From boto3 doc
for reservation in reservations['Reservations']:
    instances = reservation['Instances']
    for instance in instances:
        print(f"Status of instance {instance['InstanceId']} is {instance['State']['Name']}")


statuses = ec2_client.describe_instance_status()
for status in statuses['InstanceStatuses']:
    instance_status = status['InstanceStatus']['Status']
    system_status = status['SystemStatus']['Status']
    state = status['InstanceState']['Name']
    print(f"Instance {status['InstanceId']} is {state} with instance status {instance_status} and system status {system_status}")