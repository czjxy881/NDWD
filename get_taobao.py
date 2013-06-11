# coding:utf-8
import urllib2,urllib,requests,re,sys
#图片，名称，价格的总表
pic=[];name=[];price=[];deal=[]
def find(t):
    '''
        查询当前源代码(t)中的商品，并加入总表,返回值为成功查找到的数量
        参数说明：
            t: 所查询源代码  
    '''
    global pic,name,price,deal
    #获取淘宝图片地址
    r_pic=re.compile('<p class=\"pic-box\">.*\s*<span><img src=\"(.*?)\" />')
    #获取商品名称及地址
    r_name=re.compile('<h3 class="summary"><a .*? href=\"(.*?)\" target=\"_blank\" title=\"(.*?)\">')
    #获取商品价格及运费
    r_price=re.compile('<div class=\"col price\">(.*?)<em></em></div>\s*<div class=\"col end shipping\">\s*(.*?)\s*</div>')   
    #获取成交量
    r_deal=re.compile('<div class="col dealing">.*?(\d+)')
    
    #将此页信息加到总表中
    pic+=r_pic.findall(t)
    name+=r_name.findall(t)
    deal+=r_deal.findall(t)
    
    #将淘宝的价格及运费变成数字形式
    pt=r_price.findall(t)
    p=[1,2]
    for i in range(len(pt)):
        p[0]=pt[i][0][3:]
        if pt[i][1]=='免运费':p[1]='0.00'
        else: p[1]=pt[i][1][9:]
        pt[i]=list(p) #直接等于为引用，此处应该复制
    price+=pt
    return len(pic)
def taobao(s,id):
    '''
      查询淘宝中此商品信息，s为关键词,id为生成id，将查到的商品保存到id.txt并返回成功数目
      参数说明：
         s： 关键词
    '''
    global pic,name,price,deal
    pic=[];name=[];price=[];deal=[] #清零
    #将关键词转成网页编码
    s=urllib.quote(s)
    s.replace('%20','+')
    url='http://s.taobao.com/search?q=%s&s='%s
    start=0 #起始位置
    text="" #查询内容
    while start==0 or find(text)!=0:
        text=requests.get(url+str(start)).text.encode('u8')#requsts经测试比urllib快
        start+=44
        if start>220:break #只抓取前5页
    fname=str(id)+'tb.txt'
    with open(fname,'w') as f:
        for i in range(len(name)): #按格式写入文件
            f.write(name[i][1]+'\n'+pic[i]+'\n'+name[i][0]+'\n'+price[i][0]+'\n'+price[i][1]+'\n'+deal[i]+'\n')
    return len(name)    
if __name__=="__main__":
    if len(sys.argv)==3:
        taobao(sys.argv[1],sys.argv[2])
        exit(0)
    else: exit(-1)

