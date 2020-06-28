<div id="tbconsulta">
    <table>
        <tr>
	<td id="cabecalho" colspan="7">Militaras Cadastrados no Plano de chamada <?php echo date("Y")  ?> </td>
        </tr>
        <tr>
            <td id="cabecalho">Nome</td>
	    <td id="cabecalho">Telefone</td>
	    <td id="cabecalho">Area</td>
            <td id="cabecalho">Sub Unidade</td>
            <td id="cabecalho">Operacional</td>
            <td id="cabecalho">Chamador</td>
            <td id="cabecalho">Excluir</td>
        </tr>
        <?php
        require("_crud/conexao.php");
        function simnao ($var){
            if ($var == 1){
                return "Sim";
            }else{
                return "Não";
            }
        };
	
		$sql=mysqli_query($con,"SELECT * FROM militares ORDER BY op DESC, chamador DESC");
		while($ln=mysqli_fetch_array($sql,MYSQLI_ASSOC)) {
			   $id=$ln['id'];
		           $nome = $ln['nome'];
		           $fone = $ln['telefone'];
		           $area = $ln['area'];
		           $su = $ln['su'];
		           $op = $ln['op'];
		           $cham = $ln['chamador'];

							            ?>
            <tr>
                <td id="normal"><p><?php echo $nome; ?></p></td>
                <td id="normalCentro"><?php echo $fone; ?></td>
                <td id="normalCentro"><?php echo $area; ?></td>
                <td id="normalCentro"><?php echo strtoupper($su); ?></td>
                <td id="normalCentro"><?php echo simnao($op); ?></td>
                <td id="normalCentro"><?php echo simnao($cham); ?></td>
		<td id="normalCentro">
     			<form method="post" action="_modulos/delmil.php">
        			<input type="hidden" name="id" value="<?php echo $id; ?>" />
        	 		<input type="image" src="_imagens/excluir.png" width="30" onClick="this.form.submit()">
        		</form>
     		</td>
            </tr>
	<?php
        }
        ?>
    </table>
</div>

