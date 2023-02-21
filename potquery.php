<?

/*
(c) 2022 by Deniz K.
Simple PHP-Script to grab POT-Server Data

TODO: Parse Arrays and maybe display Server-Data nicer
*/

//Get Name and/or IP-Address

$name = $_GET['name'];
$addr = $_GET['addr'];

//Function to grab Data from alderongames servers

function getservers ($name="", $addr="") {
    if (empty($addr) && !empty($name)) {
        $json = file_get_contents("https://servers.alderongames.com/pathOfTitans?filter[name]={$name}&filter[branch]=production&filter[version]=22351&filter[official]=0&filter[platform]=mac&page=0");
        $array_data = json_decode($json, true);
        $data = "<pre>" . print_r($array_data['data'], true) . "</pre>";
        return $data;
    }
    else if (!empty($addr) && empty($name)) {
        $json = file_get_contents("https://servers.alderongames.com/pathOfTitans?filter[ip_address]={$addr}&filter[branch]=production&filter[version]=22351&filter[official]=0&filter[platform]=mac&page=0");
        $array_data = json_decode($json, true);
        $data = "<pre>" . print_r($array_data['data'], true) . "</pre>";
        return $data;
    }
    else if ((!empty($addr) && !empty($name))) {
        $json = file_get_contents("https://servers.alderongames.com/pathOfTitans?filter[ip_address]={$addr}&filter[name]={$name}&filter[branch]=production&filter[version]=22351&filter[official]=0&filter[platform]=mac&page=0");
        $array_data = json_decode($json, true);
        $data = "<pre>" . print_r($array_data['data'], true) . "</pre>";
        return $data;
    }
    else {
        $data = "Please provide at least one parameter e.g. (?name=servername&addr=1.1.2.3)";
        return $data;
    }
}


print (getservers($name, $addr));