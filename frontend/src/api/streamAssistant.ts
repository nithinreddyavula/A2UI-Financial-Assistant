const API_URL = "http://localhost:8000/chat/stream";

type StreamCallbacks = {
    onStatus: (status: string) => void;
    onResult: (ui: any) => void;
};

export async function streamMessage(
    message: string,
    callbacks: StreamCallbacks
) {

    const response = await fetch(API_URL, {

        method: "POST",

        headers: {
            "Content-Type": "application/json",
        },

        body: JSON.stringify({
            message
        })

    });

    const reader = response.body?.getReader();

    if (!reader) return;

    const decoder = new TextDecoder();

    while (true) {

        const { value, done } = await reader.read();

        if (done) break;

        const chunk = decoder.decode(value);

        const lines = chunk.split("\n");

        for (const line of lines) {

            if (!line.startsWith("data: ")) continue;

            const data = line.replace("data: ", "");

            try {

                const ui = JSON.parse(data);

                callbacks.onResult(ui);

            }

            catch {

                callbacks.onStatus(data);

            }

        }

    }

}