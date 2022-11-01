# cf-python-s3-test
Test Python Boto connection to S3 on cloud.gov through egress-proxy app

```
cf create-service s3 basic-public s3-test
cf push s3-test --vars-file vars.development.yml
```
