#encoding=gbk
import urllib2,urllib,requests,re,sys
import db
pic=[];name=[];price=[]
def find(t):
    '''
        查询当前源代码(t)中的商品，并加入总表,返回值为成功查找到的数量
        参数说明：
            t: 所查询源代码  
    '''
    global pic,name,price,deal
    #获取亚马逊图片地址
    r_pic=re.compile(u'src=\"(.*?)\".*? alt=\"\u4ea7\u54c1\u8be6\u7ec6\u4fe1\u606f\"')
    #获取商品名称及地址
    r_name=re.compile('<div class=\"productTitle\"><a href=\"(.*?)\">(.*?)</a> </div>')
    #获取商品价格及运费
    r_price=re.compile(u'<span>\uffe5\s*(.*?)<')
    pic+=r_pic.findall(t)
    name+=r_name.findall(t)
    price+=r_price.findall(t)
    #print len(pic),len(name),len(price)
    return len(pic)
def zcn(s,id):
    '''
      查询淘宝中此商品信息，s为关键词,id为生成id，将查到的商品保存到数据库id表中并返回成功数目
      参数说明：
         s： 关键词
    '''
    global pic,name,price,deal
    pic=[];name=[];price=[];deal=[] #清零
    #将关键词转成网页编码
    s=urllib.quote(s)
    s.replace('%20','+')
    url='http://www.amazon.cn/s/field-keywords=%s'%s
    start=0 #起始位置
    text="" #查询内容
    db.create(id)
    text=requests.get(url).text#requsts经测试比urllib快
    find(text)
    s=[1,2,3,4,5,6,7]
    for i in range(len(name)): #按格式写入文件
        s[0]=name[i][1].encode('gbk');s[1]=pic[i].encode('gbk');s[2]=name[i][0].encode('gbk');
        s[3]=(price[i].encode('gbk')).replace(',','')
        s[4]=-1;s[5]=-1;s[6]='亚马逊'
        #print s
        db.add(id,s)
    return len(name)    
if __name__=='__main__':
      #zcn('nx300','ttt')
      if len(sys.argv)==3:#命令行参数处理
        zcn(sys.argv[1],sys.argv[2])
        exit(0)
      else: exit(-1)
