import Renderer from "./Renderer";

import type { ContainerComponent } from "../types/ui";

type ContainerProps = {
    component: ContainerComponent;

    onFormSubmit?: (formData: {
        amount: string;
        risk: string;
        horizon: string;
    }) => void;
};

export default function Container({
    component,
    onFormSubmit
}: ContainerProps) {

    return (

        <div>

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