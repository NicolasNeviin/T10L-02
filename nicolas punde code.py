<DOCTYPE html>
<html>
<head>
    <title>Quiz</title>
    <script>
        function checkAnswers() {
            var Quiz = document.getElementById("Quiz").value;
            var Quiz_1 = document.getElementById("Quiz_1").value;
            var Quiz_2 = document.getElementById("Quiz_2").value;
            var Quiz_3 = document.getElementById("Quiz_3").value;
            var Quiz_4 = document.getElementById("Quiz_4").value;
            var Quiz_5 = document.getElementById("Quiz_5").value;

            var C = "Correct";
            var W = "Wrong";

            document.getElementById("result_Quiz").innerHTML = (Quiz.toLowerCase() === "apple") ? C : W;
            document.getElementById("result_Quiz_1").innerHTML = (Quiz_1 === "0") ? C : W;
            document.getElementById("result_Quiz_2").innerHTML = (Quiz_2.toLowerCase() === "ok") ? C : W;
            document.getElementById("result_Quiz_3").innerHTML = (Quiz_3 === "10") ? C : W;
            document.getElementById("result_Quiz_4").innerHTML = (Quiz_4 === "14") ? C : W;
            document.getElementById("result_Quiz_5").innerHTML = (Quiz_5 === "36") ? C : W;
        }
    </script>
</head>
<body>
    <h1>Quiz</h1>
    <p>What is red? <input type="text" id="Quiz"></p>
    <p id="result_Quiz"></p>

    <p>What is 1 * 0? <input type="text" id="Quiz_1"></p>
    <p id="result_Quiz_1"></p>

    <p>How are you? <input type="text" id="Quiz_2"></p>
    <p id="result_Quiz_2"></p>

    <p>5 + 5? <input type="text" id="Quiz_3"></p>
    <p id="result_Quiz_3"></p>

    <p>7 + 7? <input type="text" id="Quiz_4"></p>
    <p id="result_Quiz_4"></p>

    <p>6 * 6? <input type="text" id="Quiz_5"></p>
    <p id="result_Quiz_5"></p>

    <button onclick="checkAnswers()">Submit</button>
</body>
</html>
                    