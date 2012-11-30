
// first page is the Title,
// we do not want a page number for that
var page_counter = 0;


slideList = document.getElementsByTagName('h1');
for (element in slideList) {
    //slide.childNodes[0].lastChild.nodeValue = "oh";
    //h1List = slide.getElementsByTagName('h1');
    //for (h1 in h1List) {
    //    //h1.nodeValue = "Hihi";
    //}
    var cssString = 'color:lime;font-weight:bold;';
    if( typeof(element.style.cssText) == 'string' ) {
        element.style.cssText = cssString;
    }
    element.setAttribute('style',cssString);
    page_counter = page_counter + 1;
}

window.alert(page_counter)

    //document.getElementById("impress").addEventListener( "impress:stepenter", function (event) {
    //
    //    var step = event.target;
    //
    //    // here you have access to a step element
    //    // unfortunately you will have to count yourself to find a number of this step
    //    // and display it somewhere
    //    //elem = document.getElem(page_counter);
    //    page_counter++;
    //    //step.value = page_counter;
    //
    //
    //}, false);
