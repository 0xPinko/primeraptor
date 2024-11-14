
# Primeraptor

Primeraptor is a Terraform-powered tool for deploying Velociraptor servers on AWS with speed and efficiency. Designed for quick, automated setup of forensic analysis and incident response, Primeraptor allows easy customisation of IP whitelisting, instance types, and storage. After deployment, Primeraptor sends you an email with all essential details for the Velociraptor admin server, including IP address, username, password, and an S3 link for client binaries. You'll need to verify your designated email before the installation process begins. Deployment typically completes in just 4–6 minutes.

## Requirements

- **Terraform**: [Download Terraform](https://www.terraform.io/downloads.html)
- **AWS CLI**: [Download AWS CLI](https://aws.amazon.com/cli/)

## Installation

### 1. Install Terraform and AWS CLI

- Download and install **Terraform** from the [Terraform website](https://www.terraform.io/downloads.html).
- Download and install the **AWS CLI** from the [AWS CLI website](https://aws.amazon.com/cli/).

### 2. Set Terraform in System PATH

Make sure the path to `terraform.exe` is included in your system’s PATH.

1. Open **System Properties** > **Environment Variables**.
2. Under **System variables**, find `Path`, click **Edit**, and add the directory containing `terraform.exe` if it’s missing (e.g., `C:\Program Files\Terraform`).
3. Restart your terminal to apply the changes.

### 3. Configure AWS CLI

Run `aws configure` to set up your AWS credentials:
```bash
aws configure
```
### 4. Run Primeraptor
Once you've set up Terraform and AWS CLI, navigate to the primeraptor directory and run the `primeraptor.py` script:
```bash
python primeraptor.py
```
