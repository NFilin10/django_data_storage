let popup = document.getElementById('pops'),
popupToggle = document.getElementById('myBtn'),
popupClose = document.querySelector('.close');


popupToggle.onclick = function () {
    popup.style.display="block"
    const blur_items = document.querySelectorAll('.blur')
    blur_items.forEach(function (blur_item) {
        blur_item.style.filter = "blur(8px)"
    })
}

popupClose.onclick = function () {
    popup.style.display="none"
    const blur_items = document.querySelectorAll('.blur')
    blur_items.forEach(function (blur_item){
        blur_item.style.filter = "blur(0px)"
    })
}

window.onclick = function(event) {
    if (event.target == popup) {
        event.target.style.display = "none";
         const blur_items = document.querySelectorAll('.blur')
        blur_items.forEach(function (blur_item){
            blur_item.style.filter = "blur(0px)"
        })
    }
}


