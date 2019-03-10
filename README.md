# Logs Analysis Project

This project is an analysis of the news database given to me by Udacity. This project showcases my SQL and Python skills by
displaying a report about the given database through queries I have written in my Python code. All the database analysis
was done solely through queries in order to maintain efficiency in the project.

## Getting started
### Prerequisites
To run this project you will need:
* [Python 3](https://www.python.org/downloads/)
* [VirtualBox 5.1](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
* [Vagrant](https://www.vagrantup.com/downloads.html)
* [Udacity-provided VM](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip)
* [Udacity-provided SQL database](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

### Installing
You will first need to download **VirtualBox 5.1**. You can download it [here](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1).

You will then need to install **Vagrant**. You can dowload it [here](https://www.vagrantup.com/downloads.html). (Be sure to grant it network permissions if prompted)

Unzip the [Udacity-provided VM](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip) and navigate to the **vagrant** directory.

In here, create a **new directory** and place the **logsAnalysis.py** and **[Udacity-provided SQL database](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)** here. (Unzip the database file as well)

Go back to the **vagrant** directory, open a terminal and run the following command:
```
vagrant up
```
This will tell Vagrant to download and install the Linux OS, which my take some time.

When this is done, run the following command to connect to the VM:
```
vagrant ssh
```
Navigate to the **/vagrant** directory:
```
cd /vagrant
```
Navigate to the directory you created:
```
cd "your directory name"
```
In here run the following command to set up the database:
```
psql -d news -f newsdata.sql
```
After this try running the python file!
```
python logsAnalysis.py
```

## Author
Efren Aguilar

## Acknowledgements
[Udacity](https://www.udacity.com/) for providing the virtual machine configuration and data for the databse. 