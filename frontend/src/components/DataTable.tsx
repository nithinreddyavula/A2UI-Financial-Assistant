import type { DataTableComponent } from "../types/ui";
import "../styles/DataTable.css";
type DataTableProps = {
    component: DataTableComponent;
};

export default function DataTable({ component }: DataTableProps) {

    return (

        <div className="table-container">

        <table border={1} cellPadding={8}>

            <thead>
                <tr>

                    {component.columns.map((column) => (

                        <th key={column}>
                            {column}
                        </th>

                    ))}

                </tr>
            </thead>

            <tbody>

                {component.rows.map((row, rowIndex) => (

                    <tr key={rowIndex}>

                        {row.map((cell, cellIndex) => (

                            <td key={cellIndex}>
                                {cell}
                            </td>

                        ))}

                    </tr>

                ))}

            </tbody>

        </table>

       </div>

    );

}