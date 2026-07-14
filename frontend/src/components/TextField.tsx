import type { TextFieldComponent } from "../types/ui";

type TextFieldProps = {
    component: TextFieldComponent;
    value: string;
    onChange: (value: string) => void;
};

export default function TextField({
    component,
    value,
    onChange
}: TextFieldProps) {

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
                value={value}
                onChange={(e) => onChange(e.target.value)}
            />

        </div>

    );

}