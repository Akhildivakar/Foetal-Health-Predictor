'use server';

import { Label } from "./label.js"

const labels = [Label.Normal, Label.Suspect, Label.Pathological];

export async function submit(formData) {
    const data = {
        baselineValue: parseFloat(formData.get("baselineValue")),
        accelerators: parseFloat(formData.get("accelerators")),
        fetalMovement: parseFloat(formData.get("fetalMovement")),
        uterineContractions: parseFloat(formData.get("uterineContractions")),
        lightDecelerations: parseFloat(formData.get("lightDecelerations")),
        severeDeclerations: parseFloat(formData.get("severeDeclerations")),
        prolongedDecelerations: parseFloat(formData.get("prolongedDecelerations")),
        abnormalShortTermVariability: parseFloat(formData.get("abnormalShortTermVariability")),
        meanValueOfShortTermVariability: parseFloat(formData.get("meanValueOfShortTermVariability")),
        percentageOfTimeWithAbnormalLongTermVariability: parseFloat(formData.get("percentageOfTimeWithAbnormalLongTermVariability")),
        meanValueOfLongTermVariability: parseFloat(formData.get("meanValueOfLongTermVariability")),
        histogramWidth: parseFloat(formData.get("histogramWidth")),
        histogramMin: parseFloat(formData.get("histogramMin")),
        histogramMax: parseFloat(formData.get("histogramMax")),
        histogramNumberOfPeaks: parseFloat(formData.get("histogramNumberOfPeaks")),
        histogramNumberOfZeros: parseFloat(formData.get("histogramNumberOfZeros")),
        histogramMode: parseFloat(formData.get("histogramMode")),
        histogramMean: parseFloat(formData.get("histogramMean")),
        histogramMedian: parseFloat(formData.get("histogramMedian")),
        histogramVariance: parseFloat(formData.get("histogramVariance")),
        histogramTendency: parseFloat(formData.get("histogramTendency"))
    };

    console.log(data);

    const response = await fetch(`http://localhost:8000/api/new`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    });

    const { normal, suspect, pathological } = await response.json();
    console.log(normal)
    const probabilities = [normal, suspect, pathological];
    console.log(probabilities);

    let highest = 0;
    for (let i = 0; i < 3; i++) {
        if (probabilities[i] > highest) {
            highest = probabilities[i]
        }
    }
    console.log(highest);

    const result = probabilities.indexOf(highest);
    console.log(result);
    
    const label = labels[result];
    console.log(label);

    return {
        label: label,
        probabilities: probabilities
    }
}