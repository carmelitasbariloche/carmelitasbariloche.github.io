
<script language="Javascript" >

var article={}
const catalog=[]
{% for article in catalog %}  
  catalog[{{loop.index}}]={title:"{{article.title}}",id:"{{article.id}}",parent:"{{article.parent}}",child:"{{article.child}}"}
{%endfor%}

// var current_parent = 'todos'

//shortens document.getEgetElementById
function element(id) {
return document.getElementById(id);
}
let allSearchData = ""; //decleared to collect all search names

//gets each inputs data starting from second input
function getResults_old(countid) {
//gets value of input
let search = element("search-input"+countid).value;
allSearchData = ""; //clears data for each word typed

hideSearchResults(countid);
clearSearchResults(countid);
clearSearchData(countid); //
//starts searching from the second input
if (search.length > 1) {
    let counter = 0; // counts to 10
    // ArticlesNames se define en el archivo article.title.js
    for (let x of ArticlesNames) {
    if (counter < 15) {
        //checks for similarities
        if (x.toLowerCase().includes(search.toLowerCase())) {
        console.log(current_parent)
        //populates the suggestion div
           // "<button onclick=\"showAll('b-parent','c-parent');return false;\"><a style='color:red;' href='#" 
        element("search-results"+countid).innerHTML +=
            "<input type=button onClick=\"showAll('b-parent','c-parent');location.href='#"
            + x + "'\" value='"+ x +"'>"
            // "' ><p style='padding-left:0.3em'>" +
            // x +
            // "</p></a></button>            ";

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
    displaySearchResults(countid);
}
}
//gets each inputs data starting from second input
function getResults(countid) {

//gets value of input
let search = element("search-input"+countid).value;
allSearchData = ""; //clears data for each word typed

hideSearchResults(countid);
clearSearchResults(countid);
clearSearchData(countid); //


// Strips diacritics from a string
// Example: removeDiacritics('ï') -> 'i'
const removeDiacritics = str => {
  return str
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '')
}

// Determines if a haystack contains a needle.  Case and accent insensitive.
// Example: normalizedContains('Le Samouraï', 'I') -> true
const normalizedContains = (haystack, needle) => {
  const regExp = new RegExp(removeDiacritics(needle), 'gi');
  return regExp.test(removeDiacritics(haystack));
}

//starts searching from the second input
if (search.length > 1) {
    let counter = 0; // counts to 10
    // ArticlesNames se define en el archivo article.title.js
    // for (let article of catalog) {
    let parent=current_parent.replace('id-','').replace('-content','')
    element("search-results"+countid).innerHTML ='<p> Esta buscando dentro de '+parent.toUpperCase()+':</p>'
    for(let i=1;i<catalog.length;i++){
        article=catalog[i];
        let x=article.id; //article.title
        let p=article.parent
        let id=article.id
        if (parent=='todos'){
            p=parent
        }
        if (counter < 25) {
            //checks for similarities
            // if (x.toLowerCase().includes(search.toLowerCase()) && p==parent) {
            if (normalizedContains(x,search) && p==parent) {
            //                 console.log(article) 
            // console.log(current_parent)
            //populates the suggestion div
               // "<button onclick=\"showAll('b-parent','c-parent');return false;\"><a style='color:red;' href='#" 
               // "<input type=button onClick=\"showAll('b-parent','c-parent');location.href='#"
            element("search-results"+countid).innerHTML +=
                "<input class='search-buttons' type=button onClick=\"showCarretById('id-"+article.parent+"');return location.href='#"
                + id + "';\" value='"+ x +"'>"
                // window.scrollBy(0, 550);
                // "' ><p style='padding-left:0.3em'>" +
                // x +
                // "</p></a></button>            ";

                // "<div class='search-item' style='color:red' onclick='displayData(\"" +
                // x +
                // "\")'><p>" +
                // x +
                // "</p></div>";

            counter++;
            }
        }
    if (x.toLowerCase().includes(search.toLowerCase()) && p==current_parent)
        //saves all the realated names
        allSearchData += "<p>" + x + "</p>";
    }
    displaySearchResults(countid);
}
}
//displays the suggestion div
function displaySearchResults(countid) {
element("search-results"+countid).style.display = "block";
}
//clears the suggestion div
function clearSearchResults(countid) {
element("search-results"+countid).innerHTML = "";
}

//hides the suggestion div
function hideSearchResults(countid) {
element("search-results"+countid).style.display = "none";
}
//displays names when you click a suggestions
function displayData(name,countid) {
element("search-data"+countid).innerHTML = "<p style='color:blue'>" + name + "</p>";
hideSearchResults(countid);
}
//displays all related names to your search when you hit enter
function displayAllData(names,countid) {
element("search-data"+countid).innerHTML = names;
hideSearchResults(countid);
}
//clears names displayed from search result
function clearSearchData(countid) {
element("search-data"+countid).innerHTML = "";
}
//gets results after each input
element("search-input1").oninput = function() {
getResults(1);
};
element("search-input2").oninput = function() {
getResults(2);
};

// element("search-input1").addEventListener("keyup", function(event) {
// // Number 13 is the "Enter" key on the keyboard
// if (event.keyCode === 13) {
//     // Cancel the default action, if needed
//     event.preventDefault();
//     // Trigger the button element with a click
//     displayAllData(allSearchData,1);
// }
// });


// element("search-input2").addEventListener("keyup", function(event) {
// // Number 13 is the "Enter" key on the keyboard
// if (event.keyCode === 13) {
//     // Cancel the default action, if needed
//     event.preventDefault();
//     // Trigger the button element with a click
//     displayAllData(allSearchData,2);
// }
// });


</script>