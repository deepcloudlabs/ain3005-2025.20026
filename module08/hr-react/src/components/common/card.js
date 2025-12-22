import React from "react";

export default function Card({title, children}){
    return (
        <div className="card">
            <div className="card-header">
                <h4><span className="card-title">{title}</span></h4>
            </div>
            <div className="card-body">
                {children}
            </div>
        </div>
    );
}