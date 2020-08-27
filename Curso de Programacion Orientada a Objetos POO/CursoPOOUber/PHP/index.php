<?php

    require_once('Car.php');
    require_once('uberX.php');
    require_once('uberPool.php');
    require_once("Account.php");
    
    $uberX = new UberX("CVB123", new Account("Andres Herrera","AND456","Chevrolet","Spark"));

    $uberX->printDataCar();
    $uberPool = new UberPool("CVB123", new Account("Andres Herrera","AND456","Chevrolet","Spark"));

    $uberPool->printDataCar();


?>