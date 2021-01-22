// After form loads focus will go to User id field.
  function firstfocus()
  {
  var price = document.add1Form.city.focus();
  return true;
  }


function priceValidate()
{

	var  price=document.getElementById("id_price").value;
	const re=/^\d+$/;

	if(re.test(price)|| price.length ==0) 
		{
		if(price.length<12)
			{
			document.getElementById("add2_error").innerHTML ="";
			return true;
			}
		else
			{
			document.getElementById("add2_error").innerHTML ="Error: Maximum of 12 digits allowed for price";
			return false;
			}
		}
	else
		{
			document.getElementById("add2_error").innerHTML ="Error: Only digits are allowed in price field";
			return false;
		}

}


function bathroomValidate()
{

	var  bathroom=document.getElementById("id_bathroom").value;
	const re=/^\d+$/;

	if(re.test(bathroom)|| bathroom.length ==0) 
		{
		if(bathroom.length<3)
			{
			document.getElementById("add2_error").innerHTML ="";
			return true;
			}
		else
			{
			document.getElementById("add2_error").innerHTML ="Error: Maximum of 2 digits allowed for bathroom";
			return false;
			}
		}
	else
		{
			document.getElementById("add2_error").innerHTML ="Error: Only digits are allowed in bathroom field";
			return false;
		}

}

function bedroomValidate()
{

	var  bedroom=document.getElementById("id_bedroom").value;
	const re=/^\d+$/;

	if(re.test(bedroom)|| bedroom.length ==0) 
		{
		if(bedroom.length<3)
			{
			document.getElementById("add2_error").innerHTML ="";
			return true;
			}
		else
			{
			document.getElementById("add2_error").innerHTML ="Error: Maximum of 2 digits allowed for bedroom";
			return false;
			}
		}
	else
		{
			document.getElementById("add2_error").innerHTML ="Error: Only digits are allowed in bedroom field";
			return false;
		}

}


function builtValidate()
{

	var  built=document.getElementById("id_built_up_area").value;
	const re=/^([0-9]*[.])?[0-9]+$/;

	if(re.test(built)|| built.length ==0) 
		{
		if(built.length<10)
			{
			document.getElementById("add2_error").innerHTML ="";
			return true;
			}
		else
			{
			document.getElementById("add2_error").innerHTML ="Error: Maximum of 10 digits allowed for area";
			return false;
			}
		}
	else
		{
			document.getElementById("add2_error").innerHTML ="Error: Only numeric values are allowed for area";
			return false;
		}

}


function carpetValidate()
{

	var carpet=document.getElementById("id_carpet_area").value;
	const re=/^([0-9]*[.])?[0-9]+$/;

	if(re.test(carpet)|| carpet.length ==0) 
		{
		if(carpet.length<10)
			{
			document.getElementById("add2_error").innerHTML ="";
			return true;
			}
		else
			{
			document.getElementById("add2_error").innerHTML ="Error: Maximum of 10 digits allowed for area";
			return false;
			}
		}
	else
		{
			document.getElementById("add2_error").innerHTML ="Error: Only numeric values are allowed for area";
			return false;
		}

}

function propertyFloorValidate()
{

	var property_floor=document.getElementById("id_property_floor").value;
	const re=/^\d+$/;

	if(re.test(property_floor)|| property_floor.length ==0) 
		{
		if(property_floor.length<3)
			{
			document.getElementById("add2_error").innerHTML ="";
			return true;
			}
		else
			{
			document.getElementById("add2_error").innerHTML ="Error: Maximum of 2 digits allowed for property floor";
			return false;
			}
		}
	else
		{
			document.getElementById("add2_error").innerHTML ="Error: Only digits are allowed for property floor";
			return false;
		}

}

function totalFloorValidate()
{

	var total_floor=document.getElementById("id_total_floor").value;
	const re=/^\d+$/;

	if(re.test(total_floor)|| total_floor.length ==0) 
		{
		if(total_floor.length<3)
			{
			document.getElementById("add2_error").innerHTML ="";
			return true;
			}
		else
			{
			document.getElementById("add2_error").innerHTML ="Error: Maximum of 2 digits allowed for total floor";
			return false;
			}
		}
	else
		{
			document.getElementById("add2_error").innerHTML ="Error: Only digits are allowed for total floor";
			return false;
		}

}


function descriptionValidate()
{
	var description=document.getElementById("id_description").value;

	if(description.length>=20)
		{
		document.getElementById("add2_error").innerHTML ="";
		return true;
		}
	else
		{
		document.getElementById("add2_error").innerHTML ="Error: Description is mandatory with a minimum of 20 character length";
		return false;
		}      
	
}