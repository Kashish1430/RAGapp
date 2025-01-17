document.addEventListener('DOMContentLoaded', () => {
    const chatMessages = document.getElementById('chat-messages');
    const userInput = document.getElementById('user-input');
    const submitBtn = document.getElementById('submit-btn');
    const loadingElement = document.getElementById('loading');

    submitBtn.addEventListener('click', sendMessage);
    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });

    function sendMessage() {
        const message = userInput.value.trim();
        if (message) {
            addMessageToChat('user', message);
            fetchResponse(message);
            userInput.value = '';
        }
    }

    function addMessageToChat(sender, message, sources = null) {
    const messageElement = document.createElement('div');
    messageElement.classList.add('message', `${sender}-message`);
    messageElement.textContent = message;

    if (sources && sources.length > 0) {
        const sourcesElement = document.createElement('div');
        sourcesElement.classList.add('sources');
        sourcesElement.textContent = `Sources: ${sources.join(', ')}`;
        messageElement.appendChild(sourcesElement);
    }

    chatMessages.appendChild(messageElement);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

    async function fetchResponse(query) {
    try {
        loadingElement.classList.remove('hidden');
        submitBtn.disabled = true;
        userInput.disabled = true;

        const response = await fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ query: query }),
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        console.log('Response data:', data);  // Add this line for debugging
        addMessageToChat('bot', data.response, data.sources);
    } catch (error) {
        console.error('Error:', error);
        addMessageToChat('bot', 'Sorry, there was an error processing your request.');
    } finally {
        loadingElement.classList.add('hidden');
        submitBtn.disabled = false;
        userInput.disabled = false;
    }
}
});