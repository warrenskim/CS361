
/* ---------- State dropdowns checks and alert ---------- */
var select1 = document.getElementById("dropdown1");
var select2 = document.getElementById("dropdown2");

select1.addEventListener("change", () => {
    submitBtn();
    sameSelection();
});
select2.addEventListener("change", () => {
    submitBtn();
    sameSelection();
});

function submitBtn(event) {
    if((select1.selectedIndex != 0 && select2.selectedIndex != 0) && (select1.selectedIndex != select2.selectedIndex)) {
        document.getElementById("submit-btn").disabled = false;
    }    
    else {
        document.getElementById("submit-btn").disabled = true;
    }
}

function sameSelection(event) {
    if((select1.selectedIndex != 0 && select2.selectedIndex != 0) && (select1.selectedIndex == select2.selectedIndex)) {
        alert("You must select two different states!")
    }
}
