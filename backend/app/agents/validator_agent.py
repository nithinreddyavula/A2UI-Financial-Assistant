from app.models.validation import ValidationResult

SUPPORTED_COMPONENTS = {
    "container",
    "card",
    "text",
    "button",
    "textField",
    "form",
    "badge",
    "chart",
    "dataTable"
}

PARENT_COMPONENTS = {
    "container",
    "card",
    "form"
}

LEAF_COMPONENTS = {
    "text",
    "button",
    "badge",
    "chart",
    "textField",
    "dataTable"
}


class ValidatorAgent:

    def validate(
        self,
        ui: dict
    ) -> ValidationResult:

        return self._validate_component(ui)

    def _validate_component(
        self,
        component: dict
    ) -> ValidationResult:

        # Rule 1: id must exist
        if "id" not in component:
            return ValidationResult(
                valid=False,
                reason="Component is missing id."
            )

        # Rule 2: type must exist
        if "type" not in component:
            return ValidationResult(
                valid=False,
                reason="Component is missing type."
            )

        component_type = component["type"]

        # Rule 3: root/supported component
        if component_type not in SUPPORTED_COMPONENTS:
            return ValidationResult(
                valid=False,
                reason=f"Unsupported component: {component_type}"
            )

        # Rule 4: parent components must have children
        if component_type in PARENT_COMPONENTS:

            if "children" not in component:
                return ValidationResult(
                    valid=False,
                    reason=f"{component_type} must contain children."
                )

            for child in component["children"]:

                result = self._validate_component(child)

                if not result.valid:
                    return result

        # Rule 5: leaf components cannot have children
        if component_type in LEAF_COMPONENTS:

            if "children" in component:
                return ValidationResult(
                    valid=False,
                    reason=f"{component_type} cannot contain children."
                )

        return ValidationResult(
            valid=True
        )