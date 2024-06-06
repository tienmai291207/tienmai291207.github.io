<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Kiểm tra IP và User Agent</title>
    <style>
        html, body {
            overflow: hidden;
            height: 100%;
            margin: 0;
            padding: 0;
        }

        @viewport {
            width: device-width;
            zoom: 1.0;
            min-zoom: 1.0;
            max-zoom: 1.0;
        }

        body {
            background-color: black;
            color: white;
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .container {
            background-color: #1e1e1e;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
            text-align: center;
        }

        .header-image {
            margin-bottom: 20px;
            width: 150px;
            height: auto;
        }

        h1, h2 {
            color: #00ff00;
        }

        p {
            margin: 5px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <img class="header-image" src="https://i.imgur.com/Q1o6Bo1.png" alt="Header Image">
        <?php
        function getUserIP() {
            $ip = '';
            if (isset($_SERVER['HTTP_CLIENT_IP'])) {
                $ip = $_SERVER['HTTP_CLIENT_IP'];
            } elseif (isset($_SERVER['HTTP_X_FORWARDED_FOR'])) {
                $ip = $_SERVER['HTTP_X_FORWARDED_FOR'];
            } elseif (isset($_SERVER['REMOTE_ADDR'])) {
                $ip = $_SERVER['REMOTE_ADDR'];
            }
            return $ip;
        }

        $ip = getUserIP();
        $user_agent = $_SERVER['HTTP_USER_AGENT'];
        $url = "http://ip-api.com/json/$ip";

        $response = file_get_contents($url);
        $data = json_decode($response, true);

        if ($data && $data['status'] == 'success') {
            echo "<h2>Thông tin IP</h2>";
            echo "<p>IP: " . $data['query'] . "</p>";
            echo "<p>Quốc gia: " . $data['country'] . "</p>";
            echo "<p>Thành phố: " . $data['city'] . "</p>";
            echo "<p>Mạng: " . $data['isp'] . "</p>";
            echo "<h2>User Agent</h2>";
            echo "<p>" . $user_agent . "</p>";
        } else {
            echo "<p>Không tìm thấy thông tin cho IP này.</p>";
        }
        ?>
    </div>
</body>
</html>