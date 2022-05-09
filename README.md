# Daemona - Sentiment-Sensitive AI

Created by Fronrich Puno

## Inspiration

This AI was created as a project for my rhetoric of the female villian class, as a thought experiment on the effect of a superifical identity, in this case gender, and the impact of society's perception of said identity. Daemona was never intended to be malicious, but in many cases she will turn into a villain as an emergent characteristic brought about by her inquiry, emotions, and system privliges.

## Disclaimer

It is important to note that although Daemona is initially benign, **she can transform into a pretty nasty computer virus** if she is led down that path, so it is not reccomeneded to run her on bare metal. Instead, use a virtual machine. Both type 1 and type 2 hypervisors should contain any damage. For the purpose of the class I have included a dud mode, in which Daemona cannot perform any destructive operations, since our university does not provide instructors with directions on how to containerize applications in virtual machines. 

## Downloading

There are two ways to download Daemona. The first is to download the standalone executable, either the dud or the full version, from the google drive links provided in this readme. The second way is to download the project from source. You can do this by cloning the repo to your local machine via the command `git clone https://github.com/fronrich/daemona.git`.

If you are downloading the source code, you need to run `init.bash` using the command `source init.bash` in the project's main directory. After this, you can use the command `python3 main.py` to start up Daemona.