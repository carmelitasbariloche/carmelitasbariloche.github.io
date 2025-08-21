
<script language="Javascript" >

function myclass(id) {
return document.getElementsByClassName(id);
}

//shortens document.getEgetElementById
function element(id) {
return document.getElementById(id);
}
let allSearchData = ""; //decleared to collect all search names

//gets each inputs data starting from second input
function getResults(id) {
//gets value of input
// let search = element("search-input").value;
let search = element(id).value;
allSearchData = ""; //clears data for each word typed

hideSearchResults();
clearSearchResults();
clearSearchData(); //
//starts searching from the second input
if (search.length > 1) {
    let counter = 0; // counts to 10
    for (let x of names) {
    if (counter < 10) {
        //checks for similarities
        if (x.toLowerCase().includes(search.toLowerCase())) {
        //populates the suggestion div
        var myresult=myclass('search-results');
        for(var i = 0; i < myresult.length; i++) {
            myresult[i].innerHTML +=
            "<a style='color:red' href='#" +
            x +
            "'><p>" +
            x +
            "</p></a>";
        }
            // "<div class='search-item' style='color:red' onclick='displayData(\"" +
            // x +
            // "\")'><p>" +
            // x +
            // "</p></div>";

        counter++;
        }
    }
    if (x.toLowerCase().includes(search.toLowerCase()))
        //saves all the realated names
        allSearchData += "<p>" + x + "</p>";
    }
    displaySearchResults();
}
}
//displays the suggestion div
function displaySearchResults() {
            var myresult=myclass('search-results');
        for(var i = 0; i < myresult.length; i++) {
            myresult[i].style.display = "block";
        }
}
//clears the suggestion div
function clearSearchResults() {
        var myresult=myclass('search-results');
        for(var i = 0; i < myresult.length; i++) {
            myresult[i].innerHTML = "";
        }
}

//hides the suggestion div
function hideSearchResults() {
        var myresult=myclass('search-results');
        for(var i = 0; i < myresult.length; i++) {
            myresult[i].style.display = "none";
        }
}
//displays names when you click a suggestions
function displayData(name) {
        var myresult=myclass('search-data');
        for(var i = 0; i < myresult.length; i++) {
            myresult[i].innerHTML = "<p style='color:blue'>" + name + "</p>";
        }
hideSearchResults();
}
//displays all related names to your search when you hit enter
function displayAllData(names) {
        var myresult=myclass('search-data');
        for(var i = 0; i < myresult.length; i++) {
            myresult[i].innerHTML = names;
        }
hideSearchResults();
}
//clears names displayed from search result
function clearSearchData() {
        var myresult=myclass('search-data');
        for(var i = 0; i < myresult.length; i++) {
            myresult[i].innerHTML = "";
        }
}
//gets results after each input
// element("search-input").oninput = function() {
// getResults();
// };

// element("search-input").addEventListener("keyup", function(event) {
// // Number 13 is the "Enter" key on the keyboard
// if (event.keyCode === 13) {
//     // Cancel the default action, if needed
//     event.preventDefault();
//     // Trigger the button element with a click
//     displayAllData(allSearchData);
// }
// });

var SearchInput = document.getElementsByClassName('search-input');

for(var i = 0; i < SearchInput.length; i++) {
  (function(index) {
    SearchInput[index].oninput=(function(ii){
        var aux='search-input'+ii
        console.log(aux)
        getResults('search-input'+ii)
    })(index)


    SearchInput[index].addEventListener("keyup", function(event) {
    // Number 13 is the "Enter" key on the keyboard
    if (event.keyCode === 13) {
    // Cancel the default action, if needed
    event.preventDefault();
    // Trigger the button element with a click
    displayAllData(allSearchData);
    }
    });
  })(i);
}


</script>