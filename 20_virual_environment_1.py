# A virtual environment is used to isolate specific Python environment on a single machine,
# allowing you to work on multiple projects with  different dependencies and packagees without conflicts.
# This can be especially useful when working on projects that have conflicting package versions or 
# packages that are not compatible with each other. 

# To create a virtual environment in Python you can use the venv module that comes with Python.


# to create a virtual environment  --> python -m venv myenv(enviroment_name)

# to activate a virtual environment (windows) --> myenv\Scripts\activate.bat 

# to activate a virtual environment (mac/linux) --> source myenv\bin\activate

# once the virtual environment is activated, any package that you will install using pip will be installed 
# in the virtual environment, rather than a global python environment. This allows you to have a separate 
# set of packages for each project, without affecting the packages installed in global environment.

# to deactivate the virtual environment --> deactivate