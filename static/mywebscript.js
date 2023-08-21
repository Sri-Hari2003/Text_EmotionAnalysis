let displayError = (errorMessage) => {
    let errorHtml = `<div class="alert alert-danger" role="alert">${errorMessage}</div>`;
    document.getElementById("system_response").innerHTML = errorHtml;
}

let runSentimentAnalysis = () => {
    let textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4) {
            if (this.status == 200) {
                let response = JSON.parse(xhttp.responseText);
                if (response.status === "error") {
                    displayError(response.message);
                } else {
                    displayResults(response);
                }
            } else {
                displayError("An error occurred while processing the request.");
                try {
                    let response = JSON.parse(xhttp.responseText);
                    if (response.status === "error") {
                        displayError(response.message);
                    }
                } catch (error) {
                    displayError("An error occurred while processing the request.");
                }
            }
        }
    };
    
    xhttp.open("GET", "/emotionDetector?textToAnalyze=" + encodeURIComponent(textToAnalyze), true);
    xhttp.send();
}

let displayResults = (response) => {
    let totalScore = 0;
    for (let emotion in response) {
        totalScore += response[emotion];
    }

    let dominantEmotion = "";
    let maxScore = 0;
    let resultHtml = "<ul>";
    for (let emotion in response) {
        let score = (response[emotion] / totalScore) * 100;
        resultHtml += `<li>${emotion}: ${score.toFixed(2)}%</li>`;
        
        if (score > maxScore) {
            maxScore = score;
            dominantEmotion = emotion;
        }
    }
    resultHtml += "</ul>";

    resultHtml += `<p>Dominant Emotion: ${dominantEmotion}</p>`;

    document.getElementById("system_response").innerHTML = resultHtml;
}
