
interface BaseComponent {
    id: string;
    type: string;
}


export interface ContainerComponent extends BaseComponent {
    type: "container";
    children: UIComponent[];
}


export interface CardComponent extends BaseComponent {
    type: "card";
    title: string;
    children: UIComponent[];
}


export interface TextComponent extends BaseComponent {
    type: "text";
    value: string;
}


export interface DataTableComponent extends BaseComponent {
    type: "dataTable";
    columns: string[];
    rows: string[][];
}


export interface FormComponent extends BaseComponent {
    type: "form";
    title: string;
    children: UIComponent[];
}


export interface TextFieldComponent extends BaseComponent {
    type: "textField";
    label: string;
    name: string;
    placeholder: string;
}


export interface ButtonComponent extends BaseComponent {
    type: "button";
    label: string;
    action: string;
}


export interface BadgeComponent extends BaseComponent {
    type: "badge";
    label: string;
}


export interface ChartComponent extends BaseComponent {
    type: "chart";
    chartType: string;
    title: string;
    data: unknown[];
}

export type UIComponent =
    | ContainerComponent
    | CardComponent
    | TextComponent
    | DataTableComponent
    | FormComponent
    | TextFieldComponent
    | ButtonComponent
    | BadgeComponent
    | ChartComponent;