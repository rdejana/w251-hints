# HW3 Updated Guidance 

I know at least one student does not have a working USB web camera.  
It is possible to use the on board TX2 camera, though I don't have a containerized version at this time. 
For those students, I recommend creating a virtual python3 environment instead of containerization.

Check your versions
You want to be at  Python 3.5–3.7 and pip >= 19.0
From your tx2, run the following
   ```
    python3 --version
    pip3 --version
    virtualenv --version 
   ```

If these packages are already installed, skip to the next step.
Otherwise, install:
    ```
    sudo apt update
    sudo apt install python3-dev python3-pip
    sudo pip3 install -U virtualenv  # system-wide install
    ```

Create a new virtual environment by choosing a Python interpreter and making a ./venv directory to hold it.  I recommend 
creating the ./venv on your external drive.  Note, this will use your existing packages, including OpenCV.
   ```
    virtualenv --system-site-packages -p python3 ./venv
   ```

Activate the virtual environment using a shell-specific command:
   ```
    source ./venv/bin/activate  # sh, bash, ksh, or zsh
   ```

When virtualenv is active, your shell prompt is prefixed with (venv).

Install packages within a virtual environment without affecting the host system setup. Start by upgrading pip:
  ```
    pip install --upgrade pip
    pip list  # show packages installed within the virtual environment
  ```

And to exit virtualenv later:
   ```
    deactivate  # don't exit until you're done.
   ```

The OpenCV example is available [here](tx2camera.py).

