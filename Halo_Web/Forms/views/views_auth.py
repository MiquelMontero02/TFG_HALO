from .views_import import *

from Forms.utils import *



def main(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def profile(request):
  token = request.session.get("auth_token")
  if not token:
    return redirect("login")
  
  headers={"Authorization":f"Bearer {token}"}
  url=URL+"user/"

  response=requests.get(url,headers=headers)
  userInf=response.json()["message"]
  return render(request, "profile.html",{"user":userInf})

def logout_view(request):
  
  return render (request, "index.html")

@csrf_exempt
def start_registration(request):
    if request.method=="POST":
      data = json.loads(request.body)

      token = store_user_temp(data)
      send_confirmation_email(data['email'], token)

      return JsonResponse({'message': 'Correo enviado para confirmar registro'})
    
    return render(request, "registration/register.html")
    

@csrf_exempt
def register_user(request,token):
  key = f'pending_user:{token}'
  data = cache.get(key)

  if not data:
      return JsonResponse({'error': 'Token inválido o expirado'}, status=400)

  url = URL + "user/"
  response = requests.post(url, json=data)
  
  if response.status_code == 200:
      cache.delete(key)  # Eliminar los datos después de usarlos
      return redirect('login')
  else:
      return JsonResponse({'status':'error','message':'Error interno, sistema no operativo:'},status=405)


@csrf_exempt
def login_manual(request):
  if request.method == "POST":
      
      email = request.POST.get("email")
      password = request.POST.get("password")
      data={"email":email, "password":password}

      url=URL+"login"
      
      response=requests.post(url,json=data)
      if response.status_code == 200:
        response_data = response.json()
        token = response_data.get("token")

        if token:
          request.session["auth_token"] = token
          request.session.set_expiry(3600)
          return redirect("profile")
        else:
          return JsonResponse({'status':'error','message':'Error interno, sistema no operativo'},status=405)
      else:
          return render(request, "registration/login.html",{"messages":["Los datos introducidos son incorrectos"]})
  return render(request, "registration/login.html")
