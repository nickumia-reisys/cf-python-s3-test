#!/bin/bash

function vcap_get_service () {
  local path
  path="$1"
  service_name=s3-test
  echo $VCAP_SERVICES | jq --raw-output --arg service_name "$service_name" ".[][] | select(.name == \$service_name) | $path"
}

# Export S3 Configuration
export REGION_NAME=$(vcap_get_service .credentials.region)
export HOST_NAME=https://s3-$REGION_NAME.amazonaws.com
export AWS_ACCESS_KEY_ID=$(vcap_get_service .credentials.access_key_id)
export AWS_SECRET_ACCESS_KEY=$(vcap_get_service .credentials.secret_access_key)
export AWS_BUCKET_NAME=$(vcap_get_service .credentials.bucket)

export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
