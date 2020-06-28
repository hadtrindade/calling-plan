<?php

require_once("fpdf.php");
$con=mysqli_connect("localhost","hadd","t0rn4d0","planochamada") or die(mysqli_error($con));


class PDF extends FPDF
{
    // Page header
    function Header()
    {
        // Logo
        //$this->Image('logo.png', 10, 6, 30);
        // Arial bold 15
        $this->SetFont('Arial', 'B', 15);
        // Move to the right
        // $this->Cell(80);
        // Title
        $this->SetTextColor(255,255,255);
        $this->Cell(272, 7, utf8_decode("Plano de Chamada Dia ".date("d/m/Y")), 1, 0, 'C',1);
        $this->ln();
        $this->SetTextColor(255,255,255);
        $this->cell(140,5,"Nome",1,0,'C',1);
        $this->cell(33,5,"Chamador",1,0,'C',1);
        $this->cell(33,5,"Hora",1,0,'C',1);
        $this->cell(33,5,utf8_decode("Área"),1,0,'C',1);
        $this->cell(33,5,utf8_decode("Situação"),1,0,'C',1);
        $this->ln();
        // Line break
        $this->Ln(5);
    }
    // Page footer
    function Footer()
    {
        // Position at 1.5 cm from bottom
        $this->SetY(-15);
        // Arial italic 8
        $this->SetFont('Arial','I',8);
        // Page number
        $this->SetTextColor(255,255,255);
        $this->Cell(272,7,utf8_decode('Plano de Chamada  '.date("d/m/Y ")).$this->PageNo().'/{nb}',0,0,'R',1);
    }
}

function pronto ($var){
	            if ($var == 1){
	              return "Pronto";
		    }else{
	              return "Problemas";
		            }
		    };
function chamador ($var){
	            if ($var == 1){
	              return "Sim";
		    }else{
	              return "Não";
		            }
		    };




$pdf=new PDF('L','mm','A4');
$pdf->AddPage();
$pdf->AliasNbPages();
$pdf->setfont('Arial', 'B', 8);
$data = date("d:m:Y");
$sql=mysqli_query($con,"SELECT * FROM relatorio");
while($ln=mysqli_fetch_array($sql,MYSQLI_ASSOC)) {
	$militar=$ln['militar'];
	$chamador=$ln['chamador'];
	$area=$ln['area'];
	$horaat=$ln['horaatendimento'];
	$pronto=$ln['pronto'];

    $pdf->SetTextColor(0,0,0);
    $pdf->cell(140, 5, $militar, 1, 0, 'J');
    $pdf->cell(33, 5, utf8_decode(chamador($chamador)), 1, 0, 'J');
    $pdf->cell(33, 5, $horaat, 1, 0, 'J');
    $pdf->cell(33, 5, $area, 1, 0, 'J');
    $pdf->cell(33, 5, pronto($pronto), 1, 0, 'J');
    $pdf->ln();
}
$pdf->ln();
ob_clean();
$pdf->output("Plano de chamada","I");
?>
