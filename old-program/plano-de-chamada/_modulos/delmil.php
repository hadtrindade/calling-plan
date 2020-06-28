<?php

ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

include ('../_crud/conexao.php');
	
	$id=$_POST['id'];
	
	$sql1=mysqli_query($con,"DELETE FROM militares WHERE id='$id'");
		
echo "<meta http-equiv='refresh' content='0; URL=../index.php?mod=relmil'>
		<script type=\"text/javascript\">
		alert(\"Militar excluido com sucesso\");
		</script>
	";
mysqli_close($con); 
 
?>
