from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import signup, Detail
from sklearn.linear_model import LinearRegression
import numpy as np
import statsmodels.api as sm
from django.http import JsonResponse

# code for index of webpage
def index(request):
    return render(request,'index.html')

# code for about us of webpage
def aboutus(request):
    return render(request,'aboutus.html')

# code for user login
def mainpage(request):
    if request.method == 'POST':
        getcompanyname = request.POST.get('companyname')
        getpassword = request.POST.get('password')

        try:
            company = signup.objects.get(companyname=getcompanyname, password=getpassword)
            # If login is successful, return a JSON response with the redirect URL
            return JsonResponse({'message': 'Login successful!', 'redirect_url': '/loginpage/'}, status=200)
        except signup.DoesNotExist:
            # If login fails, return a JSON response with an error message
            return JsonResponse({'message': 'Invalid company name or password'}, status=400)

    return render(request, 'mainpage.html')

# code for user register form
def signuppage(request):
    if request.method == 'POST':
        # Fetching data from the form using POST
        getcompanyname = request.POST.get('companyname')
        getaddress = request.POST.get('address')
        getcity = request.POST.get('city')
        getstate = request.POST.get('state')
        getzip = request.POST.get('zip')
        getcountry = request.POST.get('country')
        getphonenumber = request.POST.get('phonenumber')
        getemail = request.POST.get('email')
        getwebsite = request.POST.get('website')
        getpassword = request.POST.get('password')

        # Creating an instance of the Signup model
        users = signup(
            companyname=getcompanyname,
            address=getaddress,
            city=getcity,
            state=getstate,
            zip=getzip,
            country=getcountry,
            phonenumber=getphonenumber,
            email=getemail,
            website=getwebsite,
            password=getpassword,
        )
        users.save()

        # Return a success message as a JSON response
        return JsonResponse({'message': 'Signup successful!'}, status=200)

    return render(request, 'signuppage.html')

# code to get quantity of aluminum and location
def loginpage(request):
    if request.method == 'POST':
        getaluminum = request.POST.get('aluminum')
        getlocation = request.POST.get('location')

        try:
            # Query the detail model with provided values
            details = Detail.objects.get(aluminum=getaluminum, location=getlocation)
            return redirect('result', aluminum=getaluminum, location=getlocation) # Redirect to the result page
        except Detail.DoesNotExist:
            return HttpResponse('No matching details found')  # Return error if no matching record is found

    return render(request, 'loginpage.html')

# code for result page
def result(request, aluminum, location):
    try:
        # Get the details based on the provided aluminum and location
        data = Detail.objects.get(aluminum=aluminum, location=location)
        return render(request, 'result.html', {'value': data, 'message': 'Data retrieved successfully!'})  # Pass the message to the template
    except Detail.DoesNotExist:
        # Handle the case where the record is not found
        return render(request, 'result.html', {'error': 'No matching details found for the provided aluminum and location'})

# code for admin page to add the material detail
def convert_to_float(value):
    try:
        return float(value)
    except ValueError:
        if '-' in value:
            range_values = value.split('-')
            try:
                low = float(range_values[0].strip())
                high = float(range_values[1].strip().split()[0])
                return (low + high) / 2
            except (ValueError, IndexError):
                raise ValueError(f"Invalid range format: {value}")
        raise ValueError(f"Cannot convert {value} to float")

def detail_view(request):
    if request.method == 'POST':
        try:
            aluminum_str = request.POST.get('aluminum')
            bauxite_str = request.POST.get('bauxite')
            alumina_str = request.POST.get('alumina')
            causticsoda_str = request.POST.get('causticsoda')
            lime_str = request.POST.get('lime')
            cryolite_str = request.POST.get('cryolite')
            carbonanodes_str = request.POST.get('carbonanodes')
            electricity_str = request.POST.get('electricity')

            getaluminum = convert_to_float(aluminum_str)
            getbauxite = convert_to_float(bauxite_str)
            getalumina = convert_to_float(alumina_str)
            getcausticsoda = convert_to_float(causticsoda_str)
            getlime = convert_to_float(lime_str)
            getcryolite = convert_to_float(cryolite_str)
            getcarbonanodes = convert_to_float(carbonanodes_str)
            getelectricity = convert_to_float(electricity_str)

        except ValueError as e:
            return render(request, 'detail.html', {'error': str(e)})

        getlocation = request.POST.get('location')

        user = Detail(
            aluminum=aluminum_str,
            bauxite=bauxite_str,
            alumina=alumina_str,
            causticsoda=causticsoda_str,
            lime=lime_str,
            cryolite=cryolite_str,
            carbonanodes=carbonanodes_str,
            electricity=electricity_str,
            location=getlocation
        )
        user.save()

        # Pass a success message to the template
        success_message = "Your data has been successfully submitted!"

        # Pass data and message to template
        context = {
            'success_message': success_message
        }

        return render(request, 'detail.html', context)

    return render(request, 'detail.html')
