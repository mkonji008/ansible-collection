# HTMX AWS Deployment using Ansible

  This setup deploys an HTMX container on an AWS EC2 instance using Ansible. The playbook sets up NGINX as a reverse proxy with SSL and rate limiting, providing basic DDoS protection. 

  I chose not to containerize NGINX because managing SSL certificates with Certbot is simpler on a system installation. Additionally, having NGINX and the application on separate containers adds networking complexity and slight resource overhead, which can impact performance on smaller instances.

## Prerequisites
1. AWS Free Tier account with IAM permissions.
2. An EC2 key pair (update `hosts.ini` with your private key path).
3. Domain name registered in Route 53 or another DNS provider.
4. Docker image for the HTMX app (see `vars/main.yml`).

## Setup Instructions
1. **Inventory**  
   Update `inventory/hosts.ini` with the public IP of the EC2 instance.

2. **Variables**  
   Update `vars/main.yml` with:
   - `domain_name`: Your domain name.
   - `htmx_app_image`: Docker image for HTMX app.
   - `rate_limit`: Request rate limit to help mitigate excessive access.
   - `aws_region`: Your preferred AWS region.
   - `certbot_email`: Email for SSL registration and notifications.

3. **Deploy**  
   Run the playbook with the following command:
   ```bash
   ansible-playbook -i inventory/hosts.ini playbooks/deploy_htmx.yml

## HTMX Application

This includes a simple baseline HTMX web application built using Flask. It has basic interactivity by sending requests to the server and updating the web page dynamically without a full reload. It's what I use as a baseline.

### Application Details

- The HTMX app is built as a Docker image during deployment, using the provided Dockerfile and source code in the `roles/htmx_app` directory.
- The application serves a simple button that, when clicked, fetches a greeting message from the server using HTMX.

## Notes

- **DDoS Protection**: Basic protection is provided by NGINX rate limiting.
- **SSL Setup**: Certbot automatically obtains and renews SSL certificates using Let's Encrypt.
