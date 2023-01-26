let popup = document.getElementById('file-popup'),
popupToggle = document.getElementById('myBtn'),
popupClose = document.querySelector('.close');

function a() {
    var e = document.getElementById("floatingSelect");
    var text = e.options[e.selectedIndex].text;
    if (text === "Document"){
        document.getElementById('myField').value = "f";
        popup.style.display="block"
        const blur_items = document.querySelectorAll('.blur')
        blur_items.forEach(function (blur_item) {
            blur_item.style.filter = "blur(8px)"
        })


    }

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


