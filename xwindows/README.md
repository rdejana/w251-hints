# Using X Windows
X Windows (X11, or simply X) is a windowing system for bitmap displays, common on Unix-like operating systems.  
An interesting feature of X is that it allows the remote display of a window over the network.

The following will cover using X as a means of displaying an UI running on a Jetson device via a macOS or Linux workstation<sup>*</sup>.


<sup>*</sup> At this time, I do not have a Windows system to text with.  The Linux example will be done as a virtual machine (VM) and such an approach will work with Windows.

## macOS and XQuartz
XQuartz is a X Windows solution for Apple's macOS and will be used for the display.

You'll need to [download](https://www.xquartz.org) and install XQuartz.  

Once installed, start XQuartz and navigate to its prefernce menu (XQuartz, Preferences). Select the security tab and uncheck `Authenticate Connections` and check `Allow connections from network clients`.  

![X11 Preferences](images/X11_Preferences.png)

Quit XQuartz (XQuartz, Quit X11) and restart it.

Once XQuartz is running, navigate to (or start via Applications, Terminal if not opened automatically) and enter the command `xhost +`.  Note, this window is different than the "normal" macOS termianl and will have the title xterm.

![xterm](images/X11_Preferences.png)


## Ubuntu Linux

