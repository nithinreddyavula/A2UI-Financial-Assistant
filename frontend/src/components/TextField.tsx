import "../styles/TextField.css";

import type { TextFieldComponent } from "../types/ui";

type TextFieldProps = {
    component: TextFieldComponent;
    value?: string;
    onChange?: (value: string) => void;
};

export default function TextField({

    component,

    value,

    onChange

}: TextFieldProps) {

    return (

        <div className="text-field">

            <label>

                {component.label}

            </label>

            <input

                className="text-input"

                type="text"

                value={value}

                placeholder={component.placeholder}

                onChange={(e)=>

                    onChange?.(e.target.value)

                }

            />

        </div>

    );

}