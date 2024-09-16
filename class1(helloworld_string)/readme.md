# Python
- python is a dynamic language and it has interpreter so it is a interpreter language(line by line code)
- it is not a compile language
- superset of python is mojo as typescript is superset of javascript


## How to make enviroment in VScode by the help of Anaconda
### Create a New Environment Using Conda
```
conda create -n myenv python==3.12 -y
```
- Replace myenv with the name you want for your environment:

```
conda activate myenv
```


### Select the Environment in VS Code:
* In VS Code, press Ctrl + Shift + P (or Cmd + Shift + P on macOS) to open the Command Palette.
* Type "Python: Select Interpreter" and choose the environment you just created (myenv) from the list.


### Install Necessary Packages:
* Now you can install the packages you need within this environment using Conda or pip. For example:
```
conda install numpy

```
* Or use pip:
```
pip install pandas

```

### Install more packages
* Make a file of requirement.txt and write the names of packages that I want to download and simply run a command
```
pip install -r requirement.txt
```