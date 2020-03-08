from perceval.backends.core.github import GitHub

github_obj=GitHub(
        owner='ria18405', repository='Chat-ly', sleep_for_rate=True,
        sleep_time=300
    )

""" 
    The method retrieves,the issues/pull requests from a GitHub repository, 
    updated since the given date. 
    """
for issues in github_obj.fetch():
    print(issues['data'])

