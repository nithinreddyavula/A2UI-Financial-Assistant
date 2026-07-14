import type { UIComponent } from "../types/ui";

import Container from "./Container";
import Card from "./Card";
import Text from "./Text";
import DataTable from "./DataTable";
import Form from "./Form";
import TextField from "./TextField";
import Button from "./Button";
import Badge from "./Badge";
import Chart from "./Chart";


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

        case "form":
            return <Form component={component} />;

        case "textField":
            return <TextField component={component} />;

        case "button":
            return <Button component={component} />;

        case "badge":
            return <Badge component={component} />;

        case "chart":
            return <Chart component={component} />;

        default:
            return (
                <div>
                    Unsupported Component
                </div>
            );
    }

}