#!/bin/sh
echo "#### Starting the site's CI/CD process ####"
if [ -z "$S3_BUCKET_NAME" ]; then # if there's no bucket name specified, skip the deployment
    echo "#### Dev environment. Skipping the site deployment ####"
else 
    echo "#### Deploying the site ####"
    ./deployment.py 2> deployment_errors.txt #redirect all the error messages from the deployment
    deployment_result=$(grep -i "exception" deployment_errors.txt) 
    if [ -n "$deployment_result" ]; then # if the file's contents aren't empty, there were errors
        echo "Deployment failed with the following message(s):"
        cat deployment_errors.txt
        echo "Stopping the next tests"
        exit 1
    fi
fi
if [ "$ENVIRONMENT" == "production" ]; then
    echo "#### Production environment. Skipping the tests ####"
    exit 0
fi
echo "#### Running the tests ####"
./tests.py 2> errors.txt # redirect all the stderr to the errors.txt file
test_result=$(grep -i "failure" errors.txt) #search in the file if the tests failed
if [ -n "$test_result" ]; then
    echo "Tests failed with the following message(s):"
    cat errors.txt
    exit 1
fi
echo "#### Tests passed ####"