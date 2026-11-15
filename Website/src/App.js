import { useState } from 'react';

import './App.css';

import Nav from "./Nav.js"
import Main from './Main.js';
import { Label } from "./lib/label.js";


const testData = [
    { id: "PREG-2026-88412", label: Label.Normal },
    { id: "PREG-2026-90145", label: Label.Suspect },
    { id: "PREG-2026-11049", label: Label.Suspect },
    { id: "PREG-2026-11892", label: Label.Normal },
    { id: "PREG-2026-77316", label: Label.Pathological }
];

const newFetousID = "PREG-2026-49867";

export default function App() {
    const [data, setData] = useState(testData)

    function addFetous() {
        setData([{ id: newFetousID, label: Label.Loading }, ...testData]);
    }

    function updateFetous(label) {
        setData([{ id: newFetousID, label: label }, ...testData]);
    }

    return (
        <div className="App">
            <Nav data={data} />
            <Main addFetous={addFetous} updateFetous={updateFetous} />
        </div>
    );
}
