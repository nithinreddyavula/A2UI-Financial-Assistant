const API_URL = "http://localhost:8000/chat";

type FormData = {
    amount: string;
    risk: string;
    horizon: string;
};

export async function sendMessage(
    message: string,
    formData?: FormData
) {

    const response = await fetch(API_URL, {

        method: "POST",

        headers: {
            "Content-Type": "application/json",
        },

        body: JSON.stringify({
            message,
            formData,
        }),

    });

    if (!response.ok) {
        throw new Error("Failed to call backend");
    }

    return response.json();
}