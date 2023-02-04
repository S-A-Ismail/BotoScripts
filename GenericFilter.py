import boto3
import pandas as pd

ImageIdList = []
SnapshotIdList = []
InstanceIdList = []

ec2 = boto3.resource('ec2')
def tagfilter(Resource, NoOfKeys): 
    for i in range(NoOfKeys):
        temp_key=input("Enter tag Key: ")
        temp_value=input("Enter tag Value: ")
        tag_key.append(temp_key)
        tag_value.append(temp_value)
    for i in NoOfKeys:
        print(tag_key[i])
        print(tag_value[i])
    FilterJson = []
    dict_key1 = "Name"
    dict_key2 = "Values"
    for i in range(NoOfKeys):
        temp_result = {dict_key1: "tag:"+tag_key[i], dict_key2: [tag_value[i]]}
        FilterJson.append(temp_result)
    if (Resource = "Instance"):
        resources = ec2.instance.filter(Filters=FilterJson)
        with open("./data/FilteredByTagInstances.txt", "w") as f:
            for r in resources:
                InstanceId = r.id
                InstanceIdList.append(InstanceId)
                f.write(str(InstanceId) + ',\n')
    elif (Resource = "Image"):
        resources = ec2.images.filter(Filters=FilterJson)
        with open("./data/FilteredByTagImages.txt", "w") as f:
            for r in resources:
                ImageId = r.image_id
                ImageIdList.append(ImageId)
                f.write(str(ImageId) + ',\n')
    elif (Resource = "Snapshot"):
        resources = ec2.snapshots.filter(Filters=FilterJson)
        with open("./data/FilteredByTagSanpshots.txt", "w") as f:
            for r in resources:
                SnapShotId = r.snapshot_id
                SnapshotIdList.append(SnapShotId)
                f.write(str(SnapShotId) + ',\n')
    else:
        print("Please enter right Resource/Key Values")


Resource = input("Enter the type of EC2 resource (Instance/Image/Snapshot): ")
NoOfKeys = input("Enter number of Tag Values you want to Filter by: ")
try:
    int(NoOfKeys)
except:
    print("Please enter Numeric Value!")
    NoOfKeys = input("Enter number of Tag Values you want to Filter by: ")

if (Resource != 'Instance' or Resource != 'Image' or Resource != 'Snapshot' and NoOfKeys <= 0):
    print("rerun with correct values")
else:
    tagfilter(Resource, NoOfKeys)