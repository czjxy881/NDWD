<!DOCUMENT HTML>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb2312">
<link rel="shortcut icon" href="./source/4.ico" >
<title>����ҵ�-�����ڹ��������˹���Ԥ�ıȼ���վ</title>
<style type="text/css">
<!--
.STYLE1 {font-family: "������", "�����п�"}
.STYLE2 {
	font-family: "�����п�";
	font-size: 60px;
}
.STYLE3 {font-size: 18px}
.STYLE4 {font-size: 24px}
<!--�ٶ���ʽ�� -->
#kw,.btn{background:url(http://su.bdimg.com/static/superpage/img/spis_9762e054.png) no-repeat #fff}
#kw{
width:529px;
height:32px;
padding:4px 7px;
padding:6px 7px 2px\9;
font:16px arial;
border:1px solid #cdcdcd;
border-color:#9a9a9a #cdcdcd #cdcdcd #9a9a9a;
vertical-align:top;
outline:none}
.btn{width:95px;height:32px;padding:0;padding-top:2px\9;border:0;background-position:0 -35px;background-color:#ddd;cursor:pointer}
-->
</style>
</head>

<body>
 <?php echo "<p style='font-size:14px; color:#000099; font-family:'΢���ź�''>��ӭ<b>".$_SERVER['REMOTE_ADDR']."</b>������</p>"; ?>
<hr>
<div align="center" class="STYLE1">
  <p><img src="./source/pic.jpg" width="264" height="107"></p>
  <form name="form1" method="get" action="search.php">
    <span class="STYLE3">��Ʒ���ƣ�</span>
	<input type="text" name="s" id="kw" maxlength="100" style="width:474px;">
	<input type="submit" name="sub" value="����" id="su" class="btn">
	<br>
	<input type="radio" name="order" value="price">�۸�����
	<input type="radio" name="order" value="price desc">�۸���
	<input type="radio" name="order" value="sell">��������
	<input type="radio" name="order" value="sell desc">��������
  </form>
</div>

</body>
</html>
