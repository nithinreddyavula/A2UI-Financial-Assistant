import type { BadgeComponent } from "../types/ui";

type BadgeProps = {
    component: BadgeComponent;
};

export default function Badge({ component }: BadgeProps) {

    return (

        <span>

            {component.label}

        </span>

    );

}