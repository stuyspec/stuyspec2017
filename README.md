# Stuyvesant Spectator Website 2017 (deprecated)

## Notice
This repository is no long being advanced nor maintained. From June 2017 to August 2017, the website was rewritten into a Rails back-end and a ReactJS front-end.

## Team

| Photo |  Name  |  Role  | Github  |  Email  |
|-------|--------|--------|---------|---------------|
| <img src="https://i.imgur.com/Gyat6Ts.png" align="left" height="100" > | Jason Kao | CFA Lead | jkao1 |  jkao1@stuy.edu |
| <img src="https://ih1.redbubble.net/image.265404657.9078/flat,800x800,075,f.u1.jpg" align="left" height="100" > | George Zheng | Flask Lead | |  gzheng3@stuy.edu  |
| <img src="http://nicholasyang.com/images/Headshot.jpg" align="left" height="100" > | Nicholas Yang | CMS Lead | NicholasLYang | nick@nicholasyang.com |
| <img src="https://scontent-atl3-1.xx.fbcdn.net/v/t1.0-9/12308272_1173580929338001_7544449936608883692_n.jpg?oh=7c97f7287fb2e8a6836cf9fb61a70174&oe=59C9EE27" align="left" height="100" > | Henry Zheng | CMS Developer | henryz2000 | hzheng3@stuy.edu |
| <img src="https://scontent-lga3-1.xx.fbcdn.net/v/t1.0-9/12932566_743144365821892_1371702610685774858_n.jpg?oh=11c911a41fe09c2eae160004dddaf995&oe=59A078EF" align="left" height="100" > | Raunak Chowdhury | Flask Developer | raunakchowdhury | rchowdhury5@stuy.edu |
| <img src="https://scontent-lax3-1.xx.fbcdn.net/v/t1.0-0/p206x206/17903692_785938064910478_3786230932291906266_n.jpg?oh=5ba0babb20909609ec5241b5d7ee7193&oe=59A1E181" align="left" height="100" > | Jason Lin | CFA Developer | JasonLin43212 | jasonlin43212@gmail.com |
| <img src="http://gazettereview.com/wp-content/uploads/2016/03/facebook-avatar.jpg" align="left" height="100" > | Jerry Ye | Flask Developer | jerry1ye10 | jye6@stuy.edu | |
| <img src="https://scontent-lga3-1.xx.fbcdn.net/v/t1.0-9/16831085_649694105210308_4808979255089774176_n.jpg?oh=d5cc014852fb07a3bb7fc8eec4979339&oe=59E8BAEF" align="left" height="100" > | Joyce Liao | Flask Developer | joyceliaoo | jliao@stuy.edu |
| <img src="http://hw-img.datpiff.com/mbf37a1b/Nile_I_Dont_Exist_demo-front.jpg" align="left" height="100" > | Jonathan Wong | Developer | jonw27 | admin@stuy.tech
| <img src="http://www.free-avatars.com/data/media/82/landscape_avatar_0019.jpg" align="left" height="100" >| Angela Tom | Flask Developer | angelatom | atom@stuy.edu |
| <img src="http://food.fnr.sndimg.com/content/dam/images/food/fullset/2013/9/12/1/FN_Picky-Eaters-Chicken-Nuggets_s4x3.jpg.rend.hgtvcom.406.305.jpeg" align="left" height="100" >| Suzanna Liang | CFA Developer | sliang4 | sliang4@stuy.edu |
| <img src="https://avatars1.githubusercontent.com/u/27791964?v=3&u=905f8b972dc170061fbe11b2fe5e922c4f501f27&s=400" align="left" height="100" >| Qichen Deng | Developer | QichenD | qichendeng@stuy.edu |
| <img src="https://uproxx.files.wordpress.com/2017/05/mocking-spongebob.jpg?quality=100&w=650" align="left" height="100" >| Sabrina Wen | CMS Developer | sabrina-wen | sabrinawn253@gmail.com |
| <img src="https://i.imgur.com/wfQYBT9.png" align="left" height="100" > | Kenneth Zhang | Developer | KenZ3 | kzhang8@stuy.edu |
| <img src="https://s-media-cache-ak0.pinimg.com/736x/9d/31/e0/9d31e0c2442c02b1dac172285ad61afc.jpg" align="left" height="100" > | Cathy Cai | CFA Developer | ccai1 | ccai1@stuy.edu |
| <img src="http://1.bp.blogspot.com/-2cl0a37VYPY/Vova8h-D_NI/AAAAAAAAAeY/CPr_Ivr7fpU/s1600/curti.png" align="left" height="100" > | Alvin Chung | Flask Developer | achung0 | achung00@stuy.edu |  
| <img src="https://s-media-cache-ak0.pinimg.com/736x/72/19/e8/7219e8b1b182d381c7725b2d404dacd9.jpg" align="left" height="100"> |  Claire Liu  |  CFA Developer  | cliu5  |  cliu5@stuy.edu  |

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
