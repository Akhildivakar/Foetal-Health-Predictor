import "./Input.css"

export default function Input({ id, label }) {
    return (
        <label for={id}>
            {label}:
            <input id={id} name={id} type="number" min="0" step="any" required={true} defaultValue={1}/>
        </label>
    );
}