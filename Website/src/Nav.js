import { Label } from "./lib/label";
import "./Nav.css";

export default function Nav({ data }) {
    return (
        <nav>
            <h1>Foetal Health Predictor</h1>
            <div>
                <h2>Foetuses</h2>
                <ul>
                    {data.map(fetous => (
                        <li key={fetous.id}>
                            {
                                fetous.label !== Label.Loading ?
                                    <span class="material-symbols-outlined">person</span> :
                                    <span class="material-symbols-outlined spinner">progress_activity</span>
                            }

                            {fetous.id}
                            <span class="badge" style={{ backgroundColor: fetous.label.color }}>
                                {fetous.label.value}
                            </span>
                        </li>
                    ))}
                </ul>
            </div>
            <button>
                <span class="material-symbols-outlined">add</span> New
            </button>
        </nav>
    )
}