import type { UIComponent } from "../types/ui";

import Container from "./Container";
import Card from "./Card";
import Text from "./Text";
import DataTable from "./DataTable";


type RendererProps = {
    component: UIComponent;
};

export default function Renderer({ component }: RendererProps) {

    switch (component.type) {

        case "container":
            return <Container component={component} />;

        case "card":
            return <Card component={component} />;

        case "text":
            return <Text component={component} />;

        case "dataTable":
            return <DataTable component={component} />;

        default:
            return (
                <div>
                    Unsupported Component
                </div>
            );
    }

}