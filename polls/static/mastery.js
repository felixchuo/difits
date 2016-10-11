$(function() {
// AJAX for posting
function create_post(input) {
	console.log("create post is working!") // sanity check
	
    var map2 = {
                    mas_workingstep : input, 
                    skill_id:  $('#skill_id').val(),
                    QueNum: $('#masQueNo').val(),
                    workStepNo: $('#workStepNo').val(),
                    stepCount: $('#stepCount').val(),
                    studentId: $('#student_id').val(),
                    totalQue: $('#totalQue').val(),
                    totalTry: $('#totalTry').val(),
                    masLevel: $('#masLevel').val(),
                    progressId: $('#progressId').val(),
    };
    console.log(map2);
    console.log(JSON.stringify(map2));
    
    $.ajax({
        url  : "/mas_checkworkingstep", // the endpoint
        type : "POST", // http method
        data : {mas_workingstep:JSON.stringify(map2)}, // data sent with the post request
        
            success: function (json) {
                //$('#workingstep_input').val(''); // remove the value from the input
                // $(jQuery.parse)
                console.log (json);
                $('#feedback').append('the_workingstep');
                //use <br/> to make a new line in the display
                $('#feedback').html("");  //remove the previous content
                $('#feedback').prepend(json.Feedback);

                
                function getCurrentStepCount() {
                    var currentStepCount = json.stepCount;
                    if (json.stepCount >1 && json.CheckingResult == 1){
                        currentStepCount = json.stepCount-1;
                        console.log("current step count in function when answer is correct"+currentStepCount);
                        return currentStepCount;
                    } else
                        console.log("current step count in function when answer is incorrect"+currentStepCount);
                        return currentStepCount;
                }

                function appendInput(currentStepCount, symbol){
                    var image = document.createElement("img");
                    if (json.CheckingResult == 1){
                        image.src = '/static/good.jpg';
                    } else {
                        image.src = '/static/keeptrying.jpg';
                    }
                    var para = document.createElement("p");
                    step = "stepNo"+currentStepCount;
                    para.setAttribute("id", step);
                    var node = document.createTextNode("`"+json.input+"`"+'\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0'+symbol+'\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0'+json.Feedback );
                    para.appendChild(node);
                    para.appendChild(image);
                    var element = document.getElementById("displayinput");
                    element.appendChild(para);
                    MathJax.Hub.Queue(["Typeset", MathJax.Hub, "displayinput"]);
                    return console.log("function appendInput is functioning");
                };

                function removeDisplay (stepDisplay){
                    var element = document.getElementById("displayinput");
                    var child = document.getElementById(stepDisplay);
                    element.removeChild(child);
                    return console.log("success in calling remove function");
                };

                document.getElementById("displayinput").style.font = "italic bold 20px arial,serif";
                currentStepCount = getCurrentStepCount();
                var stepCountNo = "stepNo"+currentStepCount;
                var tick = '\u2714';
                var cross = '\u2716';

                console.log (json);
                if (json.actionChoice == 6){
                    console.log ("stepCountNo"+stepCountNo);
                    console.log ("currentStepCount"+currentStepCount);
                    console.log("1");
                    appendInput(currentStepCount, tick);
                    document.getElementById(step).style.color = "black";
                    document.getElementById("editorContainer").disabled = true;
                    document.getElementById("submitbutton").disabled = true;
                    document.getElementById("masanswerRequest").style.display="none";
                    alert ("Congratulations!  You have achieved all the mastery level for this skill successfully.  \n  Proceed to the progess report to continue to the next section.");
                } else if (json.actionChoice == 5){
                    console.log ("stepCountNo"+stepCountNo);
                    console.log ("currentStepCount"+currentStepCount);
                    console.log("1");
                    appendInput(currentStepCount, tick);
                    document.getElementById(step).style.color = "black";
                    document.getElementById("editorContainer").disabled = true;
                    document.getElementById("submitbutton").disabled = true;
                    document.getElementById("masanswerRequest").style.display="none";
                    
                    alert ("Well done!  You have achieved moderate mastery for this skill successfully.  \n  Click on continue to go to the next level.");
                    document.getElementById("nextMasLevel").style.display = "block";
                } else if (json.actionChoice == 4){
                    console.log ("stepCountNo"+stepCountNo);
                    console.log ("currentStepCount"+currentStepCount);
                    console.log("1");
                    appendInput(currentStepCount, tick);
                    document.getElementById(step).style.color = "black";
                    document.getElementById("editorContainer").disabled = true;
                    document.getElementById("submitbutton").disabled = true;
                    document.getElementById("masanswerRequest").style.display="none";
                    alert ("Marvelous!  You have completed the easy level of mastery for this skill successfully.  \n  Click on continue to go to the next level.");
                    document.getElementById("nextMasLevel").style.display = "block";
                } else if (json.actionChoice ==3){
                    appendInput(currentStepCount, tick);
                    document.getElementById(step).style.color = "black";
                    document.getElementById("editorContainer").disabled = true;
                    document.getElementById("submitbutton").disabled = true;
                    document.getElementById("nextQue").style.display="block";
                    document.getElementById("nextQue").disabled=false;
                    document.getElementById("masanswerRequest").style.display="none";
                } else if (json.actionChoice ==2){
                    appendInput(currentStepCount, tick);
                    document.getElementById(step).style.color = "black";
                    document.getElementById("mastery-form").reset();
                    document.getElementById("nextQue").style.display="none";
                    document.getElementById("masanswerRequest").style.display="none";
                    document.getElementById("submitbutton").disabled = false;
                    $('#stepCount').val(json.stepCount);
                } else if (json.actionChoice ==1){
                    appendInput(currentStepCount, cross);
                    document.getElementById(step).style.color = "red";
                    alert ("Very sorry, you have not acheived the required mastery of the skill.  Please go through to the tutorial and exercise section of this skill.  Come back and test your mastery again after that.")
                    document.getElementById("editorContainer").disabled = true;
                    document.getElementById("submitbutton").disabled = true;
                    document.getElementById("masanswerRequest").style.display="none";
                    
                } else {
                    console.log("action choice: 0");
                    appendInput(currentStepCount, cross);
                    document.getElementById(step).style.color = "red";
                    alert("Very sorry, your working is wrong.  Please proceed to try the next question.  Before that you can see the answer to the working if you want to.")
                    document.getElementById("nextQue").style.display="block";
                    document.getElementById("nextQue").disabled = false;
                    document.getElementById("masanswerRequest").style.display="block";
                    document.getElementById("submitbutton").disabled = true;
                } 
            },

            error : function (xhr, errmsg, err) {
                console.log(xhr.status + ":" +xhr.responseText);
                alert("The working must be a complete equation.  Please write a complete equation and submit again for checking.");
            }
    });

};

function get_mas_hint() {
    console.log("hint button is working!") // sanity check
    
    var map3 = {
                    skill_id:  $('#skill_id').val(),
                    QueNum: $('#masQueNo').val(),
                    workStepNo: $('#workStepNo').val(),
                    stepCount: $('#stepCount').val(),
    };
    console.log(map3);
    console.log(JSON.stringify(map3));
    
    $.ajax({
        url  : "/get_masworkingstephint", // the endpoint
        type : "POST", // http method
        data : {masstephint:JSON.stringify(map3)}, // data sent with the post request
        
            success: function (json) {
                console.log (json);
                $('#hint').html(""); // remove the value from the input
                //use <br/> to make a new line in the display
                $('#hint').append(json.masHint);
                $('#hintImage').html("");
                $('#hintImage').append('<img class = "resize" src="/static/'+json.exeHintVisualAid+'" >');
                    console.log("success in hint prepend");
            },

            error : function (xhr, errmsg, err) {
                console.log(xhr.status + ":" +xhr.responseText);
            }
    });
};

function get_mas_answer() {
    console.log("get answer button is working")

    var map4 = {
                    skill_id: $('#skill_id').val(),
                    QueNum: $('#masQueNo').val(),
                    workStepNo: $('#workStepNo').val(),
                    stepCount: $('#stepCount').val(),

    };
    $.ajax({
        url  : "/get_masworkingstepanswer",
        type : "POST",
        data : {masstepanswer:JSON.stringify(map4)},

            success: function (json) {
                console.log (json);
                $('#answer').html("");
                $('#answer').append("<b>"+"Suggested Answer: "+"`"+json.masWorkStepAnswer+"`");
                console.log("success in get answer ajax");
                MathJax.Hub.Queue(["Typeset",MathJax.Hub, "answer"]);
            },
            error : function (xhr, errmsg, err) {
                console.log(xhr.status + ":" +xhr.responseText);
            }

    });
};

function get_mas_button() {
    console.log("get mastery button is working");
    
    var map5 = {
                    skill_id:  $('#skill_id').val(),
                    studentId: $('#student_id').val(),
                    masLevel:  $('#masLevel').val(),
    };
    console.log(map5);
    console.log(JSON.stringify(map5));
    
    $.ajax({
        url  : "/mas_get_questions", // the endpoint
        type : "POST", // http method
        data : {mas_get_questions:JSON.stringify(map5)}, // data sent with the post request
    
        success: function (json) {
                console.log (json);
                console.log("success in get answer ajax");
                display_button(json.totalQue);
                display_instruction(json.masLevel);
                masQueInfo = json.questions;
                console.log(masQueInfo);
                // prepare_question(json.totalQue, json);
                document.getElementById("totalQue").value = json.totalQue;
                console.log(json.questions[0]['masQueExpression']);
                console.log(json.questions[1]);
             },
            error : function (xhr, errmsg, err) {
                console.log(xhr.status + ":" +xhr.responseText);
            }



    });

    
};


function display_button (totalQue) {
    console.log("show question button is working")
    if (totalQue == 6){
            document.getElementById("getmasterybutton").style.display="none";
            document.getElementById("getMasQueButton1").style.display="block";
            // $('#gettutorialbutton1').prop('disabled', false);
            document.getElementById("getMasQueButton2").style.display="block";
            document.getElementById("getMasQueButton3").style.display="block";
            document.getElementById("getMasQueButton4").style.display="block";
            document.getElementById("getMasQueButton5").style.display="block";
            document.getElementById("getMasQueButton6").style.display="block";
    } else if (totalQue == 5){
            document.getElementById("getmasterybutton").style.display="none";
            document.getElementById("getMasQueButton1").style.display="block";
            // $('#gettutorialbutton1').prop('disabled', false);
            document.getElementById("getMasQueButton2").style.display="block";
            document.getElementById("getMasQueButton3").style.display="block";
            document.getElementById("getMasQueButton4").style.display="block";
            document.getElementById("getMasQueButton5").style.display="block";
    } else if (totalQue == 4){
            document.getElementById("getmasterybutton").style.display="none";
            document.getElementById("getMasQueButton1").style.display="block";
            // $('#gettutorialbutton1').prop('disabled', false);
            document.getElementById("getMasQueButton2").style.display="block";
            document.getElementById("getMasQueButton3").style.display="block";
            document.getElementById("getMasQueButton4").style.display="block";
    } else if (totalQue == 3){
            document.getElementById("getmasterybutton").style.display="none";
            document.getElementById("getMasQueButton1").style.display="block";
            // $('#gettutorialbutton1').prop('disabled', false);
            document.getElementById("getMasQueButton2").style.display="block";
            document.getElementById("getMasQueButton3").style.display="block";
    } else if (totalQue == 2){
            document.getElementById("getmasterybutton").style.display="none";
            document.getElementById("getMasQueButton1").style.display="block";
            // $('#gettutorialbutton1').prop('disabled', false);
            document.getElementById("getMasQueButton2").style.display="block";
    } else {
            document.getElementById("getmasterybutton").style.display="none";
            document.getElementById("getMasQueButton1").style.display="block";
            // $('#gettutorialbutton1').prop('disabled', false);
    }

    // """activate the button"""
    if (totalQue ==6){
        $('#getMasQueButton1').prop('disabled', false);
        $('#getMasQueButton2').prop('disabled', false);
        $('#getMasQueButton3').prop('disabled', false);
        $('#getMasQueButton4').prop('disabled', false);
        $('#getMasQueButton5').prop('disabled', false);
        $('#getMasQueButton6').prop('disabled', false);
    } else if (totalQue == 5) {
        $('#getMasQueButton1').prop('disabled', false);
        $('#getMasQueButton2').prop('disabled', false);
        $('#getMasQueButton3').prop('disabled', false);
        $('#getMasQueButton4').prop('disabled', false);
        $('#getMasQueButton5').prop('disabled', false);
    } else if (totalQue == 4) {
        $('#getMasQueButton1').prop('disabled', false);
        $('#getMasQueButton2').prop('disabled', false);
        $('#getMasQueButton3').prop('disabled', false);
        $('#getMasQueButton4').prop('disabled', false);
    } else if (totalQue == 3) {
        $('#getMasQueButton1').prop('disabled', false);
        $('#getMasQueButton2').prop('disabled', false);
        $('#getMasQueButton3').prop('disabled', false);
    } else if (totalQue ==2) {
        $('#getMasQueButton1').prop('disabled', false);
        $('#getMasQueButton2').prop('disabled', false);
    } else {
        $('#getMasQueButton1').prop('disabled', false);
    }
};

function display_instruction(masLevel){
    if (masLevel == 1){
        $('#instructionInfo').html("");
        $('#instructionInfo').append("Answer "+"<span class='emphasize'>"+"two "+"</span>"+"questions correctly to proceed to the next level.");
    } else if (masLevel ==2){
        $('#instructionInfo').html("");
        $('#instructionInfo').append("Congratulations. <br> You have pass the basic level. <br>"+
            "\n Answer "+"<span class='emphasize'>"+"two "+"</span>"+" questions correctly to proceed to the next level.");
        $('#instructionInfo').append("");
    } else {
        $('#instructionInfo').html("");
        $('#instructionInfo').append("Congratulations. <br> You have pass the basic and average level."+
            "\n  <br>  Answer "+"<span class='emphasize'>"+"one "+"</span>"+" questions correctly to achieve mastery in this level.");

    }
};


function prepare_question(totalQue, json){
    if (totalQue == 6){
            
    } else if (totalQue == 5){
            
    } else if (totalQue == 4){

    } else if (totalQue == 3){

    } else if (totalQue == 2){

    } else {

    }


};

function getQue(masQueNo){
    console.log(masQueNo);
    console.log(masQueInfo[masQueNo]['masQueExpression']);
    $('#queText').html("");
    $('#queText').append(masQueInfo[masQueNo]['Que']+".  ");
    $('#queText').append(masQueInfo[masQueNo]['masQueText']);
    $('#queText').append("<br>"+"<p style='font-size:1.6em'>"+"<b>"+"`"+masQueInfo[masQueNo]['masQueExpression']+"`"+"</b>"+"</p>");
    $('#queText').append("<br>You can solve this in "+"<span class='emphasize'>"+masQueInfo[masQueNo]['masTotalWorkSteps']+"</span>"+" working steps.");
    MathJax.Hub.Queue(["Typeset",MathJax.Hub, "queText"]);
    document.getElementById("mastery-form").style.display="block";
    document.getElementById("submitbutton").disabled = false;
    $('#displayinput').html("");
    document.getElementById("masQueNo").value = masQueInfo[masQueNo]['mastery'];
    document.getElementById("workStepNo").value = masQueInfo[masQueNo]['masTotalWorkSteps'];
    var totalTry = parseInt(document.getElementById("totalTry").value);
    totalTry = totalTry+1;
    document.getElementById("totalTry").value = totalTry;
    console.log (document.getElementById("totalTry").value);
    if (masQueNo ==0){
        $('#getMasQueButton1').prop('disabled', true);
        $('#getMasQueButton2').prop('disabled', true);
        $('#getMasQueButton3').prop('disabled', true);
        $('#getMasQueButton4').prop('disabled', true);
        $('#getMasQueButton5').prop('disabled', true);
        $('#getMasQueButton6').prop('disabled', true);
    } else if (masQueNo == 1) {
        $('#getMasQueButton1').prop('disabled', true);
        $('#getMasQueButton2').prop('disabled', true);
        $('#getMasQueButton3').prop('disabled', true);
        $('#getMasQueButton4').prop('disabled', true);
        $('#getMasQueButton5').prop('disabled', true);
        $('#getMasQueButton6').prop('disabled', true);
    } else if (masQueNo == 2) {
        $('#getMasQueButton1').prop('disabled', true);
        $('#getMasQueButton2').prop('disabled', true);
        $('#getMasQueButton3').prop('disabled', true);
        $('#getMasQueButton4').prop('disabled', true);
        $('#getMasQueButton5').prop('disabled', true);
        $('#getMasQueButton6').prop('disabled', true);
    } else if (masQueNo == 3) {
        $('#getMasQueButton1').prop('disabled', true);
        $('#getMasQueButton2').prop('disabled', true);
        $('#getMasQueButton3').prop('disabled', true);
        $('#getMasQueButton4').prop('disabled', true);
        $('#getMasQueButton5').prop('disabled', true);
        $('#getMasQueButton6').prop('disabled', true);
    } else if (masQueNo ==4) {
        $('#getMasQueButton1').prop('disabled', true);
        $('#getMasQueButton2').prop('disabled', true);
        $('#getMasQueButton3').prop('disabled', true);
        $('#getMasQueButton4').prop('disabled', true);
        $('#getMasQueButton5').prop('disabled', true);
        $('#getMasQueButton6').prop('disabled', true);
    } else {
        $('#getMasQueButton1').prop('disabled', true);
        $('#getMasQueButton2').prop('disabled', true);
        $('#getMasQueButton3').prop('disabled', true);
        $('#getMasQueButton4').prop('disabled', true);
        $('#getMasQueButton5').prop('disabled', true);
        $('#getMasQueButton6').prop('disabled', true);
    }


};



	// Submit post on submit
	$('#mastery-form').on('submit', function(event){
		event.preventDefault();
        console.log("form submitted!"); // sanity check
		// aim to check that the input are not empty string
        var input = editor.getMathML();
        if(!input){
            alert("Please enter the valid working.");
        } 
        else {
            create_post(input);
        }
        
	});
	    
    $('#mashintRequest').on('submit', function(event){
        event.preventDefault();
        console.log("hint submitted!");
        get_mas_hint();
    });

    $('#masanswerRequest').on('submit', function(event){
        event.preventDefault();
        console.log("get answer request submitted");
        get_mas_answer();
    });
    
    // $('#nextQue').on('submit', function(event){
    //     event.preventDefault();
    //     console.log("next question request submitted");
    //     document.getElementById("masanswerRequest").style.display="none";
    //     get_question();
    // });

    $('#get_mastery_button').on('submit', function(event){
        event.preventDefault();
        console.log("get mastery button request submitted");
        get_mas_button();
    });

    $('#get_masQue1').on('submit', function(event){
        event.preventDefault();
        console.log("get mastery question request submitted!"); // sanity check
        masQueNo = 0;
        getQue(masQueNo);
    });
    
    $('#get_masQue2').on('submit', function(event){
        event.preventDefault();
        console.log("get mastery question request submitted!"); // sanity check
        masQueNo = 1;
        getQue(masQueNo);
    });

    $('#get_masQue3').on('submit', function(event){
        event.preventDefault();
        console.log("get mastery question request submitted!"); // sanity check
        masQueNo = 2;
        getQue(masQueNo);
    });

    $('#get_masQue4').on('submit', function(event){
        event.preventDefault();
        console.log("get mastery question request submitted!"); // sanity check
        masQueNo = 3;
        getQue(masQueNo);
    });

    $('#get_masQue5').on('submit', function(event){
        event.preventDefault();
        console.log("get mastery question request submitted!"); // sanity check
        masQueNo = 4;
        getQue(masQueNo);
    });

    $('#get_masQue6').on('submit', function(event){
        event.preventDefault();
        console.log("get mastery question request submitted!"); // sanity check
        masQueNo = 5;
        getQue(masQueNo);
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

    var button = document.getElementById("info");
    button.onclick = function() {
        alert("Write your answer in the area provided.  Write each working step at a time.\
      When you are satisfy with the display at the right bottom, click submit to enter you answer.\
      To do correction, just scribbles on the part till it appears red in colour.");;
    }



});


function displayActiveButton(){
    var x = parseInt(document.getElementById("totalQue").value);
    console.log(x);
    for (i = 1; i < x+1; i++){
        var identity = "getMasQueButton"+i;
        var matchIdentity = "Question "+i;
        console.log(identity);
        console.log(matchIdentity);
        if (document.getElementById(identity).value == matchIdentity){
            $('#getMasQueButton'+i).prop('disabled', false);
        }
    }
    document.getElementById("nextQue").style.display="none";
    document.getElementById("masanswerRequest").style.display="none";
    document.getElementById("stepCount").value="1";
}

function change(i) // no ';' here
{
    console.log(i);
    var identify = "getMasQueButton"+i;
    var changeIdentify = "Question "+i+".  Done"
    console.log(identify);
    console.log(changeIdentify);
    document.getElementById(identify).value = changeIdentify;
    document.getElementById(identify).style.disabled = true;
}

