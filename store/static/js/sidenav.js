var sidebarOpen = false // Cerrado
function toggleNav(){
    if(sidebarOpen === false){
    	sidebarOpen = true;
    	openNav();
    }
    else{
    	sidebarOpen = false;
    	closeNav();
    }
}
/* Set the width of the side navigation to 250px */
function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
}

/* Set the width of the side navigation to 0 */
function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
}