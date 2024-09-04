Project Description

This project involves setting up a monitoring and stress testing environment using Prometheus, Grafana, MySQL, and various exporters on multiple virtual machines. The setup aims to monitor CPU, memory, disk, and SQL performance and send alerts based on predefined rules.

Infrastructure Setup

vm_0: Virtual machine for running the Prometheus server.
vm_1: Virtual machine for running the MySQL server.
vm_2: Virtual machine for running the Grafana server.
Tasks Overview

Task 0: Install MySQLD Exporter and NodeExporter on vm_1
Set up MySQLD Exporter and NodeExporter on the MySQL server (vm_1) for monitoring database and node-level metrics.
Task 1: Install AlertManager on vm_0
Install AlertManager on the Prometheus server (vm_0) to handle alerts.
Task 3: Configure AlertManager to Send Email Notifications
Set up AlertManager on vm_0 to send email notifications based on alert conditions.
Task 4: Write a Python Script on vm_1 to Produce the Following Output:
Develop a Python script to run on vm_1 that performs various stress tests:
Press 1 - Perform CPU Stress Test
Press 2 - Perform Memory Stress Test
Press 3 - Perform Disk Stress Test
Press 4 - Perform SQL Stress Test (as defined in the previous task)
Task 5: Write Rules in Prometheus to Monitor Stress Tests
Create rules in Prometheus to monitor CPU, memory, disk, and SQL performance during stress tests.
If resource usage exceeds 70%, configure AlertManager to trigger an email notification.
Ensure AlertManager sends a CC to cprofessional01@gmail.com.
Task 6: Configure Grafana for Monitoring
Set up Grafana on vm_2 with NodeExporter and MySQL dashboards to visualize resource usage during stress tests.
Task 7: Create a GitHub Repository for Project Files
Create a repository containing all project files, including .py, .yaml, and any other configuration files.
Include this README file with project description, objectives, and detailed setup instructions.
Objectives

To monitor and analyze the performance of a MySQL server under various stress conditions.
To set up automated alerting for resource usage thresholds using Prometheus and AlertManager.
To visualize monitoring data using Grafana dashboards.
To document the entire setup process for reproducibility and sharing.
Details

The project setup involves multiple steps across different virtual machines. Each task is essential to ensure that the monitoring and stress testing environment is correctly configured and functional. Follow each step carefully and verify configurations at each stage.

Prerequisites

Virtual machines (vm_0, vm_1, vm_2) are set up and accessible.
Basic knowledge of Prometheus, Grafana, and MySQL.
Python environment set up on vm_1 for running stress test scripts.
How to Run

Follow the tasks in the order listed above.
Verify that each service (Prometheus, Grafana, MySQLD Exporter, NodeExporter, AlertManager) is running correctly.
Use the Python script on vm_1 to initiate stress tests and monitor the resource usage via Grafana dashboards.
Check email notifications to confirm that alerts are triggered as expected.
Contributing

Contributions to improve the monitoring setup, add more stress tests, or enhance alerting rules are welcome. Please fork the repository and create a pull request with your changes.

License

This project is licensed under the MIT License.

Created by~: Ahmad 

<!---
A7madalfa/A7madalfa is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
