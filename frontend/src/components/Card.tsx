import Renderer from "./Renderer";

import type { CardComponent } from "../types/ui";

type CardProps = {
    component: CardComponent;

    onFormSubmit?: (formData: {
        amount: string;
        risk: string;
        horizon: string;
    }) => void;
};

export default function Card({
    component,
    onFormSubmit
}: CardProps) {

    return (

        <div>

            <h2>{component.title}</h2>

            {

                component.children.map((child) => (

                    <Renderer
                        key={child.id}
                        component={child}
                        onFormSubmit={onFormSubmit}
                    />

                ))

            }

        </div>

    );

}