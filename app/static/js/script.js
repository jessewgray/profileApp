$( document ).ready(function() {
    console.log( "ready!" );

    var theUrl = "./userjson"

    $.ajax({
    	url: theUrl,
    	type: 'GET',
    	dataType: 'json',
    	success: function(res){
    		console.log(res);

    		var arrayLength = res.length;

    		for(i = 0; i < arrayLength; i++){
    			var user = {
    				"firstName": res[i].fName,
    				"lastName": res[i].lName,
    				"picture": res[i].picture
    			}
    			picPath = "/static/uploads/" + user.picture
    			$("#thePeople").append(`<div><img class="headShots" src="${picPath}"><p>${user.firstName}</p><p>${user.lastName}</p></div>`)
    		}

    	} 
    });

});