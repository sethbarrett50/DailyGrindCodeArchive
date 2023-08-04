# The venv module is a built-in Python library that allows you to create virtual environments for your Python projects
# Here are some of the most commonly used methods in the venv module:

'''venv.create(path, system_site_packages=False, clear=False, symlinks=False): This method creates a new virtual environment in the specified path. The system_site_packages parameter, if set to True, allows the virtual environment to access packages installed globally. The clear parameter, if set to True, removes the contents of the target directory before creating the virtual environment. The symlinks parameter, if set to True creates symbolic links to files rather than copies.'''
import venv

venv.create('.env', with_pip=True)

'''activate(): This method activates the virtual environment and changes the environment variables so that the Python interpreter, pip, and other commands use the packages and dependencies in the virtual environment.'''
# source .env/bin/activate > In terminal

'''deactivate(): This method deactivates the virtual environment and restores the original environment variables.'''
# deactivate > In terminal

'''venv.EnvBuilder(system_site_packages=False, clear=False, symlinks=False, upgrade=False, with_pip=False): This method creates a builder class that can be used to customize virtual environment creation.'''
builder = venv.EnvBuilder(with_pip=True, clear=True)
builder.create('.env')