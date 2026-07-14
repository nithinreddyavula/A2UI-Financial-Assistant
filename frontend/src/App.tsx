import { useState } from "react";

import Renderer from "./components/Renderer";
import { sendMessage } from "./api/assistant";

import type { UIComponent } from "./types/ui";

function App() {

    const [message, setMessage] = useState("");

    const [currentMessage, setCurrentMessage] = useState("");

    const [ui, setUi] = useState<UIComponent | null>(null);

    async function handleSend() {

        if (!message.trim()) return;

        setCurrentMessage(message);

        const response = await sendMessage(message);

        setUi(response.ui);

        setMessage("");

    }
    async function handleFormSubmit(formData: {
        amount: string;
        risk: string;
        horizon: string;
    }) {

        console.log("App received:", formData);

        const response = await sendMessage(
            currentMessage,
            formData
        );
        console.log("Backend Response:", response);
        console.log("UI:", response.ui);

        setUi(response.ui);

    }

    return (

        <div>

            <h1>A2UI Financial Assistant</h1>

            <input
                type="text"
                value={message}
                onChange={(e) => setMessage(e.target.value)}
                placeholder="Ask anything..."
            />

            <button onClick={handleSend}>
                Send
            </button>

            <hr />

            {ui && (

                <Renderer
                    component={ui}
                    onFormSubmit={handleFormSubmit}
                />

            )}

        </div>

    );

}

export default App;