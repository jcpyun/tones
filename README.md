# TONES
##### Contributors
  - John C. Pyun (Carnegie Mellon University Class of 2016)
  - Patrick Yurky (Carnegie Mellon Universtiy Class of 2015)
  - Roger B. Dannenberg (Professor of Carnegie Mellon University)

Sample execute:  
Sample code to compile into .wav file:  
`
python createMusic.py blankSpace.txt blank.wav
`  

sample code to play the .wav file:  
`
aplay blank.wav
`

I might try to use virtualenv for scikit.

I need numpy and scipy.


`
$ sudo apt-get install python-virtualenv python-pip
$ sudo apt-get build-dep python-numpy python-scipy
$ # Create virtualenv in home
$ virtualenv .myenv
$ # Activate the virtualenv
$ source .myenv/bin/activate
(myenv)$ pip install -U numpy
(myenv)$ pip install -U scipy
`
now do this after: 
http://scikit-image.org/download