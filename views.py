from django.shortcuts import render,HttpResponseRedirect
from account.forms import userRegisterForm,UserEditForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash

# Create your views here.

def UserRegisterView(request):
    if request.method=="POST":
        fm = userRegisterForm(request.POST)

        if fm.is_valid():
            fm.save()
            messages.success(request,"User Register Successfully!")
    else:
        fm = userRegisterForm()

    return render(request,'account/singup.html',{'form':fm})

def UserLoginView(request):
    if not request.user.is_authenticated:

        if request.method=="POST":
            fm = AuthenticationForm(request= request,data=request.POST)
            if fm.is_valid():
                username = fm.cleaned_data['username']
                upassword = fm.cleaned_data['password']
                user = authenticate(username=username,password=upassword)

                if user is not None:
                    login(request,user)

                    messages.success(request,"user login successfully")
                    return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()

        return render(request,'account/singin.html',{'form':fm})
    
    else:
        return HttpResponseRedirect('/profile/')

def UserProfile(request):
    if request.user.is_authenticated:
        return render(request,'account/profile.html')
    else:
        return HttpResponseRedirect('/singin/')

def UserLogout(request):
    logout(request)
    messages.success(request,"user logout successfully")
    return HttpResponseRedirect('/singin/')


def UserPasswordChange(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            fm = PasswordChangeForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.success(request,"Password Change Successfuly!")
                return HttpResponseRedirect('/profile/')
        else:
            fm = PasswordChangeForm(user=request.user)

        return render(request,'account/change-password.html',{'form':fm})
    else:
        messages.error(request,"please login frist")
        return HttpResponseRedirect('/singin/')

def UserProfileEdit(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = UserEditForm(request.POST, instance=request.user)
            if fm.is_valid():
                fm.save()
                messages.success(request, "Profile Updated Successfully")
                return HttpResponseRedirect('/profile/')
        else:
            fm = UserEditForm(instance=request.user)
            return render(request, 'account/edit-profile.html', {'form': fm})
    else:
        messages.error(request, "Please log in to update your profile")
        return HttpResponseRedirect('/signin/')