// // もしチャンネル作成者uidと自分のuidが同じだった場合は削除ボタンを追加
// if (uid === channel.uid) {
//     const deleteButton = document.createElement("button");
//     deleteButton.innerHTML =
//         '<img id="delete-button" src="/static/img/close-icon.png">';
//     deleteButton.classList.add("delete-button");
//     li.appendChild(deleteButton);
//     // ゴミ箱ボタンが押された時にdeleteモーダルを表示させる
//     deleteButton.addEventListener("click", () => {
//         deleteChannelModal.style.display = "flex";
//         const confirmationButtonLink = document.getElementById(
//             "delete-confirmation-link"
//         );
//         // aタグにhrefを追加
//         const channelURL = `/delete/${channel.id}`;
//         confirmationButtonLink.setAttribute("href", channelURL);
//     });
// }