<?php
switch (isset($_GET['mod'])?$_GET['mod']:"princ") {

        case 'princ':
            include "principal.php";
		break;

        case 'cadmil':
            	include "cadmil.php";	
		break;
			
	case 'relplano':
		include "relatorioplano.php";
		break;
		
	case 'relmil':
		include "relatorio.php";
		break;
		
	case 'gravamil':
		include "gravamil.php";
		break;
		
	case 'altmil':
		include "altmil.php";
		break;
		
	case 'od':
		include "od.php";
		break;
		
	case 'relod':
		include "relod.php";
		break;
}		
?>
