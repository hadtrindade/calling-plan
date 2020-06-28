<?php
include ('_crud/conexao.php');

	$id = $_POST['id'];
	
	$sql=mysqli_query($con,"SELECT * from militar WHERE id='$id'");
	while($ln=mysqli_fetch_array($sql)){
		$grad=$ln['grad'];	
		$nome=$ln['nome'];
		$cpf=$ln['cpf'];
		$bco=$ln['bco'];
		$ag=$ln['ag'];
		$cc=$ln['cc'];
	}
?>

<h2 align="center"> Altera Cadastro de Militares</h2>
<hr /><hr />
<form method="post" action="_modulos/gravaaltmil.php">
Nome:<input type="text" name="nome"  size="80" value="<?php echo $nome; ?>"/>
Posto/Grad:
<select name="grad">
		<option value="<?php echo $grad; ?>" selected><?php echo $grad; ?></option>
		<option value="Cel">Cel</option>
    	<option value="Ten Cel">Ten Cel</option>
    	<option value="Maj">Maj</option>
    	<option value="Cap">Cap</option>
    	<option value="1º Ten">1º Ten</option>
    	<option value="2º Ten">2º Ten</option>
    	<option value="Asp">Asp</option>
    	<option value="S Ten">S Ten</option>
    	<option value="1º Sgt">1º Sgt</option>
    	<option value="2º Sgt">2º Sgt</option>
    	<option value="3º Sgt">3º Sgt</option>
    	<option value="Cb">Cb</option>
    	<option value="Sd">Sd</option>
</select>
<br><br>
CPF:<input type="text" name="cpf" value="<?php echo $cpf; ?>"><font color="#FF0000"> (Ex:. 999.999.999-99)</font>
<br><br>
Banco:
<select name="banco">
		<option value="<?php echo $bco; ?>" selected><?php echo $bco; ?></option>
		<option value="001">001</option>
        <option value="033">033</option>
    	<option value="104">104</option>
        <option value="237">237</option>
        <option value="341">341</option>
        <option value="399">399</option>
</select>
Agência: <input type="text" name="agencia" value="<?php echo $ag; ?>">
Conta: <input type="text" name="conta" value="<?php echo $cc; ?>">
<br><br>
<input type="hidden" name="id" value="<?php echo $id; ?>" />
<input type="submit" value="Alterar">
</form>

