# Stuyvesant Spectator Website 2017

minion: http://fontsgeek.com/search?q=minion+pro
## Bugs
- navbar collapse is glitchy on tall screens
## Standard dependency workflow
*Do NOT check dependencies into the repo*
- Create a virtual environment outside the repo (or inside, as long as you
do not check it into the repo)
- When you add a new dependency:
  `pip freeze > requirements.txt`
- When you want to install the new dependencies:
  `pip install -r requirements.txt`
- THE ONLY THING ADDED TO THE REPO SHOULD BE `requirements.txt`


## Tips for Deployment

- Do not check db files into the repo
- Deploy early
- Use automated deployment scripts
  - A good way to automate deployment is through git hooks
- Do not use spaces, hyphens or slashes in the app name

## Team

| Photo |  Name  |  Role  | Programming Languages  |
|-------|--------|--------|------------------------|
| <img src="http://nicholasyang.com/images/Headshot.jpg" align="left" height="100" > | Nicholas Yang | Project Consultant | Python, Ruby, JavaScript, C++, SQL |
| <img src="https://i.imgur.com/Gyat6Ts.png" align="left" height="100" > | Jason Kao | Editor | Python, Ruby, JavaScript, C++, SQL |
| <img src="https://ih1.redbubble.net/image.265404657.9078/flat,800x800,075,f.u1.jpg" align="left" height="100" > | George Zheng | Editor | Python |
| <img src="https://scontent-lga3-1.xx.fbcdn.net/v/t1.0-9/12932566_743144365821892_1371702610685774858_n.jpg?oh=11c911a41fe09c2eae160004dddaf995&oe=59A078EF" align="left" height="100" > | Raunak Chowdhury | Developer | Python |
