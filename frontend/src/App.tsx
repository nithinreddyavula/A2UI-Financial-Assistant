import { useState } from "react";

import Renderer from "./components/Renderer";
import { sendMessage } from "./api/assistant";

import type { UIComponent } from "./types/ui";

function App() {

    const [message, setMessage] = useState("");

    const [ui, setUi] = useState<UIComponent | null>(null);

    async function handleSend() {

        if (!message.trim()) return;

        const response = await sendMessage(message);

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

                <Renderer component={ui} />

            )}

        </div>

    );

}

export default App;