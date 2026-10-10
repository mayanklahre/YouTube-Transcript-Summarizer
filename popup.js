const btn = document.getElementById("summarise");
const output = document.getElementById("output");

function done(message) {
    output.textContent = message;
    btn.disabled = false;
    btn.textContent = "Summarise";
}

btn.addEventListener("click", () => {
    btn.disabled = true;
    btn.textContent = "Summarising...";
    output.textContent = "";
    chrome.tabs.query({ currentWindow: true, active: true }, (tabs) => {
        const url = tabs[0].url;
        fetch("http://127.0.0.1:5000/summary?url=" + encodeURIComponent(url))
            .then((res) => res.json().then((data) => ({ ok: res.ok, data })))
            .then(({ ok, data }) => done(ok ? data.summary : data.error))
            .catch(() => done("Could not reach the summarizer API. Is app.py running?"));
    });
});
