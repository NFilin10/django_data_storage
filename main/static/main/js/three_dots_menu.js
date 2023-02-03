document.addEventListener("click", function(event) {
    const menuIcons = document.querySelectorAll(".fa-solid.fa-ellipsis-vertical");
    menuIcons.forEach(menuIcon => {
        const menuId = menuIcon.getAttribute("id");
        if (event.target === menuIcon) {
            const dropdownMenu = document.getElementById(menuId.replace("menu-icon", "dropdown-menu"));
            if (dropdownMenu.style.display === "block") {
                dropdownMenu.style.display = "none";
            } else {
                dropdownMenu.style.display = "block";
            }
        } else {
            const dropdownMenu = document.getElementById(menuId.replace("menu-icon", "dropdown-menu"));
            if (dropdownMenu.style.display === "block") {
                dropdownMenu.style.display = "none";
            }
        }
    });
});