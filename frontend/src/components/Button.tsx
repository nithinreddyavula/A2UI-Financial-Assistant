import type { ButtonComponent } from "../types/ui";

type ButtonProps = {
    component: ButtonComponent;
};

export default function Button({ component }: ButtonProps) {

    return (

        <button type="submit">

            {component.label}

        </button>

    );

}