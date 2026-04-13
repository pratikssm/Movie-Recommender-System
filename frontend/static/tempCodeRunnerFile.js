const ws = new WebSocket("ws://127.0.0.1:8000/ws");

ws.onopen = () => console.log("WebSocket connected!");
ws.onclose = (event) => console.log("WebSocket closed:", event.reason);
ws.onerror = (err) => console.error("WebSocket error:", err);

const recommendBtn = document.getElementById("recommendBtn");
const movieInput = document.getElementById("movieInput");
const resultsDiv = document.getElementById("results");
const loading = document.getElementById("loading");

recommendBtn.addEventListener("click", () => {
  if (ws.readyState !== WebSocket.OPEN) {
    alert("WebSocket not connected yet!");
    return;
  }

  const movieName = movieInput.value.trim();
  if (!movieName) {
    alert("Please enter a movie name!");
    return;
  }

  resultsDiv.innerHTML = "";
  loading.classList.remove("hidden");

  ws.send(JSON.stringify({ movie_name: movieName }));
});

ws.onmessage = (event) => {
  loading.classList.add("hidden");
  const data = JSON.parse(event.data);
  console.log("Received data:", data); // Log the full response for debugging

  if (data.error) {
    resultsDiv.innerHTML = `<p style="color: red;">Error: ${data.error}</p>`;
    return;
  }

  const recs = data.recommendations;
  if (!recs || recs.length === 0) {
    resultsDiv.innerHTML = `<p>No recommendations found.</p>`;
    return;
  }

  resultsDiv.innerHTML = `<h2>Recommended for: ${data.input_movie}</h2>`;

  recs.forEach((m) => {
    const badgeColor =
      m.classification?.toLowerCase() === "blockbuster"
        ? "blockbuster"
        : m.classification?.toLowerCase() === "hit"
        ? "hit"
        : "flop";

    // Fallback values for all fields
    const productionCompanies = m.production_companies || "N/A";
    const productionCountries = m.production_countries || "N/A";
    const releaseDate = m.release_date || "N/A";
    const revenue = m.revenue || "N/A";
    const spokenLanguages = m.spoken_languages || "N/A";
    const budget = m.budget || "N/A";
    const genres = m.genres || "N/A";

    resultsDiv.innerHTML += `
      <div class="card">
        <h3>${m.title || "Untitled"}</h3>
        <div class="details">
          <p>⭐ Average Rating: ${m.avg_rating || "N/A"}</p>
          <p>👍 Likes: ${m.likes_percent || "N/A"}%</p>
          <p>💰 Box Office: ${m.box_office || "N/A"}</p>
          <p>📈 Similarity: ${m.similarity || "N/A"}%</p>
          <p>🎯 Classification: <span class="badge ${badgeColor || ''}">${m.classification || "N/A"}</span></p>
          <p>🏭 Production Companies: ${productionCompanies}</p>
          <p>🌍 Production Countries: ${productionCountries}</p>
          <p>📅 Release Date: ${releaseDate}</p>
          <p>💵 Revenue: ${revenue}</p>
          <p>🗣️ Spoken Languages: ${spokenLanguages}</p>
          <p>💸 Budget: ${budget}</p>
          <p>🎬 Genres: ${genres}</p>
        </div>
      </div>
    `;
  });
};