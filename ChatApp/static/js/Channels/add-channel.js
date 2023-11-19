//モーダル表示と非表示、チャンネル登録処理について記載

// チャンネルを登録する時の処理
const addChannelModal = document.getElementById("add-channel-modal");
const addPageButtonClose = document.getElementById("add-page-close-button");
const addChannelConfirmButton = document.getElementById("add-channel-confirmation-button");

  // モーダル表示ボタンが押された時にモーダルを表示する
const addChannelButton = document.getElementById("add-channel-button");

addChannelButton.addEventListener("click", () => {
    addChannelModal.style.display = "flex";
});

// モーダル内の×ボタンが押された時にモーダルを非表示にする
addPageButtonClose.addEventListener("click",() => {
    addChannelModal.style.display = "none";
});

// 画面のどこかが押された時にモーダルを非表示にする
addEventListener("click", (e) => {
    if(e.target == addChannelModal){
        addChannelModal.style.display = "none";
    }
});