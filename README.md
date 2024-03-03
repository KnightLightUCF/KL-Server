# KnightLight Server Executable

This project is an executable version of Skybrush Server which allows the user to quickly set up a server which facilitates communication for a drone show. The executable detects if the user has Skybrush Server installed on their device and installs it if needed and then proceedes to run the server. This project is deployable on macOS and Windows only requiring slightly different methods of startup.

# Getting Started

### Prerequisites
Ensure that you have Python 3.9+ installed on your machine. Installation can be found [here](https://www.python.org/downloads/)

### Installation
Clone the repository into your desired location as shown below and move into the cloned directory
```bash
git clone <repository-url>
cd <project-directory>
```

# Starting the server
### MacOS
Starting up the server on Mac is as simple as moving into the /mac folder and running run.sh!
```bash
cd <project-directory>/mac
sh run.sh
```
All dependencies should be installed and the server will start running afterwards.

### Windows
