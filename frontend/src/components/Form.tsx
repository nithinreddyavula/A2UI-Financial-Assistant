import Renderer from "./Renderer";

import type { FormComponent } from "../types/ui";

type FormProps = {
    component: FormComponent;
};

export default function Form({ component }: FormProps) {

    return (

        <form>

            <h3>{component.title}</h3>

            {

                component.children.map((child) => (

                    <Renderer
                        key={child.id}
                        component={child}
                    />

                ))

            }

        </form>

    );

}