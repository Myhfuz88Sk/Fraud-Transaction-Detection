async function submitForm() {
    const data = {
        TX_AMOUNT: parseFloat(document.getElementById("amount").value),
        TX_HOUR: parseInt(document.getElementById("hour").value),
        TX_DAY: parseInt(document.getElementById("day").value),
        TX_MONTH: parseInt(document.getElementById("month").value)
    };

    const response = await fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    });

    const result = await response.json();
    document.getElementById("result").innerText =
        result.fraud === 1 ? "⚠️ Fraudulent Transaction Detected!" : "✅ Transaction Seems Legitimate.";
}
