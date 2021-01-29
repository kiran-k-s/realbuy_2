function nameValidate()
{
var error = document.getElementById("edit_profile_error");
var name=document.getElementById("profile-edit-name").value;

if(name.length>=3 && name.length <=100)
		{
			if(/^[a-zA-Z\s]+$/.test(name))
			{
                document.getElementById("edit_profile_error").innerHTML ="";
				return true;
			}
		else
			{
                document.getElementById("edit_profile_error").innerHTML ="Error: Name should only contain characters and space.";
                
				return false;
			}
		}
		
else
    {	
        document.getElementById("edit_profile_error").innerHTML ="Error: Name length should be greater than 3 characters and less than 100 characters";
  
        return false;
    }		
}

function mailValidate()
{
var email=document.getElementById("profile-edit-email").value;
const re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
if(re.test(email))
		{
			document.getElementById("edit_profile_error").innerHTML ="";
			return true;
		}
    
else
		{
			document.getElementById("edit_profile_error").innerHTML ="Error: Invalid E-mail id";
			return false;
		}

}

function phoneValidate()
{

	var  mobile=document.getElementById("profile-edit-phone").value;
	const re=/^\d+$/;

	if(re.test(mobile)|| mobile.length ==0) 
		{
		if(mobile.length==0 || mobile.length ==10)
			{
			document.getElementById("edit_profile_error").innerHTML ="";
			return true;
			}
		else
			{
			document.getElementById("edit_profile_error").innerHTML ="Error: Invalid phone number";
			return false;
			}
		}
	else
		{
			document.getElementById("edit_profile_error").innerHTML ="Error: Invalid phone number";
			return false;
		}

}

function addressValidate()
{
	var  address=document.getElementById("profile-edit-address").value;

	if(address.length>=20)
		{
		document.getElementById("edit_profile_error").innerHTML ="";
		return true;
		}
	else
		{
		document.getElementById("edit_profile_error").innerHTML ="Error: Address is mandatory with a minimum of 20 character length";
		return false;
		}      
	
}