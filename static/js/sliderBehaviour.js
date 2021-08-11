var redslider = document.getElementById("redSlider");
var redval = document.getElementById("redVal");

var greenslider = document.getElementById("greenSlider");
var greenval = document.getElementById("greenVal");

var blueslider = document.getElementById("blueSlider");
var blueval = document.getElementById("blueVal");

redval.innerHTML = redslider.value;
greenval.innerHTML = greenslider.value;
blueval.innerHTML = blueslider.value;

redslider.oninput = function(){
  redval.innerHTML = this.value;
}

greenslider.oninput = function(){
  greenval.innerHTML = this.value;
}

blueslider.oninput = function(){
  blueval.innerHTML= this.value
}
