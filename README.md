## Personal collection of Ansible projects and playbooks.

### See the main branch for other projects... [ansible-collection](https://github.com/mkonji008/ansible-collection)

### gke deployment for hugo + htmx site

#### This playbook is a baseline for a hugo static site that leverages htmx for dynamic elements and deploying a hugo site with htmx integration on a gke cluster in gcp.

**what we're doing:**

- set up gke cluster
- deploy hugo site using helm chart
- configure htmx integration

**requirements:**

- gcp project and service account
- kubectl configured

**how to use:**

1. replace placeholders in `vars.yaml` with your values.
2. run `ansible-playbook main.yml`.

optional flags: (obvious ansible flags but healthy reminder)

- `-v`: increase verbosity for more detailed output.
- `-vv`: even greater verbosity for debugging purposes.
- `-l SUBSET`: run tasks only for specific hosts in the inventory (if applicable).
- `--check`: perform a dry run without making any changes (useful for testing).

**3. access your hugo site :**

If the deployment is successful, the `main.yml` will print the external IP address of your Hugo service (assuming an exposed LoadBalancer service). You can then access your site by opening that IP address in a web browser.

### note

- this is a example built from a working project that was tasked to me. it needed to be repeatable with minimal configuration and use existing hugo and htmx repos
- modify and adapt based on your specific needs if you run across this perchance

### further reading

- ansible documentation: [https://docs.ansible.com/platform.html](https://docs.ansible.com/platform.html)
- gcp project and service account: [https://developers.google.com/workspace/guides/create-project](https://developers.google.com/workspace/guides/create-project)
- kubectl configuration: [https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/)
