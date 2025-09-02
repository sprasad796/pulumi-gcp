"""A Google Cloud Python Pulumi program"""

import pulumi
import pulumi_gcp as gcp
from pulumi_gcp import storage

# Create a GCP resource (Storage Bucket)
#bucket = storage.Bucket('my-bucket', location="US")

# Export the DNS name of the bucket
#pulumi.export('bucket_name', bucket.url)
pulumi.export("a", "banana")
pulumi.export("b", pulumi.Output.secret("miaow"))
pulumi.export("c", pulumi.Output.secret("woof"))
pulumi.export("d", pulumi.Output.secret({"a": 1, "b": 2}))

#Config
config = pulumi.Config();
print('config: {}',config);
