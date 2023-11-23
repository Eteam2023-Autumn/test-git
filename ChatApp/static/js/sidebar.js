//HTML文書内の要素をjs変数へ定義
const list = document.querySelectorAll(".list");
const openBurgerButton = document.getElementById("burger-icon");
const closeBurgerButton = document.getElementById("burger-close-icon");
const menu = document.getElementById("mobile-header");

//各クリック時の動作を定義
list.forEach((item) => item.addEventListener("click", activateLink));
openBurgerButton.addEventListener("click", () => toggleMenu(true));
closeBurgerButton.addEventListener("click", () => toggleMenu(false));

//各要素に対応するリンクを呼び出す
function activateLink() {
  list.forEach((item) => item.classList.remove("active"));
  this.classList.add("active");
  console.log("リストアイテムがクリックされました。");
}

//togglemenu()と三項演算子を使用し、isOpenがtrueならメニューを開き、falseなら閉じる（モバイルサイズ用）
function toggleMenu(isOpen) {
  openBurgerButton.style.display = isOpen ? "none" : "block";
  closeBurgerButton.style.display = isOpen ? "block" : "none";
  menu.style.display = isOpen ? "flex" : "none";
  console.log(isOpen ? "リストが開かれました" : "リストが閉じられました");
}