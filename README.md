# How to Set Up (for Ubuntu 14.04 LTS)
* `sudo apt-get update`
* `sudo apt-get install git`
* `sudo apt-get install bzip2`
* `git clone https://github.com/KahanPrabhu/Anomaly-Detection-.git`
* `wget https://3230d63b5fc54e62148e-c95ac804525aac4b6dba79b00b39d1d3.ssl.cf1.rackcdn.com/Anaconda2-4.0.0-Linux-x86_64.sh`
* `chmod 777 Anaconda2-4.0.0-Linux-x86_64.sh`
* `bash Anaconda2-4.0.0-Linux-x86_64.sh`
  * Be sure to answer yes when it asks to add the anaconda path to your .bashrc file.
* End your SSH session and re-open it again.
* `cd Anomaly-Detection-`
* `conda env create -f anomaly-detection.yml`
* `source activate anomaly-detection`
  * You are now in the anaconda environment with the required packages installed.
* Uncomment your line of code in go.py
* Run the algorithm using `screen -S anomaly-detection python go.py`. Press CTRL + AD to detach the screen. It is now safe to exit your ssh session.
