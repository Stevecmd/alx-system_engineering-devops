# 0x18-webstack_monitoring

## Overview

This project focuses on web stack monitoring, an essential aspect of maintaining healthy software systems. It encompasses both application monitoring, which ensures the proper behavior of running software, and server monitoring, which prevents server overload.

## Objectives

By the end of this project, you should be able to:

- Explain the need for monitoring.
- Understand the two main areas of monitoring: application and server.
- Define access logs and error logs for a web server (e.g., Nginx).

## Requirements

- Allowed editors: vi, vim, emacs
- All files will be interpreted on Ubuntu 16.04 LTS
- All files should end with a new line
- A `README.md` file, at the root of the project folder, is mandatory
- All Bash script files must be executable
- Your Bash script must pass Shellcheck (version 0.3.7) without any error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what the script is doing

## Installation and Setup

### 0. Sign up for Datadog and install datadog-agent

1. Sign up for a free Datadog account at [Datadog](https://www.datadoghq.com/). Please make sure you are using the US website of Datadog (https://app.datadoghq.com) and select the `US1 region`.

2. Install the Datadog agent on `web-01` by following the instructions provided on the Datadog website.

3. Create an application key and copy-paste your DataDog API key and application key in your Intranet user profile.

4. Ensure that your server `web-01` is visible in Datadog under the host name `XX-web-01`. You can validate it using [this API](https://docs.datadoghq.com/api/latest/hosts/).

### 1. Monitor some metrics

- Set up a monitor that checks the number of read requests issued to the device per second.
- Set up a monitor that checks the number of write requests issued to the device per second.

### 2. Create a dashboard

- Create a new dashboard.
- Add at least 4 widgets to your dashboard. They can be of any type and monitor whatever you'd like.
- Create the answer file `2-setup_datadog` which has the `dashboard_id` on the first line. To obtain the id of your dashboard, you may need to use Datadog’s API.
