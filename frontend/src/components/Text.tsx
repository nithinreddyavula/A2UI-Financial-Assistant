import type { TextComponent } from "../types/ui";
import "../styles/Text.css";

type TextProps = {
    component: TextComponent;
};

export default function Text({ component }: TextProps) {

    return (

        <p>

            {component.value}

        </p>

    );

}