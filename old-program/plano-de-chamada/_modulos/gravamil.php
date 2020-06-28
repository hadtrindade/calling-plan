<?php
include ('../_crud/conexao.php');
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

	$nome=$_POST['nome'];
	$nome=strtoupper($nome);
	$fone=$_POST['fone'];
	$area=$_POST['area'];
	$su=$_POST['su'];
	$op=$_POST['op'];
	$cham=$_POST['cham'];
				
					
	$sql=mysqli_query($con,"INSERT INTO militares (nome,telefone,area,su,op,chamador) VALUES ('$nome','$fone','$area','$su','$op','$cham')") or die (mysqli_error($con));
						
?>
<?php
	echo "<meta http-equiv='refresh' content='0; URL=../index.php?mod=cadmil'>
		<script type=\"text/javascript\">
			alert(\"Militar cadastrado com sucesso\");
		</script>
								";
	mysqli_close($con);
?>
