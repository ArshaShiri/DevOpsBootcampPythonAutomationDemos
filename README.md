# DevOps Bootcamp Python Automation Demosco

## check_server_status

Schedule library is used: `pip install schedule`
Check the status of the servers.

## add-env-tags
Add prod tags to the servers in Paris and add dev tag to servers in Frankfurt.

## eks-status-checks.py
Checks
* EkS cluster status
* Which kubernetes version is used
* Cluster endpoint

## volume-backups.py
Automating backups of EC2.

## cleanup-snapshots.py
Automation of the snapshot cleanup.

## restore-volume.py
Restoring the EC2 instance from the latest snapshot.

## monitor-website.py
Monitoring a website that is running on linode.

In Linode the following server is created:
![image](https://github.com/ArshaShiri/DevOpsBootcampPythonAutomationDemos/assets/18715119/df297925-cdad-41cf-8b03-155cb035a367)

We then install docker on our server: https://docs.docker.com/engine/install/debian/
Subsequnely, we install the nginx container.

    docker run -d -p 8080:80 nginx

We can access the running nginx on port 8080:

![image](https://github.com/ArshaShiri/DevOpsBootcampPythonAutomationDemos/assets/18715119/6dfdcf3b-74ae-4a1d-bfad-65357bae8688)
