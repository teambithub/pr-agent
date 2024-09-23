PR Agent
=

Install
==

````
source bin/activate
pip3 install -e .
````

Configure
==

````
cp pr_agent/settings/.secrets_template.toml pr_agent/settings/.secrets.toml
````

Configure openai.key and github.user_token

Execute
==

````
python3 -m pr_agent.exec --pr_url=https://github.com/teambithub/git-service/pull/33
````
