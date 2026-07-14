import "../styles/Chart.css";

import type { ChartComponent } from "../types/ui";

type Props = {
    component: ChartComponent;
};

export default function Chart({ component }: Props){

    return(

        <div className="chart">

            📊 {component.title}

            <p>

                ({component.chartType} Chart)

            </p>

        </div>

    );

}