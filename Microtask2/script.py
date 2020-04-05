
from perceval.backends.core.github import GitHub
from perceval.backends.core.gitlab import GitLab

def extract_github(own,repo):
	github_obj=GitHub(
			owner=own, repository=repo, sleep_for_rate=True,
			sleep_time=300
		)

	""" 
		The method retrieves,the issues/pull requests 
		from a GitHub repository, updated since the given date. 
		"""
	for issues in github_obj.fetch():
		print(issues['data'])

def extract_gitlab(own,repo):

	# Initialising GitLab object
	gitlab_obj = GitLab(owner=own, repository=repo,sleep_for_rate=True,
			sleep_time=300, api_token='xxxx')


	"""The method fetch() retrieves a list of all issues/merge requests 
	from the repository from a GitLab repository.
	Here, we are fetching the list of commits and printing all the data.
	"""

	for commit in gitlab_obj.fetch() :
			print(commit['data'])


def main():
	print('Enter Github repository details ')
	owner=input("Enter owner of repository: ")
	repository=input("Enter repository name: ")
	print("Extracting data from GitHub")
	extract_github(owner,repository)
	print("EXTRACTION COMPLETE")


	print('Enter GitLab repository details ')
	gitlab_owner = input("Enter owner of repository: ")
	gitlab_repository = input("Enter repository name: ")
	print("Extracting data from GitLab")
	extract_gitlab(gitlab_owner,gitlab_repository)
	print("EXTRACTION COMPLETE")


if __name__ == "__main__":
	main()
