#encoding=gbk
import urllib2,urllib,requests,re,sys
import db
pic=[];name=[];price=[]
def find(t):
    '''
        ��ѯ��ǰԴ����(t)�е���Ʒ���������ܱ�,����ֵΪ�ɹ����ҵ�������
        ����˵����
            t: ����ѯԴ����  
    '''
    global pic,name,price,deal
    #��ȡ����ѷͼƬ��ַ
    r_pic=re.compile(u'src=\"(.*?)\".*? alt=\"\u4ea7\u54c1\u8be6\u7ec6\u4fe1\u606f\"')
    #��ȡ��Ʒ���Ƽ���ַ
    r_name=re.compile('<div class=\"productTitle\"><a href=\"(.*?)\">(.*?)</a> </div>')
    #��ȡ��Ʒ�۸��˷�
    r_price=re.compile(u'<span>\uffe5\s*(.*?)<')
    pic+=r_pic.findall(t)
    name+=r_name.findall(t)
    price+=r_price.findall(t)
    #print len(pic),len(name),len(price)
    return len(pic)
def zcn(s,id):
    '''
      ��ѯ�Ա��д���Ʒ��Ϣ��sΪ�ؼ���,idΪ����id�����鵽����Ʒ���浽���ݿ�id���в����سɹ���Ŀ
      ����˵����
         s�� �ؼ���
    '''
    global pic,name,price,deal
    pic=[];name=[];price=[];deal=[] #����
    #���ؼ���ת����ҳ����
    s=urllib.quote(s)
    s.replace('%20','+')
    url='http://www.amazon.cn/s/field-keywords=%s'%s
    start=0 #��ʼλ��
    text="" #��ѯ����
    db.create(id)
    text=requests.get(url).text#requsts�����Ա�urllib��
    find(text)
    s=[1,2,3,4,5,6,7]
    for i in range(len(name)): #����ʽд���ļ�
        s[0]=name[i][1].encode('gbk');s[1]=pic[i].encode('gbk');s[2]=name[i][0].encode('gbk');
        s[3]=(price[i].encode('gbk')).replace(',','')
        s[4]=-1;s[5]=-1;s[6]='����ѷ'
        #print s
        db.add(id,s)
    return len(name)    
if __name__=='__main__':
      #zcn('nx300','ttt')
      if len(sys.argv)==3:#�����в�������
        zcn(sys.argv[1],sys.argv[2])
        exit(0)
      else: exit(-1)
