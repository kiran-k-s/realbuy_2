
function cityValidate()
{
var error = document.getElementById("add1_error");
var city=document.getElementById("add1-city").value;

if(city.length>=3 && city.length <=100)
		{
			if(/^[a-zA-Z\s]+$/.test(city))
			{
                document.getElementById("add1_error").innerHTML ="";
              
				return true;
			}
		else
			{
                document.getElementById("add1_error").innerHTML ="Error: City should only contain characters and space.";
                
				return false;
			}
		}
		
else
    {	
        document.getElementById("add1_error").innerHTML ="Error: City length should be greater than 2 characters and less than 100 characters";
  		
        return false;
    }		
}

function locationValidate()
{
var error = document.getElementById("add1_error");
var location=document.getElementById("add1-location").value;

if(location.length>=3 && location.length <=100)
		{
			if(/^[a-zA-Z\s]+$/.test(location))
			{
                document.getElementById("add1_error").innerHTML ="";
                
				return true;
			}
		else
			{
                document.getElementById("add1_error").innerHTML ="Error: Location should only contain characters and space.";
                
				return false;
			}
		}
		
else
    {	
        document.getElementById("add1_error").innerHTML ="Error: Location length should be greater than 3 characters and less than 100 characters";
        
        return false;
    }		
}


function addressValidate()
{
	var  address=document.getElementById("add1-address").value;

	if(address.length>=20)
		{
		document.getElementById("add1_error").innerHTML ="";
		return true;
		}
	else
		{
		document.getElementById("add1_error").innerHTML ="Error: Address is mandatory with a minimum of 20 character length";
		return false;
		}      
	
}




