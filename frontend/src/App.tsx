import { useState } from "react";
import "./App.css";

import Renderer from "./components/Renderer";
import { sendMessage } from "./api/assistant";
import { streamMessage } from "./api/streamAssistant";

import type { UIComponent } from "./types/ui";

function App() {

    const [message, setMessage] = useState("");

    const [currentMessage, setCurrentMessage] = useState("");

    const [ui, setUi] = useState<UIComponent | null>(null);

    const [status, setStatus] = useState("");

    const [loading, setLoading] = useState(false);

    async function handleSend() {

        if (!message.trim() || loading) return;

        setLoading(true);

        setCurrentMessage(message);

        setUi(null);

        setStatus("");

        const userMessage = message;

        setMessage("");

        await streamMessage(
            userMessage,
            {
                onStatus: (status) => {
                    setStatus(status);
                },

                onResult: (ui) => {
                    setUi(ui);
                    setStatus("");
                    setLoading(false);
                }
            }
        );

    }

    async function handleFormSubmit(formData: {
        amount: string;
        risk: string;
        horizon: string;
    }) {

        const response = await sendMessage(
            currentMessage,
            formData
        );

        setUi(response.ui);

    }

    return (

        <div className="app">

            <div className="header">

                <h1>
                    A2UI Financial Assistant
                </h1>

                <p>
                    AI Powered Financial Advisory Assistant
                </p>

            </div>

            <div className="input-section">

                <input
                    type="text"
                    value={message}
                    placeholder="Ask anything..."
                    onChange={(e) => setMessage(e.target.value)}
                    onKeyDown={(e) => {
                        if (e.key === "Enter") {
                            handleSend();
                        }
                    }}
                />

                <button
                    onClick={handleSend}
                    disabled={loading}
                >

                    {loading ? "Thinking..." : "Send"}

                </button>

            </div>

            {status && (

                <div className="progress-card">

                    <div className="thinking">

                        <span className="dot"></span>

                        <span>{status}</span>

                    </div>

                </div>

            )}

            <div className="response-section">

                {

                    ui && (

                        <Renderer
                            component={ui}
                            onFormSubmit={handleFormSubmit}
                        />

                    )

                }

            </div>

        </div>

    );

}

export default App;