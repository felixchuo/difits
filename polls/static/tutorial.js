$(function() {
// AJAX for posting
function create_post(tutorialNo) {
	console.log("create post is working!") // sanity check
	
    var map3 = {
                    // take away all the empty space from the input using .replace(/s+/g, '')
                    skill_id:  $('#skill_id').val(),
                    studentId: $('#student_id').val(),
                    total_ani: $('#total_ani').val(),
                    tutorialNo: tutorialNo,

    };
    console.log(map3);
    console.log(JSON.stringify(map3));
    console.log(skill_id);
    console.log(total_ani);
    $.ajax({
        url  : "/get_tutorial", // the endpoint
        type : "POST", // http method
        data : {get_tutorial:JSON.stringify(map3)}, // data sent with the post request
        
           
            success: function (json) {
                console.log (json);
                $('#displayAni').append('get_tutorial');
                //use <br/> to make a new line in the display
                $('#displayAni').empty();  //remove the previous content

                $('#displayAni').prepend("<b>You are watching video on </b>"+json.tutName+"<br>");
                
                $('#displayAni').append('<video width="650" height="400" controls="controls" autoplay="autoplay" type="video/mp4" class="resize" src="/static/tutorial/'+json.tutorial_file+'">');

                var video = document.getElementsByTagName('video')[0];

                video.onended = function(e) {
                    console.log("Video finished playing");
                    console.log(tutorialNo);
                    ani_no = document.getElementById("total_ani").value;
                    console.log(total_ani);

                    var map_tutorial = {
                        skill_id:  $('#skill_id').val(),
                        studentId: $('#student_id').val(),
                        total_ani: $('#total_ani').val(),
                        tutorialNo : tutorialNo, 
                    };
                    console.log ("able to try update");
                    $.ajax({
                        url  : "/update_tutorial_progress",
                        type : "POST",
                        data : {update_tutorial_progress:JSON.stringify(map_tutorial)},

                            success: function (json) {
                                console.log (json);
                                $('#gettutorialbutton'+json.tutorialNo).prop('disabled', false);
                                if (json.tutorialNo > json.total_ani){
                                    alert ("Congratulations!  You have completed the tutorial successfully.  \n  Proceed to the progress report to continue to the next section.");
                                    window.location.href = "/details/";
                                }
                            },
                            error : function (xhr, errmsg, err) {
                                console.log(xhr.status + ":" +xhr.responseText);
                            }
                    });
                }
            },    
            error : function (xhr, errmsg, err) {
                console.log(xhr.status + ":" +xhr.responseText);
                }  
            
    });
};


function show_button() {
    console.log("show button is working")
    tutorialItem = document.getElementById("tutorialNo").value;
    if (document.getElementById("total_ani").value == 6){
            document.getElementById("get_tutorial_button").style.display="none";
            document.getElementById("gettutorialbutton1").style.display="block";
            // $('#gettutorialbutton1').prop('disabled', false);
            document.getElementById("gettutorialbutton2").style.display="block";
            document.getElementById("gettutorialbutton3").style.display="block";
            document.getElementById("gettutorialbutton4").style.display="block";
            document.getElementById("gettutorialbutton5").style.display="block";
            document.getElementById("gettutorialbutton6").style.display="block";
    } else if (document.getElementById("total_ani").value == 5){
            document.getElementById("get_tutorial_button").style.display="none";
            document.getElementById("gettutorialbutton1").style.display="block";
            // $('#gettutorialbutton1').prop('disabled', false);
            document.getElementById("gettutorialbutton2").style.display="block";
            document.getElementById("gettutorialbutton3").style.display="block";
            document.getElementById("gettutorialbutton4").style.display="block";
            document.getElementById("gettutorialbutton5").style.display="block";
    } else if (document.getElementById("total_ani").value == 4){
            document.getElementById("get_tutorial_button").style.display="none";
            document.getElementById("gettutorialbutton1").style.display="block";
            // $('#gettutorialbutton1').prop('disabled', false);
            document.getElementById("gettutorialbutton2").style.display="block";
            document.getElementById("gettutorialbutton3").style.display="block";
            document.getElementById("gettutorialbutton4").style.display="block";
    } else if (document.getElementById("total_ani").value == 3){
            document.getElementById("get_tutorial_button").style.display="none";
            document.getElementById("gettutorialbutton1").style.display="block";
            // $('#gettutorialbutton1').prop('disabled', false);
            document.getElementById("gettutorialbutton2").style.display="block";
            document.getElementById("gettutorialbutton3").style.display="block";
    } else if (document.getElementById("total_ani").value == 2){
            document.getElementById("get_tutorial_button").style.display="none";
            document.getElementById("gettutorialbutton1").style.display="block";
            // $('#gettutorialbutton1').prop('disabled', false);
            document.getElementById("gettutorialbutton2").style.display="block";
    } else {
            document.getElementById("get_tutorial_button").style.display="none";
            document.getElementById("gettutorialbutton1").style.display="block";
            // $('#gettutorialbutton1').prop('disabled', false);
    }

    // """activate the button"""
    if (tutorialItem ==6){
        $('#gettutorialbutton1').prop('disabled', false);
        $('#gettutorialbutton2').prop('disabled', false);
        $('#gettutorialbutton3').prop('disabled', false);
        $('#gettutorialbutton4').prop('disabled', false);
        $('#gettutorialbutton5').prop('disabled', false);
        $('#gettutorialbutton6').prop('disabled', false);
    } else if (tutorialItem == 5) {
        $('#gettutorialbutton1').prop('disabled', false);
        $('#gettutorialbutton2').prop('disabled', false);
        $('#gettutorialbutton3').prop('disabled', false);
        $('#gettutorialbutton4').prop('disabled', false);
        $('#gettutorialbutton5').prop('disabled', false);
    } else if (tutorialItem == 4) {
        $('#gettutorialbutton1').prop('disabled', false);
        $('#gettutorialbutton2').prop('disabled', false);
        $('#gettutorialbutton3').prop('disabled', false);
        $('#gettutorialbutton4').prop('disabled', false);
    } else if (tutorialItem == 3) {
        $('#gettutorialbutton1').prop('disabled', false);
        $('#gettutorialbutton2').prop('disabled', false);
        $('#gettutorialbutton3').prop('disabled', false);
    } else if (tutorialItem ==2) {
        $('#gettutorialbutton1').prop('disabled', false);
        $('#gettutorialbutton2').prop('disabled', false);
    } else {
        $('#gettutorialbutton1').prop('disabled', false);
    }
};

function update_tutorial_progress(tutorialNo) {
    console.log("update user tutorial pogress!") // sanity check
    
    var map4 = {
                    // take away all the empty space from the input using .replace(/s+/g, '')
                    skill_id:  $('#skill_id').val(),
                    studentId: $('#student_id').val(),
                    tutorialNo: tutorialNo,
    };

        $.ajax({
        url  : "/update_tutorial_progress", // the endpoint
        type : "POST", // http method
        data : {update_tutorial_progress:JSON.stringify(map4)}, // data sent with the post request

            success: function (json) {
                console.log (json);
             },

            error : function (xhr, errmsg, err) {
                console.log(xhr.status + ":" +xhr.responseText);
            }
            
        });
};


function getNextTutorial(tutorialNo, total_ani){
    console.log("trying to get next tutorial");
    if (tutorialNo ==1 && tutorialNo < total_ani){
        $('#gettutorialbutton2').prop('disabled', false);
    } else if (tutorialNo ==2 && tutorialNo < total_ani){
        $('#gettutorialbutton3').prop('disabled', false);
    } else if (tutorialNo ==3 && tutorialNo < total_ani){
        $('#gettutorialbutton4').prop('disabled', false);
    } else if (tutorialNo ==4 && tutorialNo < total_ani){
        $('#gettutorialbutton5').prop('disabled', false);
    } else if (tutorialNo ==5 && tutorialNo < total_ani){
        $('#gettutorialbutton6').prop('disabled', false);
    }
}

	// Submit post on submit
	$('#get_tutorial1').on('submit', function(event){
		event.preventDefault();
        console.log("tutorial request submitted!"); // sanity check
		tutorialNo = 1;
        create_post(tutorialNo);
	});
	
    $('#get_tutorial2').on('submit', function(event){
        event.preventDefault();
        console.log("tutorial request submitted!"); // sanity check
        tutorialNo = 2;
        create_post(tutorialNo);
    });

    $('#get_tutorial3').on('submit', function(event){
        event.preventDefault();
        console.log("tutorial request submitted!"); // sanity check
        tutorialNo = 3;
        create_post(tutorialNo);
    });

    $('#get_tutorial4').on('submit', function(event){
        event.preventDefault();
        console.log("tutorial request submitted!"); // sanity check
        tutorialNo = 4;
        create_post(tutorialNo);
    });

    $('#get_tutorial5').on('submit', function(event){
        event.preventDefault();
        console.log("tutorial request submitted!"); // sanity check
        tutorialNo = 5;
        create_post(tutorialNo);
    });

    $('#get_tutorial6').on('submit', function(event){
        event.preventDefault();
        console.log("tutorial request submitted!"); // sanity check
        tutorialNo = 6;
        create_post(tutorialNo);
    });

    $('#get_tutorial_button').on('submit', function(event){
        event.preventDefault();
        show_button();
    });

    $('.icon-menu').click(function() {
    $('.skillListDiv').animate({
      left: "0px"
    }, 200);

    $('.content').animate({
      left: "285px"
    }, 200);
    });

    /* Then push them back */
    $('.icon-close').click(function() {
    $('.skillListDiv').animate({
      left: "-285px"
    }, 200);

    $('.content').animate({
      left: "0px"
    }, 200);
    });

});

