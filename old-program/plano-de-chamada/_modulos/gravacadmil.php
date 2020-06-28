<?php
include ('_crud/conexao.php');
	
	$nome=$_POST['nome'];
	$grad=utf8_encode($_POST['grad']);
	$cpf=$_POST['cpf'];
	$bco=$_POST['banco'];
	$ag=$_POST['agencia'];
	$cc=$_POST['conta'];
	
	$sql=mysqli_query($con,"INSERT INTO militar (nome,grad,cpf,bco,ag,cc) values ('".$nome."','".$grad."','".$cpf."','".$bco."','".$ag."','".$cc."')");
?>
?>
<?php
echo "<meta http-equiv='refresh' content='0; URL=index.php?mod=cadmil'>
		<script type=\"text/javascript\">
		alert(\"Militar cadastrado com sucesso\");
		</script>
	";
	mysql_close($con);
?>