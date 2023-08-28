const pointMap = {
  korean: 10,
  math: 10,
  english: 10,
  science: 10,
};

const salaryMap = {
  0: 0,
  100: 10000,
  200: 20000,
  300: 30000,
  400: 40000,
  500: 50000,
};

const spendingMap = {
  0: 0,
  100: 5,
  200: 10,
  300: 15,
  400: 20,
  500: 25,
};

const tree = document.getElementById("tree");
const pointsElem = document.getElementById("points");
const salaryElem = document.getElementById("salary");
const spendingElem = document.getElementById("spending");

function updatePoints(points) {
  pointsElem.textContent = `포인트: ${points}`;
  const level = Math.floor(points / 10);
  const imageUrl = `images/tree.jpeg`;
  tree.innerHTML = `<img src="${imageUrl}" alt="${level}">`;
  const expectedSalary = salaryMap[level];
  salaryElem.textContent = `예상연봉: $${expectedSalary}`;
  const spendingPerMeal = spendingMap[level];
  spendingElem.textContent = `한끼가격: $${spendingPerMeal}`;
}

const form = document.querySelector("form");
form.addEventListener("submit", function (event) {
  event.preventDefault();
  const subject = document.getElementById("subject").value;
  const points = pointMap[subject];
  updatePoints(points);
});
