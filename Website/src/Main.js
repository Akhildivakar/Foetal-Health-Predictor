
import { useState } from "react";

import Input from "./Input.js";
import { submit } from "./lib/form.js";
import { Label } from "./lib/label.js";

import "./Main.css";

const labels = [Label.Normal, Label.Suspect, Label.Pathological];

export default function Main({ addFetous, updateFetous }) {
    const [loading, setLoading] = useState(false);
    const [label, setLabel] = useState(null);
    const [probabilities, setProbabilities] = useState([]);

    async function handleSubmit(e) {
        setLoading(true);
        e.preventDefault();
        const form = e.target;
        const formData = new FormData(form);

        try {
            addFetous();

            setLabel(null);
            setProbabilities([]);

            const { label, probabilities } = await submit(formData);

            setLabel(label);
            setProbabilities(probabilities);

            updateFetous(label);

        } catch (error) {
            console.error("Submission failed:", error);

        } finally {
            setLoading(false);
        }
    }

    return (
        <main>
            <header>
                <h1>Enter CGT results</h1>
            </header>

            <form onSubmit={handleSubmit}>
                    <div className="inputGrid">
                        <Input id="baselineValue" label="Baseline Value" />
                        <Input id="accelerators" label="Accelerators" />
                        <Input id="fetalMovement" label="Fetal Movement" />
                        <Input id="uterineContractions" label="Uterine Contractions" />
                        <Input id="lightDecelerations" label="Light Decelerations" />
                        <Input id="severeDeclerations" label="Severe Decelerations" />
                        <Input id="prolonguedDecelerations" label="Prolongued Decelerations" />
                        <Input id="abnormalShortTermVariability" label="Abnormal Short Term Variability" />
                        <Input id="meanValueOfShortTermVariability" label="Mean Value Of Short Term Variability" />
                        <Input id="percentageOfTimeWithAbnormalLongTermVariability" label="Percentage Of Time With Abnormal Long Term Variability" />
                        <Input id="meanValueOfLongTermVariability" label="Mean Value Of Long Term Variability" />
                        <Input id="histogramWidth" label="Histogram Width" />
                        <Input id="histogramMin" label="Histogram Min" />
                        <Input id="histogramMax" label="Histogram Max" />
                        <Input id="histogramNumberOfPeaks" label="Histogram Number Of Peaks" />
                        <Input id="histogramNumberOfZeros" label="Histogram Number Of Zeros" />
                        <Input id="histogramMode" label="Histogram Mode" />
                        <Input id="histogramMean" label="Histogram Mean" />
                        <Input id="histogramMedian" label="Histogram Median" />
                        <Input id="histogramVariance" label="Histogram Variance" />
                        <Input id="histogramTendency" label="Histogram Tendency" />

                        <div></div>
                        <div></div>

                        <button type="submit" disabled={loading}>
                            {loading ? "Processing..." : "Submit"}
                        </button>
                    </div>
                </form>

                <h2 style={{ textAlign: "left" }}>Results:</h2>

                <div class="results">
                {probabilities.map((prob, i) => (
                    <>
                        <span className="badge" style={{ backgroundColor: labels[i].color}}>
                            {labels[i].value}
                        </span>

                        <progress style={{accentColor: labels[i].color}} id="file" value="32" max="100"> 32% </progress>
                    </>
                ))}
                </div>
        </main>
    );
}
