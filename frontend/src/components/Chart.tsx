import type { ChartComponent } from "../types/ui";

type ChartProps = {
    component: ChartComponent;
};

export default function Chart({ component }: ChartProps) {

    return (

        <div>

            <h3>{component.title}</h3>

            <p>

                {component.chartType} Chart

            </p>

        </div>

    );

}