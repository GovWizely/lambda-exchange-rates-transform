# ITA Exchange Rates Transform Lambda

This project provides an AWS Lambda that queries the Open Exchange Rates API and transforms the JSON into CSV containing the required fields. 

## Prerequisites

Follow instructions from [python-lambda](https://github.com/nficano/python-lambda) to ensure your basic development environment is ready,
including:

* Python
* Pip
* Virtualenv
* Virtualenvwrapper
* AWS credentials

## Getting Started

  git clone git@github.com:GovWizely/lambda-exchange-rates-transform.git
  cd lambda-exchange-rates-transform
  mkvirtualenv -r requirements.txt lambda-exchange-rates-transform

## Configuration

* Define AWS credentials in either `config.yaml` or in the [default] section of ~/.aws/credentials.
* Edit `config.yaml` if you want to specify a different AWS region, role, and so on.
* Make sure you do not commit the AWS credentials to version control

## Invocation

  lambda invoke -v
 
## Deploy

  lambda deploy
