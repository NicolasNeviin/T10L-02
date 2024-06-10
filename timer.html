<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Timer App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
       .timer-container {
            position: absolute;
            top: 20px;
            right: 20px;
        }
       .timer-circle {
            width: 100px;
            height: 100px;
            border-radius: 50%;
            background-color: #fff;
            border: 2px solid #ddd;
            display: flex;
            justify-content: center;
            align-items: center;
        }
       .timer-text {
            font-size: 24px;
            font-weight: bold;
        }
       .input-container {
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="timer-container">
        <div class="timer-circle">
            <span id="timer-text" class="timer-text">00:00</span>
        </div>
    </div>
    <div class="input-container">
        <input id="seconds-input" type="number" value="0" />
        <button id="start-button">Start</button>
    </div>

    <script>
        let timer = 0;
        let intervalId = null;

        document.getElementById("start-button").addEventListener("click", () => {
            timer = parseInt(document.getElementById("seconds-input").value);
            intervalId = setInterval(() => {
                timer -= 1;
                updateTimerText();
                if (timer <= 3) {
                    beep();
                }
                if (timer <= 0) {
                    clearInterval(intervalId);
                }
            }, 1000);
        });

        function updateTimerText() {
            let minutes = Math.floor(timer / 60);
            let seconds = timer % 60;
            document.getElementById("timer-text").innerText = `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
        }

        function beep() {
            var audio = new Audio('beep.mp3');
            audio.play();
        }
    </script>
</body>
</html>