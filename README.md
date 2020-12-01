# GitHub Actions SAM Deployment Example
The purpose of this repository is to illustrate a GitHub Actions pipeline deploying a SAM template.

In this particular example we are deploying Amazon API Gateway, AWS StateMachine, AWS Lambda Functions, and corresponding IAM Roles.

## How it Works

There are two workflows `sam-validate-build-test-deploy` and `sam-validate-build-test`.

In this repository's current configuration, deployment only occurs when changes land into the `main` branch. This is seen within the `.github/workflows/sam-validate-build-test-deploy.yml` file:
```
on:
  push:
    branches: [ main ]
```

For all `other branches`, we will run the `sam-validate-build-test` workflow when pull requests are created. This ensures that the code they are looking to merge passes the `sam validate` and `sam build` steps.
```
on:
  pull_request:
    branches: [ main ]
```

## How To Configure
* Fork this repo and update the code and SAM template to reflect the code you are looking to deploy.
* Within the Repository settings for your fork or repo, create the following `Secrets` to configure the permissions to be used by the GitHub Actions pipeline:
```
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_SESSION_TOKEN
AWS_REGION
```

Please note the `AWS_SESSION_TOKEN` is optional, but preferable.