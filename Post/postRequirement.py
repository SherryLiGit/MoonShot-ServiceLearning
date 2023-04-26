# ref: https://zhuanlan.zhihu.com/p/522834445
# ref: https://python-wordpress-xmlrpc.readthedocs.io/en/latest/index.html
import json
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost

with open('account.json', 'r', encoding='utf-8') as userList:
    wplogin = json.load(userList)

id = wplogin["username"]
pwd = wplogin["password"]
url = "https://my.moonshotacademy.cn/service-learning/xmlrpc.php"

which = 'draft'
wp = Client(url, id, pwd)
post = WordPressPost()
post.post_status = which
post.title = 'Python XMLRPC API TEST'
post.content = 'Python XMLRPC API TEST CONTENT'
post.excerpt = 'Pythin XMLRPC API TEST EXCERPT'
post.terms_names = {
    "post_tag": ['testing12345'],
    "category": ['testing12345']
}

wp.call(NewPost(post))