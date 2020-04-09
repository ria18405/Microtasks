## MICROTASK 10:
**AIM** : Submit at least a PR to one of the GrimoireLab repositories to fix an issue, improve the documentation, etc.

1. (Merged ) Added sections of Troubleshooting in Getting Started - [chaoss/grimoirelab-sirmordred#429](https://github.com/chaoss/grimoirelab-sirmordred/pull/429) 

	Made commits regarding some problems I faced during my setup of the dev environment. It was related to a sleep-for-rate section and a loss of functionality due to swap space.

2. (Merged) Added sections in 'HOW TO' section in Getting Started - [chaoss/grimoirelab-sirmordred#440](https://github.com/chaoss/grimoirelab-sirmordred/pull/440) 

	Made commits regarding the cleaning of all existing docker containers and making a fresh installation. The following section was added :
	- Remove existing dockers and start a fresh environment

3. (Merged) Added some FAQ sections under 'HOW TO' section- [chaoss/grimoirelab-sirmordred#449](https://github.com/chaoss/grimoirelab-sirmordred/pull/449)

	This will ensure first time contributions and users to know more about the system and will solve some basic Q n A . These are the sections added in the document:

	- Share a dashboard
	- Edit the name of a Visualization
	- Edit a Visualization
	- Check that the data is up to date

4. (Merged) Fixed some backlinks in Getting Started -[chaoss/grimoirelab-sirmordred#451](https://github.com/chaoss/grimoirelab-sirmordred/pull/451)

	- Fixed some broken and inconsistent links in GettingStarted.md document

5. (Merged) Fixed minor typos [chaoss/grimoirelab-perceval#641](https://github.com/chaoss/grimoirelab-perceval/pull/641)
	- Fixed minor typos in README and backend.py

6. (Merged) [travis] Upgrade setuptools and pip [chaoss/grimoirelab-perceval#643](https://github.com/chaoss/grimoirelab-perceval/pull/643)
		
	This code upgrades the setuptools and pip in travis.yml
	It was needed to fix the CI tests that were failing due to the following error:

	```
	File "../python3.5/site-packages/setuptools/sandbox.py", line 44, in _execfile
	  code = compile(script, filename, 'exec')
	File "/tmp/easy_install-wu9lgsxc/pandoc-2.0a4/setup.py", line 11
	  error = f"pip is not installed, refer to <{url}> for instructions."
	                                                                    ^
	SyntaxError: invalid syntax
	```

	Similar commits in other repositories :

	- [travis] Upgrade setuptools and pip [grimoirelab-sortinghat#283](https://github.com/chaoss/grimoirelab-sortinghat/pull/283)

	- [travis] Upgrade setuptools and pip [grimoirelab-manuscripts#137](https://github.com/chaoss/grimoirelab-manuscripts/pull/137)



