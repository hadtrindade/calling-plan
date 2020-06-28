<div id="formulario">
    <form method="post" action="_modulos/gravamil.php">

        <legend>Militar:</legend>
        <table>
            <tr>
                <td><span><label for="cNome">Nome:</label></td><td><input type="text" name="nome" placeholder="NOME COMPLETO" id="cNome" required="required" size="40" /></span></td>
                <td><span><label for="cfone">Telefone:</label></td><td><input type="text" name="fone" placeholder="sipuser ou 084000000000" id="cfone" required="required"/> </span></td>

                <td><label for="carea">Área:</label></td>
            <td><select name="area" id="carea">
                    <option value="1">1</option>
                    <option value="2" selected >2</option>
                </select>
            </td>
            </tr>
            <tr>
                <td><label for="csu">Su:</label></td>
                <td><select name="su" id="csu" >
                        <option value="bc">Bia C</option>
                        <option value="1bo" >1ª Bia O</option>
                        <option value="2bo" >2ª Bia O</option>
                    </select>
                </td>
                <td><label for="cop">Operacional:</label></td>
                    <td><select name="op" id="cop" >
                            <option value="1">Sim</option>
                            <option value="0" >Não</option>
                        </select>
                    </td>

                <td><label for="ccham">Chamador:</label></td>
                <td><select name="cham" id="ccham">
                        <option value="1">Sim</option>
                        <option value="0" selected >Não</option>
                    </select>
                </td>
            </tr>
        </table>
        <p style="text-align: center"><input type="submit" value="Gravar" class="botao"/> </p>
    </form>
</div>

