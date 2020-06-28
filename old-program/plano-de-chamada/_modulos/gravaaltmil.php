../<?php
include ('_crud/conexao.php');
	
	$nome=$_POST['nome'];
	$nome=strtoupper($nome);
	$grad=$_POST['grad'];
	$cpf=$_POST['cpf'];
	$bco=$_POST['banco'];
	$ag=$_POST['agencia'];
	$cc=$_POST['conta'];
	$id=$_POST['id'];
		
	$sql1=mysqli_query ($con,"UPDATE militar SET nome='".$nome."',grad='".$grad."',cpf='".$cpf."',bco='".$bco."',ag='".$ag."',cc='".$cc."' WHERE id='".$id."'");
		
?>
<?php
echo "<meta http-equiv='refresh' content='0; URL=../index.php?mod=relmil'>
		<script type=\"text/javascript\">
		alert(\"Militar alterado com sucesso\");
		</script>
	";
	mysql_close($con);
?>