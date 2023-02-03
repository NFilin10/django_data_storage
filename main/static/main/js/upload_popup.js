// let popup = document.getElementById('file-popup'),
// popupToggle = document.getElementById('myBtn'),


function a() {
    var e = document.getElementById("floatingSelect");
    var text = e.options[e.selectedIndex].text;
    var text_id = e.options[e.selectedIndex].id;
    console.log(text)
    console.log(text_id)

    if (text_id === "photo" || text_id === "document") {
        search_id = "file-popup"
        close_id = "doc-close"
    } else if (text_id === "link" || text_id === "note") {
        search_id = "note-popup"
        close_id = "note-close"
    }

    console.log(search_id)
    let popup = document.getElementById(search_id)


    document.getElementById('myField').value = text;
    document.getElementById('myField1').value = text;
    popup.style.display = "block"
    const blur_items = document.querySelectorAll('.blur')
    blur_items.forEach(function (blur_item) {
        blur_item.style.filter = "blur(8px)"
    })

    popupClose = document.getElementById(close_id);

    popupClose.onclick = function () {
        console.log("clicked")
        popup.style.display = "none"
        const blur_items = document.querySelectorAll('.blur')
        blur_items.forEach(function (blur_item) {
            blur_item.style.filter = "blur(0px)"
        })
    }


    window.onclick = function(event) {
        if (event.target == popup) {
            event.target.style.display = "none";
            const blur_items = document.querySelectorAll('.blur')
            blur_items.forEach(function (blur_item) {
                blur_item.style.filter = "blur(0px)"
            })
        }
    }

}
