async function generateMonster() {

    const prompt = document.getElementById("prompt").value;

    const response = await fetch("http://127.0.0.1:8000/generate-monster", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: prompt })
    });

    const data = await response.json();

    console.log(data); // 👈 ADD THIS

    document.getElementById("monster").innerHTML = `
        <h2>${data.title}</h2>
        <img src="${data.image}" width="256">
        <p>${data.lore}</p>
        <p>Intensity: ${data.stats.intensity}</p>
        <p>Stealth: ${data.stats.stealth}</p>
        <p>Rift Affinity: ${data.stats.rift_affinity}</p>
    `;
}