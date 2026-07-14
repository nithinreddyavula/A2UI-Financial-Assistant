import { useState } from "react";
import Renderer from "./Renderer";
import TextField from "./TextField";
import Button from "./Button";
import "../styles/Form.css";
import type { FormComponent } from "../types/ui";

type FormProps = {
    component: FormComponent;

    onSubmit?: (formData: {
        amount: string;
        risk: string;
        horizon: string;
    }) => void;
};

export default function Form({
    component,
    onSubmit
}: FormProps) {

    const [formData, setFormData] = useState({
        amount: "",
        risk: "",
        horizon: ""
    });

    function handleSubmit(
        e: React.FormEvent<HTMLFormElement>
    ) {

        e.preventDefault();

        console.log("Form Submitted");
        console.log(formData);

        onSubmit?.(formData);

    }

    return (

        <form className="form" onSubmit={handleSubmit}>

            <h3>{component.title}</h3>

            {

                component.children.map((child) => {

                    if (child.type === "textField") {

                        return (

                            <TextField
                                key={child.id}
                                component={child}
                                value={formData[child.name as keyof typeof formData]}
                                onChange={(value) =>

                                    setFormData({
                                        ...formData,
                                        [child.name]: value
                                    })

                                }
                            />

                        );

                    }

                    if (child.type === "button") {

                        return (

                            <Button
                                key={child.id}
                                component={child}
                            />

                        );

                    }

                    return null;

                })

            }

        </form>

    );

}