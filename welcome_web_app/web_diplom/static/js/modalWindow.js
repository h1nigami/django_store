let buttonModal = document.getElementById("buttonSetReviews");
let modalWindow = document.getElementById("modalWindow");
let modalClose = document.getElementById("modalClose");
let modalContent = document.getElementById("modalContent");

buttonModal.onclick = () => {
    modalWindow.style.visibility = 'visible';
    modalWindow.style.opacity = '1';
    modalWindow.style.transform = 'translateY(0)';
}

modalClose.onclick = () => {
    modalWindow.style.opacity = '0';
    modalWindow.style.visibility = 'hidden';
    modalWindow.style.transform = 'translateY(-50%)';
}

window.addEventListener('click', (event) => {
    if (event.target == modalWindow) {
        modalWindow.style.opacity = '0';
        modalWindow.style.visibility = 'hidden';
        modalWindow.style.transform = 'translateY(-50%)';
    }
})