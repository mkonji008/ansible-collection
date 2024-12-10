# Ansible Collection

A personal collection of Ansible playbooks for configuration management and deployments across different environments. This repository includes a variety of projects, and I plan to add more as I refine and organize content from a larger private repository of mine.

## Ansible Projects

### AWS
- [**aws-ec2-htmx**](https://github.com/mkonji008/ansible-collection/tree/aws-ec2-htmx)  
  *HTMX on AWS EC2*
  - Deploys a minimal HTMX container app on AWS EC2, featuring NGINX and Certbot for SSL certification.

### GCP
- [**gcp-gke-hugo-htmx**](https://github.com/mkonji008/ansible-collection/tree/gcp-gke-hugo-htmx)  
  *HUGO + HTMX on GKE in GCP*
  - Sets up a Hugo static site with HTMX integration for dynamic elements, deployed on a GKE cluster in GCP.

---

### Projects yet to be scrubbed and added. 

1. **Multi-Environment Kubernetes Cluster Deployment**
   - Deploys Kubernetes clusters on AWS (EKS) and GCP (GKE) using Ansible and Terraform. Configures separate environments (dev, staging, prod) with secure networking and monitoring. Hosts a microservices-based metabase/redash along with API Gateway/Service Mesh.
   - This was a larger project and will will receive it's own repo due to scope once I scrub it...  Personal note to link it here as well as my [Terraform Collection](https://github.com/mkonji008/terraform-collection) repo.

2. **HTMX Application with Multi-Cloud Load Balancer**
   - Automates deployment of an HTMX web app across AWS EC2 and GCP Compute Engine. Includes SSL setup, DDOS protection, and multi-environment configurations. Uses AWS Shield or GCP Cloud Armor for security. Larger in scope but fully deployable with Ansible.
   - Partially scrubbed and entirely using Ansible so it will make it into this repo.

3. **Cloud-Native CI/CD Pipeline with Jenkins and CircleCI**
   - Sets up Jenkins and CircleCI for hybrid CI/CD pipelines, managing multi-environment deployments (dev, staging, prod) using Docker and Kubernetes. Jenkins handles legacy tasks while CircleCI manages the modern workflows. Deployed on AWS and GCP using Ansible, Terraform, and Helm for infrastructure and app deployment.
   - Partially scrubbed but large in scope so it will get it's own repo...  Personal note to link it here as well as my [Terraform Collection](https://github.com/mkonji008/terraform-collection) repo.

4. **Redis & PostgreSQL High Availability Setup**
   - Configures a highly-available Redis and PostgreSQL cluster using Ansible on AWS/GCP. Automates failover, backups, and monitoring for a **cough** very bloated (Node.js) app using Redis for caching and PostgreSQL as the main database.
   - Not scrubbed, fully using Ansible and ***could*** be in this repo. Less interested in migrating this over as the node app was a massive dependency hell anyways, so having to accomidate for it bloated the inf provisioning and deployment automation as well. *Node.... right?*
      
5. **Multi-Environment ELK Stack with Fluentd Integration**
   - Sets up a scalable ELK Stack on GCP using Ansible to manage centralized logging across multiple environments. Fluentd collects logs from whatever microservice app you are wanting this to integrate this into, sending them to Logstash and Elasticsearch for storage and analysis. Kibana is used for real time log monitoring, and the setup is designed for scalability and high availability.
   - Not started scrubbing my private lab repo yet. All deployed and configured using Ansible so it will be added here eventually when I have the time.

6. **Nginx Reverse Proxy with SSL and DNS Configuration**
   - Sets up an Nginx reverse proxy on GCP with SSL and DNS management. Routes traffic between a React frontend and Go API backend in a dev environment for testing features.
   - Not started scrubbing, all using Ansible and will get to it at some point.

7. **Serverless API with Ansible Automation**
   - Deploy a cost efficient serverless API with AWS Lambda. Integrates with a Go-based backend via API Gateway. Includes monitoring and supports multiple environments for development and testing. This was used for video processing but generalizing the Ansible project for sake of versatility. 
   - Not yet scrubbed. Higher priority due to using this for an easy POC. 

8. **HCP Vault & Consul Deployment**
   - Sets up HashiCorp Vault and Consul clusters using Ansible on AWS/GCP. Configures secure secret management and service discovery for a Go-based API service. Includes multi-region setup and disaster recovery... secrets are kinda important.
   - Sensitive stuff but all personal POC anyways, I'll get to this eventually as well.

9. **CockroachDB Multi-Region Cluster**
   - Deploys a multi-cloud, multi-region CockroachDB cluster across AWS and GCP. Configures multi-environment support and automated backups for a Go application backend.
   - A more recent project that I'll scrub sooner than later while it's all fresh in my mind.
     
10. **Helm Chart Repository with Ansible Automation**
    - Automates the creation of a private Helm chart repository on AWS S3 and GCP GCS. Hosts Helm charts for Redis, Nginx, and PostgreSQL with secure access and multi-environment support. Integrates with Jenkins ci/cd.
    - Common project with many examples so less focused on getting this added to the repo at the moment.

  --- 
#### There are more to add but will start with these initial 10. 
