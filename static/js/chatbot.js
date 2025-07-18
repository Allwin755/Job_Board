// static/js/chatbot.js

document.addEventListener("DOMContentLoaded", function () {
    const chatForm = document.getElementById("chat-form");
    const chatInput = document.getElementById("chat-input");
    const chatMessages = document.getElementById("chat-messages");

    chatForm.addEventListener("submit", async function (e) {
        e.preventDefault();
        const userMessage = chatInput.value.trim();
        if (!userMessage) return;

        appendMessage("You", userMessage);
        chatInput.value = "";

        try {
            const response = await fetch("/chat", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ message: userMessage }),
            });

            const data = await response.json();
            appendMessage("Bot", data.reply);
        } catch (err) {
            appendMessage("Bot", "Oops! Something went wrong.");
        }
    });

    function appendMessage(sender, message) {
        const messageElem = document.createElement("div");
        messageElem.className = "message " + sender.toLowerCase();
        messageElem.innerHTML = `<strong>${sender}:</strong> ${message}`;
        chatMessages.appendChild(messageElem);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
});
