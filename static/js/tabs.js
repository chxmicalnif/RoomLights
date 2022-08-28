function changetab(evt, tname) {
  var i, tabcontent, tablink;

  // Hide all elements with class="tabcontent"
  tabcontent = document.getElementsByClassName("tabcontent");
  for(i=0; i< tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  //get elements with class="tablink" and remove the class "active"
  tablink = document.getElementsByClassName("tablink");
  for(i = 0 ; i < tablink.length; i++){
    tablink[i].className = tablink[i].className.replace(" active", "");
  }

  document.getElementById(tname).style.display = "block";
  evt.currentTarget.className += " active";
}

// Open first tab by default
document.getElementById("def").click();
