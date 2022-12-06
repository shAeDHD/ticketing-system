# Randomised Ticketing System 

My first Pyhon project, this repo houses a program that can generate usable randomised JSON ticket data for seeding into a relatoinal database for a customer helpdesk, or similar service. 
---

## Instructions
When using the program, please make sure that you follow the steps below.

Open a Bash/Shell program and check if Python is installed on your system,
`$  python3 --version`

If you do not have python installed, you'll need to. In which case you'll want to have Homebrew installed. If you already have Homebrew installed, you can skip the following steps regarding Homebrew Installation.

### Homebrew Installation  
    
    1. Open a browser and navigate to http://brew.sh/.

    2. You should see a command for installing Homebrew near the top of the page under the tile “Install Homebrew.” This command will be something like the following:

    `$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"`

    3. Highlight the command with your cursor and press Cmd+C to copy it to your clipboard.

    4. Open a terminal window and paste the command, then press Enter. This will begin the Homebrew installation.

    5. Enter your macOS user password when prompted.
    
Now that Homebrew is installed, you’re ready to install Python.

### Installing Python
Going back to your bash/shell - 
  `$ brew update && brew upgrade`
then
  `$ brew install python3` 
  
Now, once that's done, if we try again, `$  python3 --version`, we should get something like, `Python 3.6.10`.

### Pip3 - Packages
We'll also need to download a package that generates realistic addresses for shipping details. 

Going back to the bash/shell, check you have pip3 installed. 
  `$ pip3 --version`

Which should return something like,
  `$ pip 20.0.2 from C:\Python38\lib\site-packages\pip (python 3.8)`
  
To download the lovely package: [random-address 1.1.1](https://pypi.org/project/random-address/) 
  `$ pip3 install random-address`
  
Then we're good to go!

## Using the Ticket Generator
With everything installed, and the git files on your computer, run
  `$  python3 ticket_generator.py`

You will be prompted to enter an integer of how many tickets you wish to create and then once the program has completed it will export a file to the home folder called 'json_ticket_data.json' with the requested ticket data. 

#### Additional
If you wish to see the tickets print out in the console itself - uncomment `line 142` in the `ticket_generator.py` file.
