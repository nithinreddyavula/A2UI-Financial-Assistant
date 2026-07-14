import type { BadgeComponent } from "../types/ui";
import "../styles/Badge.css";

type BadgeProps = {
    component: BadgeComponent;
};

export default function Badge({ component }: BadgeProps) {

    return (

        <span className="badge">

            {component.label}

        </span>

    );

}