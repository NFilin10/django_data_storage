
//Autor: Nikita Filin, mõned ideed olid võetud: https://www.w3schools.com/howto/howto_js_popup.asp

var popupsToggle = document.querySelectorAll('.folder-wrapper'), popupClose = document.querySelectorAll('.close');
var xmarks = document.querySelectorAll('.fa-xmark');

popupsToggle.forEach(function(item) {
  item.addEventListener("click", function(e) {
    var popupName = item.getAttribute('data-popup');
    document.getElementById(popupName).style.display = "block";
    const blur_items = document.querySelectorAll('.blur');
    blur_items.forEach(function(blur_item) {
      blur_item.style.filter = "blur(8px)";
    });
  });
});

xmarks.forEach(function(xmark) {
  xmark.addEventListener("click", function(e) {
    e.stopPropagation();
  });
});



//Funktsioon paneb kinni popupi ja muudab tausta tagasi tavaliseks
popupClose.forEach(function(item){
    item.addEventListener("click", function () {
        var popup = item.closest('.modal')
        popup.style.display = "none"
        const blur_items = document.querySelectorAll('.blur')
        blur_items.forEach(function (blur_item){
            blur_item.style.filter = "blur(0px)"
        })
    })
})

//Funktsioon paneb popupi kinni, siis kui kasutaja vajutab ekraanile popupi väljaspoolt
window.onclick = function(event) {
    if (event.target.classList.contains('modal')) {
        event.target.style.display = "none";
        const blur_items = document.querySelectorAll('.blur')
        blur_items.forEach(function (blur_item){
            blur_item.style.filter = "blur(0px)"
        })
    }
}

//Funktsioon paneb popupi kinni, siis kui kasutaja vajutab ekraanile popupi väljaspoolt (telefonide jaoks)
window.addEventListener('touchstart', function(event) {
    if (event.target.classList.contains('modal')) {
        event.target.style.display = "none";
        const blur_items = document.querySelectorAll('.blur')
        blur_items.forEach(function (blur_item){
            blur_item.style.filter = "blur(0px)"
        })
    }
})


