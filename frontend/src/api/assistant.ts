const API_URL = "http://localhost:8000/chat";

export async function sendMessage(message: string) {

    const response = await fetch(API_URL, {

        method: "POST",

        headers: {
            "Content-Type": "application/json",
        },

        body: JSON.stringify({
            message,
        }),

    });

    if (!response.ok) {
        throw new Error("Failed to call backend");
    }

    return response.json();

}