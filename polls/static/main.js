$(function() {
// AJAX for posting
function create_post(input) {
	console.log("create post is working!") // sanity check
	
    var map2 = {
                    // take away all the empty space from the input using .replace(/s+/g, '')
                    the_workingstep : input, 
                    skill_id:  $('#skill_id').val(),
                    QueNum: $('#exeQueNo').val(),
                    workStepNo: $('#workStepNo').val(),
                    stepCount: $('#stepCount').val(),
                    studentId: $('#student_id').val(),
    };
    console.log(map2);
    console.log(JSON.stringify(map2));
    
    $.ajax({
        url  : "/checkworkingstep", // the endpoint
        type : "POST", // http method
        data : {the_workingstep:JSON.stringify(map2)}, // data sent with the post request
        
            success: function (json) {
                console.log (json);
                $('#feedback').append('the_workingstep');
                //use <br/> to make a new line in the display
                $('#feedback').html("");  //remove the previous content
                $('#feedback').prepend(json.Feedback+json.CheckingResult);
                $('#feedback').append('<img class="resize" src="/static/'+json.VisualAid+'">');
                // $('#exeQueNo').val(json.exeQueNum)
                // $('#stepCount').val(json.stepCount)
                // after checking that input is not empty the working are display back to the user
                
                

                // the color of the text will determine on whether the working is right or wrong, the effect will happen after checking the working
                //display the all the input

                
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
                    console.log(json.VisualAid);
                    if (json.VisualAid == null && json.CheckingResult ==1){
                        image.src = '/static/happy.jpg';
                    } else if (json.VisualAid == null && json.CheckingResult == 0){
                        image.src = '/static/sad.jpg';
                    } else {
                        // image.src = '/static/'+json.VisualAid;
                    }
                    console.log(image.src);
                    var para = document.createElement("p");
                    step = "stepNo"+currentStepCount;
                    para.setAttribute("id", step);
                    var node = document.createTextNode("`"+json.input+"`"+'\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0'+symbol+'\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0'+json.Feedback);
                    para.appendChild(node);
                    para.appendChild(image);
                    var element = document.getElementById("displayinput");
                    element.appendChild(para);
                    MathJax.Hub.Queue(["Typeset",MathJax.Hub, "displayinput"]);
                    return console.log("function appendInput is functioning");
                };

                function removeDisplay (stepDisplay){
                    var element = document.getElementById("displayinput");
                    var child = document.getElementById(stepDisplay);
                    element.removeChild(child);
                    return console.log("success in calling remove function");
                };

                // document.getElementById("displayinput").innerHTML += json.input +'</br>';
                document.getElementById("displayinput").style.font = "italic bold 20px arial,serif";
                currentStepCount = getCurrentStepCount();
                var stepCountNo = "stepNo"+currentStepCount;
                var tick = '\u2714';
                var cross = '\u2716';

                console.log (json);
                if (json.actionChoice == 3){
                    console.log ("stepCountNo"+stepCountNo);
                    console.log ("currentStepCount"+currentStepCount);
                    if (document.getElementById(stepCountNo) == null){
                        console.log("1");
                        appendInput(currentStepCount, tick);
                        document.getElementById(step).style.color = "black";
                        document.getElementById("editorContainer").disabled = true;
                        document.getElementById("submitbutton").disabled = true;
                        document.getElementById("answerRequest").style.display="none";
                        alert ("Congratulations!  You have completed the exercise successfully.  \n  Proceed to the progress report to continue to the next section.");
                        window.location.href = "/details/";
                        
                    }
                    else {
                        if (document.getElementById(stepCountNo).style.color == "red"){
                            console.log("3");
                            removeDisplay(stepCountNo);
                            appendInput(currentStepCount, tick);
                            document.getElementById(step).style.color = "black";
                            document.getElementById("editorContainer").disabled = true;
                            document.getElementById("submitbutton").disabled = true;
                            document.getElementById("answerRequest").style.display="none";
                            alert ("Congratulations!  You have completed the exercise successfully.  \n  Proceed to the progress report to continue to the next section.");
                            window.location.href = "/details/";
                        }
                    }
                } else if (json.actionChoice ==2){
                    if (document.getElementById(stepCountNo) == null){
                        appendInput(currentStepCount, tick);
                        document.getElementById(step).style.color = "black";
                        document.getElementById("editorContainer").disabled = true;
                        document.getElementById("submitbutton").disabled = true;
                        document.getElementById("nextQue").style.display="block";
                        document.getElementById("answerRequest").style.display="none";
                    }
                    else {
                        if (document.getElementById(stepCountNo).style.color == "red"){
                            console.log("3");
                            removeDisplay(stepCountNo);
                            appendInput(currentStepCount, tick);
                            document.getElementById(step).style.color = "black";
                            document.getElementById("editorContainer").disabled = true;
                            document.getElementById("submitbutton").disabled = true;
                            document.getElementById("nextQue").style.display="block";
                            document.getElementById("answerRequest").style.display="none";
                        }
                    }
                } else if (json.actionChoice ==1){
                    if (document.getElementById(stepCountNo) == null){
                        appendInput(currentStepCount, tick);
                        document.getElementById(stepCountNo).style.color = "black";
                        document.getElementById("workingstep-form").reset();
                        document.getElementById("nextQue").style.display="none";
                        document.getElementById("answerRequest").style.display="none";
                        $('#stepCount').val(json.stepCount);
                    } else {
                        if (document.getElementById(stepCountNo).style.color == "red"){
                            removeDisplay(stepCountNo);
                            appendInput(currentStepCount, tick);
                            document.getElementById(step).style.color = "black";
                            document.getElementById("workingstep-form").reset();
                            document.getElementById("nextQue").style.display="none";
                            document.getElementById("answerRequest").style.display="none";
                            $('#stepCount').val(json.stepCount);
                        }
                    }
                } else if (json.actionChoice ==0) {
                    console.log("into condition when answer is incorrect");
                    console.log("currentStepCount"+ currentStepCount);
                    // display the hidden answer button
                    // if (currentStepCount == 1){
                    console.log("1");
                    if (document.getElementById(stepCountNo) == null){
                        console.log("2");
                        appendInput(currentStepCount, cross);
                        document.getElementById("nextQue").style.display="none";
                        document.getElementById("answerRequest").style.display="block";
                        document.getElementById(step).style.color = "red";
                    } 
                    else {
                        if (document.getElementById(stepCountNo).style.color == "red"){
                            console.log("3");
                            removeDisplay(stepCountNo);
                            appendInput(currentStepCount, cross);
                            document.getElementById("nextQue").style.display="none";
                            document.getElementById("answerRequest").style.display="block";
                            document.getElementById(stepCountNo).style.color = "red";
                        }
                    }
                }

            },

            error : function (xhr, errmsg, err) {
                console.log(xhr.status + ":" +xhr.responseText);
                alert("The working must be a complete equation.  Please write a complete equation and submit again for checking.");
            }
    });

};

function get_hint() {
    console.log("hint button is working!") // sanity check
    
    var map3 = {
                    skill_id:  $('#skill_id').val(),
                    QueNum: $('#exeQueNo').val(),
                    workStepNo: $('#workStepNo').val(),
                    stepCount: $('#stepCount').val(),
    };
    console.log(map3);
    console.log(JSON.stringify(map3));
    
    $.ajax({
        url  : "/getworkingstephint", // the endpoint
        type : "POST", // http method
        data : {stephint:JSON.stringify(map3)}, // data sent with the post request
        
            success: function (json) {
                console.log (json);
                $('#hint').html(""); // remove the value from the input
                //use <br/> to make a new line in the display
                $('#hint').append(json.exeStepHint);
                $('#hintImage').html("");
                $('#hintImage').append('<img class = "resize" src="/static/'+json.exeHintVisualAid+'" >');
                    console.log("success in hint prepend");
            },

            error : function (xhr, errmsg, err) {
                console.log(xhr.status + ":" +xhr.responseText);
            }
    });
};

function get_answer() {
    console.log("get answer button is working")

    var map4 = {
                    skill_id: $('#skill_id').val(),
                    QueNum: $('#exeQueNo').val(),
                    workStepNo: $('#workStepNo').val(),
                    stepCount: $('#stepCount').val(),

    };
    $.ajax({
        url  : "/getworkingstepanswer",
        type : "POST",
        data : {stepanswer:JSON.stringify(map4)},

            success: function (json) {
                console.log(json.answerStep);
                $('#answer').html("");
                // document.getElementById("answer").innerHTML = "`"+json.exeStepAnswer+"`";
                $('#answer').append("<b>"+"Suggested Answer: "+"`"+json.exeStepAnswer+"`");
                console.log("success in get answer ajax");
                MathJax.Hub.Queue(["Typeset",MathJax.Hub, "answer"]);
            },
            error : function (xhr, errmsg, err) {
                console.log(xhr.status + ":" +xhr.responseText);
            }

    });
};

function get_question() {
    console.log("next button is working");
    
    

    
};

function warning()
    {
            return "go to google"; //you can put your code here.
    }
    window.onbeforeunload = warning;



function getInfo() {
    alert("Write your answer in the area provided.  Write each working step at a time.\
      When you are satisfy with the display at the right bottom, click submit to enter you answer.\
      To do correction, just scribbles on the part till it appears red in colour.");
}

	// Submit post on submit
	$('#workingstep-form').on('submit', function(event){
		event.preventDefault();
		// aim to check that the input are not empty string
        alert(editor.getMathML());
        var input = editor.getMathML();
        if(!input){
            alert("Please enter the valid working.");
        } 
        else {
            create_post(input);
        }
        
	});
	    
    $('#hintRequest').on('submit', function(event){
        event.preventDefault();
        console.log("hint submitted!");
        get_hint();
    });

    $('#answerRequest').on('submit', function(event){
        event.preventDefault();
        console.log("get answer request submitted");
        get_answer();
        
    })
    
    $('#nextQue').on('submit', function(event){
        event.preventDefault();
        console.log("next question request submitted");
        get_question();
    })

    var button = document.getElementById("info");
    button.onclick = function() {
        alert("Write your working step in the area provided.  You can choose between using handwriting or typing.  \
Click the icon on the right hand of the boxed area to change from one to the other.  Write one complete working step at a time.\
        \nFor handwriting:\
        \nUse the mouse or touch pad to write.  As you write the working, your handwriting will be processed and displayed at the right bottom of the boxed area.  \
Click submit to enter you working when you are statisfy that it is the working that you write.  To do correction, \
just scribbles on the part you want to remove till it appears red in colour.  Then write your working over it.\
        \nFor typing:\
        \nClick and choose the right mathematical symbol that you will need to complete your working.  Click submit to enter your working.  \
It will be better to use typing for long workings.");;
    }


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