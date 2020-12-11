
/*function validate(){
  var name = document.getElementById("inputName").value;
  var email = document.getElementById("inputEmail").value;
  var phone = document.getElementById("inputPhone").value;
  var message = document.getElementById("inputMessage").value;
  var error_message = document.getElementById("error_message");
  
  error_message.style.padding = "10px";
  
  var text;
  if(name.length < 5){
    text = "Please Enter valid Name";
    error_message.innerHTML = text;
    return false;
  }
  if(email.indexOf("@") == -1 || email.length < 6){
    text = "Please Enter valid Email";
    error_message.innerHTML = text;
    return false;
  }
  if(isNaN(phone) || phone.length != 10){
    text = "Please Enter valid Phone Number";
    error_message.innerHTML = text;
    return false;
  }
  if(message.length <= 140){
    text = "Please Enter More Than 140 Characters";
    error_message.innerHTML = text;
    return false;
  }
  //alert("Form Submitted Successfully!");
  //return true;
} */
/*function nameValidate()
{
var name=document.getElementById("inputName").value;

if(name.length>=3 && name.length <=100)
		{
			if(/^[a-zA-Z\s]+$/.test(name))
			{
                document.getElementById("nameError").innerHTML ="";
				return true;
			}
		else
			{
                document.getElementById("nameError").innerHTML ="Error: Name should only contain characters and space.";
				return false;
			}
		}
		
else
    {	
        document.getElementById("nameError").innerHTML ="Error: Name length should be greater than 3 characters and less than 100 characters";
        return false;
    }		
}

function mailValidate()
{
var email=document.getElementById("inputEmail").value;
const re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
if(re.test(email))
		{
			document.getElementById("mailError").innerHTML ="";
			return true;
		}
    
else
		{
			document.getElementById("mailError").innerHTML ="Error: Invalid E-mail id";
			return false;
		}

}

function numberValidate()
{

	var  mobile=document.getElementById("inputPhone").value;
	const re=/^\d+$/;

	if(re.test(mobile)|| mobile.length ==0) 
		{
		if(mobile.length==0 || mobile.length ==10)
			{
			document.getElementById("phoneError").innerHTML ="";
			return true;
			}
		else
			{
			document.getElementById("phoneError").innerHTML ="Error: Invalid phone number";
			return false;
			}
		}
	else
		{
			document.getElementById("phoneError").innerHTML ="Error: Invalid phone number";
			return false;
		}

}

function messageValidate()
{
	var  message=document.getElementById("inputMessage").value;

	if(message.length>=20)
		{
		document.getElementById("descriptionError").innerHTML ="";
		return true;
		}
	else
		{
		document.getElementById("descriptionError").innerHTML ="Error: Description is mandatory with a minimum of 20 character length";
		return false;
		}      
	
}   */
const form = document.getElementById('contactForm');
form.addEventListener("submit", submitHandler);

function submitHandler(e) {
    e.preventDefault();
    $.ajax({
        type        : 'POST', // define the type of HTTP verb we want to use (POST for our form)
        url         : '{% url 'contactus' %}', // the url where we want to POST
        data        : $('#contactForm').serialize(), // our form data
        dataType    : 'json', // what type of data do we expect back from the server
        success     : successFunction
    });
}

function successFunction(msg) {
    if (msg.message === 'success') {
        alert('Success!');
        form.reset()
    }
}

   /*

        $(document).ready(function(){
            $('#fbutton').click(function(e){
                  //var isvalid=validation()
                  
                  e.preventDefault();
                  console.log("Hello");
                    var nameok=nameValidate();
                    var emailok=mailValidate();
                    var mobok=numberValidate();
                    var mesok=messageValidate();
          if(nameok==true && emailok==true && mobok==true && mesok==true){
                  $.ajax({

                    headers: { "X-CSRFToken": "{{ csrf_token }}" },

                          method:'POST',
                          url:'/add',
                          data:{
                                'csrfmiddlewaretoken':'{{ csrf_token }}',

                                name:$('#inputName').val(),
                                email:$('#inputEmail').val(),
                                phone:$('#inputPhone').val(),
                                message:$('#inputMessage').val(),
                         },
                      
                    success:function(response){
                     
                      document.getElementById('success').innerHTML="Succesfully added data"
                     
                      $('#cform').trigger('reset')
                    

                    }
                  

                })

          }


                })          
        });           */


		
		

