import Renderer from "./Renderer";

import type { CardComponent } from "../types/ui";

type CardProps = {
    component: CardComponent;
};

export default function Card({ component }: CardProps) {

    return (

        <div>

            <h2>{component.title}</h2>

            {

                component.children.map((child) => (

                    <Renderer
                        key={child.id}
                        component={child}
                    />

                ))

            }

        </div>

    );

}