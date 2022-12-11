button = document.getElementById("button");
textarea = document.getElementById("textarea");
embed = document.getElementById("embed");

async function getDataFromAPI(data = "hello") {
  const d = await axios.get(`http://127.0.0.1:8000/check/${textarea.value}`);

  textarea.value = "";
  embed.childNodes = [];
  const text = d["data"]["isSpam"] ? "Spam" : "Not Spam";
  const n = document.createElement("h1");
  n.innerText = text;
  embed.childNodes = [];
  embed.appendChild(n);
}

checkSpam = (e) => {
  e.preventDefault();
  getDataFromAPI();
};

button.addEventListener("click", checkSpam);
