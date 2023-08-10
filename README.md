# DockerPortal

DockerPortal is a tool that acts as a wormhole, simplifying the process of pushing Docker images to a remote repository. It automates the tagging and pushing of Docker files to a specified server, eliminating the need for manual intervention.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

DockerPortal streamlines the process of pushing Docker images to a remote repository. It automates the tagging and pushing of images to the right remote repository, reducing the manual effort required.

## Features

- Automated tagging and pushing of Docker images to a remote repository.
- Easy installation as a binary file, accessible via the command line.
- Simplifies the creation of a folder where you can start the wormhole and push images.

## Getting Started

### Installation

1. Download the latest release binary for your operating system from the [Releases](https://github.com/yourusername/dockerportal/releases) page.
2. Make the binary file executable:
  ```sh
     chmod +x dockerportal```
Move the binary to a directory included in your system's PATH, e.g., /usr/local/bin:

```mv dockerportal /usr/local/bin/```


Usage
Create a new folder for your DockerPortal setup:

```mkdir my-dockerportal
cd my-dockerportal
Start the DockerPortal wormhole server:
dockerportal start```


Follow the prompts to provide the necessary configuration details, including the remote image repository server.

Place your Docker files in the created folder. DockerPortal will automatically tag and push these images to the remote repository based on your configuration.

Configuration
DockerPortal uses a configuration file named userio.yml to specify the remote server and other settings. Refer to the Configuration Guide for more information on setting up and customizing your configuration.

Contributing
We welcome contributions from the community! If you'd like to contribute, please refer to the Contributing Guidelines.

License
DockerPortal is open-source software licensed under the MIT License.

Contact
For any questions or support, please create an issue or contact us on LinkedIn.

Replace the placeholders (`yourusername`, `my-dockerportal`, etc.) with actual details relevant to your project. Make sure to provide clear instructions and explanations to help users understand how to use and contribute to your project.