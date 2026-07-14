import Renderer from "./Renderer";

import type { ContainerComponent } from "../types/ui";

type ContainerProps = {
    component: ContainerComponent;
};

export default function Container({ component }: ContainerProps) {

    return (

        <div>

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