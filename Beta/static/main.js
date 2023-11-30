function redirectlogin(params) {
    window.location.href = 'login.html';
}
function redirect_reg(params) {
    window.location.href = 'reg.html';
}
function redirect_set_q() {
    window.location.href = '{{ url_for('set_paper') }}';
}
function redirect_show_paper() {
    window.location.href = '{{ url_for('show_paper') }}';
}
let questionCount = 0;

function addQuestion() {
    questionCount++;

    const questionsContainer = document.getElementById('questions-container');

    const questionDiv = document.createElement('div');
    questionDiv.classList.add('question');

    questionDiv.innerHTML = `
    <h3>Question ${questionCount}: <input type="text" name="question${questionCount}" placeholder="Enter your question" /></h3>
    <label><input type="radio" name="q${questionCount}" value="a"> Option A</label>
    <label><input type="radio" name="q${questionCount}" value="b"> Option B</label>
    <label><input type="radio" name="q${questionCount}" value="c"> Option C</label>
    <label><input type="radio" name="q${questionCount}" value="d"> Option D</label>
    `;

    questionsContainer.appendChild(questionDiv);
}

function submitQuiz() {
    const responses = {};

    for (let i = 1; i <= questionCount; i++) {
        const selectedOption = document.querySelector(`input[name="q${i}"]:checked`);
            const questionText = document.querySelector(`input[name="question${i}"]`).value;

        if (selectedOption) {
            responses[`question${i}`] = {
                question: questionText,
                answer: selectedOption.value
            };
        } 
        else {
                alert(`Please select an option for Question ${i}`);
                return;
        }
    }

            // Send data to Flask using Ajax (Assuming you have a Flask route to handle this)
            fetch('/submit-paper', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ responses }),
            })
            .then(response => response.json())
            .then(data => {
                // Handle the response from the server
                console.log(data);
            })
            .catch(error => {
                console.error('Error:', error);
            });
        }