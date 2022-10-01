var hamburger = document.querySelector(".hamburger");
hamburger.addEventListener("click", function(){
  document.querySelector("body").classList.toggle("active");
})


function validate() {
  console.log("Inside VAlidate");
  if (document.getElementById(arguments[0]).checked) {
      document.getElementById(arguments[1]).style.border = "border-left: 4px solid #72a604;";
  }  
  if (document.getElementById(arguments[0]).unchecked) {
    document.getElementById(arguments[1]).style.border = "border-left: 4px solid rgb(207, 27, 27); ";
  }
}