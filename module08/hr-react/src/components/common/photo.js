import React from "react";

export default function Photo({id, label, value, handleChange, readOnly=false}) {
    function handleFileChange(e) {
        const fileReader = new FileReader();
        const fileName = e.target.files[0];
        fileReader.onload = (e) => {
            handleChange(e.target.result);
        }
        fileReader.readAsDataURL(fileName);
    }
    if (readOnly) {
        return (
            <img style={{width: "64px", height:"64px"}} src={value} alt="Employee's photo" className={"img-thumbnail"} />
        );
    }
    return (
        <div className={"mb-3"}>
            <label className={"form-label"} htmlFor={id}>{label}:</label>
            <img src={value}
                 style={{width: "64px"}}
                 alt="Employee's photo"
                 className={"img-thumbnail"} />
            <label>
                <input type="file" onChange={handleFileChange} style={{"display":"none"}} />
                <span className={"btn btn-primary"}>File</span>
            </label>
        </div>
    );
}
