def get_fallback_ui() -> dict:

    return {
        "type": "container",
        "id": "errorContainer",
        "children": [
            {
                "type": "card",
                "id": "errorCard",
                "title": "Something went wrong",
                "children": [
                    {
                        "type": "text",
                        "id": "errorText",
                        "value": "Unable to generate the interface. Please try again."
                    }
                ]
            }
        ]
    }