<!DOCUMENT HTML>
<link rel="shortcut icon" href="4.ico" >
<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
<?php
	if(!isset($_GET['s'])||$_GET['s']=="")
	{
		echo '<meta http-equiv="refresh" content="0; url=1.php" />';
	}
	else
	{
		$s=$_GET['s'];
		if(isset($_GET['id']))$it=$_GET['id'];
		else $it='t'.rand(0,200000);
		if(isset($_GET['order']))$order=$_GET['order'];
		else $order='price';
	}
?>
<style type="text/css">
<!--
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
}
.btn{width:95px;height:32px;padding:0;vertical-align:top;padding-top:2px\9;border:0;background-position:0 -35px;background-color:#ddd;cursor:pointer}
.STYLE4 {
	font-size: x-large;
	color: #FF0000;
	font-weight: bold;
}
.STYLE5 {font-size: medium}
.STYLE6 {font-size: small}
-->
</style>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>你低我低-<?php echo $s;?></title>
</head>
<body>
<?php echo "<p style='font-size:14px; color:#000099; font-family:'微软雅黑''>欢迎<b>".$_SERVER['REMOTE_ADDR']."</b>的朋友</p>"; ?>
<hr>
<div>
	<tr></tr><tr></tr><tr></tr>
  <form name="form1" method="get" action="2.php">
    <p>
      <img src="pic.jpg" width="125" height="50">
      <input type="text" name="s" id="kw" value=<?php echo $s?> maxlength="100" style="width:474px;">
      <input type="submit" name="sub" value="搜索" id="su" class="btn">
    </p>
	<b><b><input type="radio" name="order" value="price">价格升序
	<input type="radio" name="order" value="price desc">价格降序
	<input type="radio" name="order" value="sell">销量升序
	<input type="radio" name="order" value="sell desc">销量降序
</form>

</div>

<?php
include_once ("conn/conn.php");
if ($_GET [page] == "") {
	$_GET [page] = 1;
}
;
if ($_GET [link_type] == "") {
	$_GET [link_type] = 0;
}
;
?>
<style type="text/css">
<!--
body,td,th {
	font-size: 12px;
}

a:link {
	text-decoration: none;
}

a:visited {
	text-decoration: none;
}

a:hover {
	text-decoration: none;
}

a:active {
	text-decoration: none;
}
-->
</style>
</head>

<body>

<table>
	<tr>
		<td height="330">&nbsp;</td>
		<td align="center" valign="top">
		<table width="520" align="center">
 <?php
 	$q=mysql_query("SHOW TABLES LIKE '".$it."'");
	if(mysql_num_rows($q)<=0)
	{
		system("python get_taobao.py ".$s." ".$it);//抓取淘宝数据
		system("python get_zcn.py ".$s." ".$it);//抓取亚马逊数据
	}
	$query_1 = mysql_query ( "select * from ".$it ); //获取数据库中总的记录数
	if (mysql_num_rows ( $query_1 ) <= 0) { //判断值是否为空
		?>
<tr>
				<td colspan="2" align="center">没有数据！</td>
			</tr>
<?php
	} else {
		$number = 0; //定义变量
		if ($_GET [page]) {
			$page_size = 40; //每页显示40条数据
			$query = "select count(*) as total from ".$it;
			$result = mysql_query ( $query );
			$message_count = mysql_result ( $result, 0, "total" ); //统计总的记录数
			$page_count = ceil ( $message_count / $page_size ); //计算总共有几页
			$offset = ($_GET [page] - 1) * $page_size; //获取当前页的起始页
			

			$query_2 = mysql_query ( "select * from ".$it." order by ".$order." limit $offset, $page_size" );
			while ( $myrow_2 = mysql_fetch_array ( $query_2 ) ) { //循环输出
				if (($number % 5) == 0) echo '<tr>';
?>
              <td colspan="2" align="center"><!--输出数据库中数据-->
				<table width="256" border="1" cellpadding="1" cellspacing="1"
					bordercolor="#FFFFFF" bgcolor="#D0D0D0">
					<tr>
						<td width="106" bgcolor="#FFFFFF">
						<div align="center"><a href="<?php echo $myrow_2 [url]; ?>"><img src="<?php echo $myrow_2 [pic]; ?>" width="100" height="120" border="0"></a></div>
						</td>
						<td width="170" valign="top" bgcolor="#FFFFFF">
						<table width="170" border="0" cellspacing="0" cellpadding="0">
							<tr>
								<td height="25" align="center">价格：</td>
								<td align="left"><span class="STYLE4"><?php echo $myrow_2 [price]; ?>元</span></td>
							</tr>
							<tr>
								<td height="25" align="center">运费：</td>
								<td align="left"><?php echo $myrow_2 [transport]; ?>元</td>
							</tr>
							<tr>
								<td height="25" align="center">成交量：</td>
								<td align="left"><?php echo $myrow_2 [sell]; ?></td>
							</tr>
								<tr>
								<td height="25" align="center">来源：</td>
								<td align="left"><?php echo $myrow_2 [from]; ?></td>
							</tr>
						</table>
						</td>
					</tr>
					<tr>
						<td height="28" colspan="2" align="center" valign="top"
							bgcolor="#FFFFFF">
						<table width="240">
							<tr>
								<td height="5"></td>
							</tr>
							<tr>
								<td><a href="<?php echo $myrow_2 [url]; ?>"><?php 
								$t=str_ireplace($s,"<font color='#FF0000'><strong>$s</strong></font>",$myrow_2 [name]);
								echo $t; ?></a></td>
							</tr>
							<tr>
								<td height="5"></td>
							</tr>
						</table>
						</td>
				</table>

<?php if ((++$number % 5) == 0)echo '</tr>';
		}
	}
}?>
</table>

		<table  height="30" border="1" align="right"
			cellpadding="1" cellspacing="1" bordercolor="#FFFFFF"
			bgcolor="#D0D0D0">
			<tr>
				<td  align="center" bgcolor="#FFFFFF"><span
					class="STYLE5"> <span class="STYLE6"></span>分页：
          <?php
										$next = $_GET [link_type] * 40;
										$n = $link_type - 1;
										$m = $link_type + 1;
										$prev_page = $_GET [page] - 40;
										?>
                <?php
																for($j = 1; $j <= $page_count; $j ++) {
																	$pnext = $next + $j;
																	if ($mm == 40) {
																		break;
																	}
																	if ($mm > $page_count) {
																		break;
																	}
																	if ($page_count - $vv < 40) {
																		if ($mm >= $page_count - $vv) {
																			break;
																		}
																	}
																	?>
                <?php
																	echo "<a href='2.php?s=$s&id=".$it."&page=$pnext'> $pnext </a>";
																	$mm = $mm + 1;
																}
																?>
        </span></td>
			</tr>
		</table>
		</td>
		<td>&nbsp;</td>
	</tr>
	<tr>
		<td height="109">&nbsp;</td>
		<td>&nbsp;</td>
		<td>&nbsp;</td>
	</tr>
</table>
</body>
</html>
	



      

</body>
</html>
