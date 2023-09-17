    const happinessBar = document.getElementById("happiness_bar");
    const happinessPoints = document.getElementById("happiness_points");
    const smiley = document.getElementById("smiley");
    const checkboxes = document.querySelectorAll('input[type="checkbox"]');
    let happiness = 0;

    function updateHappiness(checkbox) {
       if (checkbox.checked) {
           happiness += 10; // Increase happiness when a checkbox is checked
       } else {
           happiness -= 10; // Decrease happiness when a checkbox is unchecked
       }

       if (happiness < 0) {
           happiness = 0; // Ensure happiness doesn't go below 0
       }

       // Update the happiness bar, count, and smiley face
       updateHappinessUI();
    

    function updateHappinessUI() {
       happinessPoints.textContent = happiness;
       happinessBar.style.width = happiness + "%";

       // Update the smiley face based on happiness level
       if (happiness >= 50) {
           smiley.textContent = "😄";
       } else if (happiness >= 40) {
           smiley.textContent = "😊"
       } else if (happiness >= 30) {
           smiley.textContent = "☺️"
       } else if (happiness >= 20) {
           smiley.textContent = "🙂"
       } else if (happiness >= 10) {
           smiley.textContent = "😐";
       } else {
           smiley.textContent = "😢";
       }
    

    function goToEnterMedPage() {
       window.location.href = "/EnterMedication";
    
    
    function removeSelectedMedications(){
       const removeButtons = document.querySelectorAll(".remove-button-medication")

       removeButtons.forEach( button => {
           button.addEventListener("click", () => {
               const checkboxes = document.querySelectorAll('input[type = "checkbox"]:checked');

               checkboxes.forEach(checkbox => {
                   const label = checkbox.nextElementSibling;
                   label.remove();
                   checkbox.remove();
               });


           });  
       });

       hapiness = 0;
       updateHappinessUI();
    

    function goToMainPage() {
       window.location.href = "/MainPage";
    



