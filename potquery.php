<?php
// Function to format and colorize the output
function format_output($data, $indent_level = 0)
{
    $indent = str_repeat('  ', $indent_level);
    $formatted_output = '';
    foreach ($data as $key => $value) {
        // Check if the value is an array or a dictionary
        if (is_array($value)) {
            // If the value is an array, recursively format the output
            $formatted_output .= $indent . "<b>" . $key . "</b><br />";
            $formatted_output .= format_output($value, $indent_level + 1);
        } elseif (is_object($value)) {
            // If the value is an object (dictionary), recursively format the output
            $formatted_output .= $indent . "<b>" . $key . "</b><br />";
            $formatted_output .= format_output((array)$value, $indent_level + 1);
        } else {
            // If the value is not an array or object, format it and append it to the output
            $formatted_output .= $indent . "<b>" . $key . "</b> : " . $value . "<br />";
        }
    }
    return $formatted_output;
}

// Function to get data from Alderon Games servers
function get_servers($name = "", $addr = "")
{
    if (empty($addr) && !empty($name)) {
        $url = "https://servers.alderongames.com/pathOfTitans?filter[name]={$name}&filter[official]=0&filter[platform]=mac&page=0";
    } elseif (!empty($addr) && empty($name)) {
        $url = "https://servers.alderongames.com/pathOfTitans?filter[ip_address]={$addr}&filter[official]=0&filter[platform]=mac&page=0";
    } elseif (!empty($addr) && !empty($name)) {
        $url = "https://servers.alderongames.com/pathOfTitans?filter[ip_address]={$addr}&filter[name]={$name}&filter[official]=0&filter[platform]=mac&page=0";
    } else {
        return "Please provide at least one parameter e.g. (?name=servername&addr=1.1.2.3)";
    }

    // Make HTTP request to get the data
    $response = file_get_contents($url);
    $data = json_decode($response, true);

    // Format and colorize the output
    $formatted_data = format_output($data['data']);

    // Return the formatted output
    return $formatted_data;
}

// Get parameters from the URL and call the get_servers function
$name = $_GET['name'] ?? '';
$addr = $_GET['addr'] ?? '';
$output = get_servers($name, $addr);

// Output the formatted data
echo $output;
?>
