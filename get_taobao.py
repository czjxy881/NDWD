#encoding=gbk
import urllib2,urllib,requests,re,sys
import db
#ͼƬ�����ƣ��۸���ܱ�
pic=[];name=[];price=[];deal=[]
def find(t):
    '''
        ��ѯ��ǰԴ����(t)�е���Ʒ���������ܱ�,����ֵΪ�ɹ����ҵ�������
        ����˵����
            t: ����ѯԴ����  
    '''
    global pic,name,price,deal
    #��ȡ�Ա�ͼƬ��ַ
    r_pic=re.compile('<p class=\"pic-box\">.*\s*<span><img src=\"(.*?)\" />')
    #��ȡ��Ʒ���Ƽ���ַ
    r_name=re.compile('<h3 class="summary"><a .*? href=\"(.*?)\" target=\"_blank\" title=\"(.*?)\">')
    #��ȡ��Ʒ�۸��˷�
    r_price=re.compile('<div class=\"col price\">(.*?)<em></em></div>\s*<div class=\"col end shipping\">\s*(.*?)\s*</div>')   
    #��ȡ�ɽ���
    r_deal=re.compile('<div class="col dealing">.*?(\d+)')
    
    #����ҳ��Ϣ�ӵ��ܱ���
    pic+=r_pic.findall(t)
    name+=r_name.findall(t)
    deal+=r_deal.findall(t)
    
    #���Ա��ļ۸��˷ѱ��������ʽ
    pt=r_price.findall(t)
    p=[1,2]
    for i in range(len(pt)):
        p[0]=pt[i][0][3:]
        if pt[i][1].decode('u8')=='���˷�'.decode('gbk'):p[1]='0.00'
        else: p[1]=pt[i][1][9:]
        pt[i]=list(p) #ֱ�ӵ���Ϊ���ã��˴�Ӧ�ø���
    price+=pt
    return len(pic)
def taobao(s,id):
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
    url='http://s.taobao.com/search?q=%s&s='%s
    start=0 #��ʼλ��
    text="" #��ѯ����
    db.create(id)
    while start==0 or find(text)!=0:
        text=requests.get(url+str(start)).text.encode('u8')#requsts�����Ա�urllib��
        start+=44
        if start>220:break #ֻץȡǰ5ҳ
    s=[1,2,3,4,5,6,7]
    for i in range(len(name)): #����ʽд���ļ�
        s[0]=name[i][1].decode('u8').encode('gbk');s[1]=pic[i];s[2]=name[i][0];s[3]=price[i][0]
        s[4]=price[i][1];s[5]=deal[i];s[6]='�Ա�'
        #print s
        db.add(id,s)
    return len(name)    
if __name__=="__main__":
   # taobao('nx300','t5')
    if len(sys.argv)==3:#�����в�������
        taobao(sys.argv[1],sys.argv[2])
        exit(0)
    else: exit(-1)

