<?php

$SONDE_TEMPERATURE_CORRECTION='-3';	

$array_data['screen']=1; 
$array_data['smallScreen']=0;
$array_data['desc']='Température du local technique';
$array_data['value']=round(Temperature_USB('/usr/bin/sudo /opt/temperv14/temperv14 -c')+$SONDE_TEMPERATURE_CORRECTION, 1);
$array_data['units']='°C';

return $array_data;

?>
