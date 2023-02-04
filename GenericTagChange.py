import boto3
import pandas as pd

resource_type = 'ec2'
resource_client = boto3.client(resource_type)

ResourceIdList = []

def tagchanger(Resource):
    new_tag_key=input("Enter tag Key: ")
    new_tag_value=input("Enter tag Value: ")
    with open("./data/Changed"+str(Resource)+".txt", "w") as f:
        with open("./data/Excepted"+str(Resource)+".txt", "w") as d:
            for item in ResourceIdList:
                try:
                    resource_client.create_tags(
                        DryRun=False,
                        Resources=[ResourceIdList[item]],
                        Tags=[
                            {
                                'Key': new_tag_key[item],
                                'Value': new_tag_value[item]
                            }
                        ]
                    )
                    f.write(str(ResourceIdList[item])+',\n')
                    ChangedResourceList.append(ResourceIdList[item])
                except:
                    d.write(str(ResourceIdList[item])+',\n')
                    ExceptedResourceList.append(ResourceIdList[item])
                    pass

Resource = input("Enter the type of EC2 resource (Instance/Image/Snapshot): ")

if (Resource != 'Instance' or Resource != 'Image' or Resource != 'Snapshot'):
    print("rerun with correct values")
else:
    tagchanger(Resource)