import type { TextFieldComponent } from "../types/ui";

type TextFieldProps = {
    component: TextFieldComponent;
};

export default function TextField({ component }: TextFieldProps) {

    return (

        <div>

            <label>

                {component.label}

            </label>

            <br />

            <input
                type="text"
                name={component.name}
                placeholder={component.placeholder}
            />

        </div>

    );

}