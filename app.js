const rows = document.querySelectorAll(".showrow");

for (let i = 0; i < rows.length; i++) {
  const date = rows[i].children[0].innerText;
  const day = rows[i].children[1].innerText;
  const holiday = rows[i].children[2].querySelector("a").innerText;
  const holiday_type = rows[i].children[3].innerText;
  console.log(date + " " + day + " " + holiday + " " + holiday_type);

  const ul = document.querySelector("#list");
  const li = document.createElement("li");
  li.innerHTML = `${i + 1}:  ${date} - ${day} - ${holiday} - ${holiday_type}`;
  ul.append(li);
}
