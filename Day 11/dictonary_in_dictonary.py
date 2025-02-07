ec2_instance_info = [
    {
        "id" : "instance-001",
        "type" : "t2.micro"
    },
    {
        "id" : "instance-002",
        "type" : "m5.large"
    },
    {
        "id" : "instance-003",
        "type" : "c5.xlarge"
    }
]

print(ec2_instance_info)
print(ec2_instance_info[1]["id"])