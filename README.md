# multi-cloud-htmx

Project to automate the deployment of an HTMX web app across AWS EC2 and GCP Compute Engine. Includes SSL setup, DDOS protection, and multi-environment configurations, utilizing AWS Shield or GCP Cloud Armor.

## Features
- Deploys an HTMX web app using Docker containers.
- SSL setup with NGINX and Certbot for secure HTTPS access.
- DDOS protection via AWS Shield/GCP Cloud Armor.
- Multi-environment configurations for AWS/GCP.

## Project Structure
```
multi-cloud-htmx/
├── inventory/
│   ├── aws.yml
│   ├── gcp.yml
├── playbooks/
│   ├── deploy.yml
│   ├── setup-ssl.yml
│   ├── configure-ddos.yml
├── roles/
│   ├── common/
│   │   ├── tasks/
│   │   │   └── main.yml
│   ├── aws/
│   │   ├── tasks/
│   │   │   └── main.yml
│   ├── gcp/
│       ├── tasks/
│           └── main.yml
├── vars/
│   ├── aws.yml
│   ├── gcp.yml
└── ansible.cfg
```

## Prereqs
1. Ansible installed on your local machine.
2. SSH access to your AWS EC2 and/or GCP Compute Engine instances.
3. Docker installed on the target instances.

## Configuration
### Variables to Replace
1. `AWS_PUB_IP`: public IP address of the AWS EC2 instance
2. `GCP_PUB_IP`: public IP address of the GCP Compute Engine instance
3. `AWS_SSH_KEY_PATH`: Path to the AWS private SSH key
4. `GCP_SSH_KEY_PATH`: path to the GCP private SSH key
5. `domain_name`: domain name for the web app
6. `email`: email address for SSL certificate registration
7. `provider`: set as "aws" or "gcp" based on the deployment target
8. `resource_arn`: the ARN of the AWS resource for AWS Shield
9. `ddos_policy_name`: name of the GCP Cloud Armor policy

## Usage
1. replace the variables in `inventory` and `vars` files.
2. run the playbooks:
   - for AWS:
     ```bash
     ansible-playbook -i inventory/aws.yml playbooks/deploy.yml
     ansible-playbook -i inventory/aws.yml playbooks/setup-ssl.yml
     ansible-playbook -i inventory/aws.yml playbooks/configure-ddos.yml
     ```
   - for GCP:
     ```bash
     ansible-playbook -i inventory/gcp.yml playbooks/deploy.yml
     ansible-playbook -i inventory/gcp.yml playbooks/setup-ssl.yml
     ansible-playbook -i inventory/gcp.yml playbooks/configure-ddos.yml
     ```

## License
This project is licensed under the MIT License. See the LICENSE file for details.

