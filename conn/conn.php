<?php 
$id=mysql_connect("localhost","root","asdf1234")or dir('����ʧ��:' . mysql_error());//�������ݿ�
if(mysql_select_db("test1",$id))
echo "";
else
echo ('����ʧ��:' . mysql_error());
mysql_query("set names gb2312");
mysql_query("create database test1");
?>