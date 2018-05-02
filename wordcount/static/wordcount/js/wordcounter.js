//word counting on onchange

function wordCounter(content){
	//alert(content);
    var input = content.match(/\S+/g);
    var numOfWords = input ? input.length : 0
    var numOfCharacters = content.length;
    
    /*return {
        charactersNoSpaces : val.replace(/\s+/g, '').length,
        characters         : val.length,
        words              : wom ? wom.length : 0,
        lines              : val.split(/\r*\n/).length
    };*/
    $("#charcount").empty();
    var newcount = '<h1 class="card-text">' + numOfCharacters + '</h1>'
    $("#charcount").append(newcount);
}