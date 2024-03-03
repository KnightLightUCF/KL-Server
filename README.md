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

# Starting the Server
## MacOS
Starting up the server on Mac is as simple as moving into the /mac folder and running run.sh!
```bash
cd <project-directory>/mac
sh run.sh
```
All dependencies should be installed and the server will start running afterwards.
### Potential Issue on Mac...
If you are having trouble starting the server, there is a high likelyhood that the port the server runs on is occupied by Apple Airplay. To fix this issue, the current solution is to turn off Airplay in your device settings. Instructions can be found [here](https://osxdaily.com/2022/12/19/how-to-turn-off-airplay-on-mac/)

## Windows
To start the server on Windows, change into the /windows folder and run the run.bat file
```bash
cd <project-directory>/windows
run run.bat
```
All dependencies should be installed and the server will start running afterwards.
