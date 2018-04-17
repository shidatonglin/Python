from bs4 import BeautifulSoup
import re, urllib.parse

set_urls = []
root_url = 'https://www.baidu.com/showthread.php?t=682126'
for p in range(1, 200, 1):
    set_urls.append(root_url + '&page=' + str(p))
    # print(p)

for url in set_urls:
    #print(url)

    html = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>
    <p class="story">...</p>
    """
html_cont = '''
<div>
<li class="others">
    <a>link13</a>
    <ul> 
       <li>  
          <a>link24</a> 
       </li>
    </ul>
</li>
<li class="test">
    <div>
    <a>link1</a>
    <ul> 
       <li>  
          <a>link2</a> 
       </li>
    </ul>
    </div>
</li>
</div>
'''

ff_doc = """
<div class="showthread showthread--anchored flexBox noflex" id="post10478935"> 
<a class="anchor abs" name="post10478935"></a> 
<div class="threadpost-header "> 
<div class="threadpost-header__controls"> 
<ul> <li class="threadpost-header__controllink"> 
<a class="threadpost-header__linkicon threadpost-header__linkicon--postnum postnum" href="showthread.php?p=10478935#post10478935" 
id="postcount10478935" name="3" rel="nofollow" title="Post Permalink"><span>
<span class="visible-dv visible-tv">Post </span>
<span class="visible-mv">#</span>3
</span
></a> 
</li> <li class="threadpost-header__controllink">
 <a class="threadpost-header__linkicon threadpost-header__linkicon--quote quote" href="showthread.php?t=713593&amp;reply=1&amp;page=196&amp;quote=10478935#reply" title="Quote This Post"><span>Quote</span></a> </li> <li class="threadpost-header__controllink threadpost-header__controllink--nolink"> <span> <span class="visible-mv">

Nov 9, 2017 5:23pm

</span> <span class="visible-dv visible-tv">

Nov 9, 2017 5:23pm 



</span> </span> </li> </ul> </div> <div class="threadpost-header__userarea"> <ul> <li class="threadpost-header__userbit threadpost-header__userbit--username"> <div class="usernamedisplay large"> <a class="" href="yalgaar" title=""> <span class="usernamedisplay__avatar avatar usernamedisplay__avatar--noavatar noavatar"> </span> <span class="usernamedisplay__username username"> yalgaar</span> </a></div> </li> <li class="threadpost-header__userbit threadpost-header__userbit--userinfo threadpost-header__userbit--reduce"> <div class="threadpost-header__userbit-details"> <span class="seperator">|</span>




Joined Jan 2017




<span class="threadpost-header__userarea-hidden visible-tv visible-dv"> <span class="seperator">|</span>
Status: Member



<span class="seperator">|</span> <a class="darklink" href="search.php?do=process&amp;provider=Member&amp;searchuser=549443">316 Posts</a> <span class="seperator">|</span> <span class="onlinestatus online">Online Now</span> </span> </div> </li> </ul> </div> </div> <div class="threadpost-content " id="td_post_10478935"> <div class="threadpost-content__message" id="post_message_10478935">
              Can you provide the settings for each indicator? I just loaded my charts with all the indicators you mentioned but it just looks totally different.              
</div> <div class="like like--post like--disabled like--noperms" data-contentid="10478935" data-contenttype="post"> <div class="like__button like__button--dislike" data-touchable=""> <div class="like__count like__count--dislike"><span></span></div> <div class="icon icon--dislike"></div> </div> <div class="like__button like__button--like" data-touchable=""> <div class="like__count like__count--like"><span></span></div> <div class="icon icon--like"></div> </div> </div> </div> </div>
"""
soup = BeautifulSoup(ff_doc, 'html.parser')

message_data = []
res_data = {}


title_node = soup.find_all('div', class_='showthread showthread--anchored flexBox noflex')

for node in title_node:
    # nodesoup = BeautifulSoup(node.get_text(), 'html.parser', from_encoding='utf-8')
    #print(node)
    #print('==================')
    res_data['postlink'] = \
        node.find('a', class_='threadpost-header__linkicon threadpost-header__linkicon--postnum postnum')['href']
    res_data['name'] = node.find('span', class_ = 'usernamedisplay__username username').get_text()
    res_data['message'] = node.find('div', class_='threadpost-content__message').get_text()
    #print(res_data)
    message_data.append(res_data)


for number in range(100):
    print(number)