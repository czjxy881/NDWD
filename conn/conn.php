<?php 
$id=mysql_connect("localhost","root","asdf1234")or dir('连接失败:' . mysql_error());//链接数据库
if(mysql_select_db("test1",$id))
echo "";
else
echo ('连接失败:' . mysql_error());
mysql_query("set names gb2312");
mysql_query("create database test1");
?>