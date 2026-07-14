from app.agents.validator_agent import ValidatorAgent

validator = ValidatorAgent()

print("Test 1")
print(
    validator.validate(
        {
            "type": "container"
        }
    )
)

print()

print("Test 2")
print(
    validator.validate(
        {
            "type": "card"
        }
    )
)