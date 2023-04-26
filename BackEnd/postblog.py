# ref: https://zhuanlan.zhihu.com/p/522834445
# ref: https://python-wordpress-xmlrpc.readthedocs.io/en/latest/index.html
import json
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost

def post_to_wordpress(title: str, content: str):
    # get wordpress account information
    with open('account.json', 'r', encoding='utf-8') as userList:
        wplogin = json.load(userList)
    id = wplogin["username"]
    pwd = wplogin["password"]
    url = "https://my.moonshotacademy.cn/service-learning/xmlrpc.php"

    wp = Client(url, id, pwd)
    post = WordPressPost()
    # save as draft when developing, can be changed to publish by uncommenting the following line
    # post.post_status = 'publish'
    post.title = title
    post.content = content

    wp.call(NewPost(post))