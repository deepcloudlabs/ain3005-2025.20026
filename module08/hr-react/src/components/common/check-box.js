export default function CheckBox({id, label, value, handleChange}) {
    return(
      <div className="mb-3">
          <label htmlFor={id} className={"form-label"}>{label}:
            <input type={"checkbox"}
                   id={id}
                   checked={value}
                   onChange={handleChange}
                   className="form-check-input"/>
          </label>
      </div>
    );
}