
from perceval.backends.core.git import Git

# URL for the git repo to analyze
repo_url = 'https://github.com/ria18405/Chat-ly'
# directory for letting Perceval clone the git repo
repo_dir = 'Clone/Chat-ly.git'

# Initialising Git object
git_obj = Git(uri=repo_url, gitpath=repo_dir)

"""The method fetch() retrieves a list of all commits from a 
	Git repository or a log file.
	Here, we are fetching the list of commits and printing all the data.
"""
for commit in git_obj.fetch() :
	print(commit['data'])