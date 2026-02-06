# Authentication Templates for LaptopXplorer

## Directory Structure

Create these directories in `src/templates/`:
- `account/` (for django-allauth templates)
- `accounts/` (for custom profile templates)

## Files to Create

### 1. src/templates/account/login.html
```html
{% extends 'base.html' %}
{% load socialaccount %}

{% block title %}Login - LaptopXplorer{% endblock %}

{% block content %}
<div class="min-h-screen bg-gradient-to-br from-purple-50 to-pink-50 flex items-center justify-center py-12 px-4">
    <div class="max-w-md w-full">
        <div class="bg-white rounded-2xl shadow-2xl p-8">
            <div class="text-center mb-8">
                <h2 class="text-3xl font-bold bg-gradient-to-r from-purple-600 to-pink-600 bg-clip-text text-transparent">
                    Welcome Back
                </h2>
                <p class="text-gray-600 mt-2">Sign in to your LaptopXplorer account</p>
            </div>

            <form method="post" class="space-y-6">
                {% csrf_token %}
                
                {% if form.errors %}
                <div class="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded-lg">
                    <p class="font-medium">Please correct the errors below.</p>
                </div>
                {% endif %}

                <div>
                    <label for="id_login" class="block text-sm font-medium text-gray-700 mb-2">Email</label>
                    {{ form.login }}
                </div>

                <div>
                    <label for="id_password" class="block text-sm font-medium text-gray-700 mb-2">Password</label>
                    {{ form.password }}
                </div>

                <div class="flex items-center justify-between">
                    <label class="flex items-center">
                        {{ form.remember }}
                        <span class="ml-2 text-sm text-gray-700">Remember me</span>
                    </label>
                    <a href="{% url 'account_reset_password' %}" class="text-sm text-purple-600 hover:text-purple-700">
                        Forgot password?
                    </a>
                </div>

                <button type="submit" class="w-full bg-gradient-to-r from-purple-600 to-pink-600 text-white py-3 rounded-lg hover:from-purple-700 hover:to-pink-700 transition font-semibold">
                    Sign In
                </button>
            </form>

            <div class="relative my-6">
                <div class="absolute inset-0 flex items-center">
                    <div class="w-full border-t border-gray-300"></div>
                </div>
                <div class="relative flex justify-center text-sm">
                    <span class="px-2 bg-white text-gray-500">Or continue with</span>
                </div>
            </div>

            <div class="grid grid-cols-2 gap-3">
                <a href="{% provider_login_url 'google' %}" class="flex items-center justify-center px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50">
                    <i class="fab fa-google text-red-500 mr-2"></i>
                    <span class="text-sm font-medium">Google</span>
                </a>
                <a href="{% provider_login_url 'github' %}" class="flex items-center justify-center px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50">
                    <i class="fab fa-github mr-2"></i>
                    <span class="text-sm font-medium">GitHub</span>
                </a>
            </div>

            <p class="text-center text-sm text-gray-600 mt-6">
                Don't have an account?
                <a href="{% url 'account_signup' %}" class="text-purple-600 hover:text-purple-700 font-semibold">
                    Sign up for free
                </a>
            </p>
        </div>
    </div>
</div>

<style>
input[type="email"], input[type="password"], input[type="text"] {
    @apply w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-600;
}
input[type="checkbox"] {
    @apply w-4 h-4 text-purple-600 border-gray-300 rounded focus:ring-purple-500;
}
</style>
{% endblock %}
```

### 2. src/templates/account/signup.html
```html
{% extends 'base.html' %}

{% block title %}Sign Up - LaptopXplorer{% endblock %}

{% block content %}
<div class="min-h-screen bg-gradient-to-br from-purple-50 to-pink-50 flex items-center justify-center py-12 px-4">
    <div class="max-w-md w-full">
        <div class="bg-white rounded-2xl shadow-2xl p-8">
            <div class="text-center mb-8">
                <h2 class="text-3xl font-bold bg-gradient-to-r from-purple-600 to-pink-600 bg-clip-text text-transparent">
                    Create Account
                </h2>
                <p class="text-gray-600 mt-2">Join LaptopXplorer today</p>
            </div>

            <form method="post" class="space-y-6">
                {% csrf_token %}
                
                {% if form.errors %}
                <div class="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded-lg">
                    <p class="font-medium">Please correct the errors below.</p>
                    {{ form.non_field_errors }}
                </div>
                {% endif %}

                <div>
                    <label for="id_email" class="block text-sm font-medium text-gray-700 mb-2">Email</label>
                    {{ form.email }}
                    {% if form.email.errors %}
                    <p class="text-red-600 text-sm mt-1">{{ form.email.errors.0 }}</p>
                    {% endif %}
                </div>

                <div>
                    <label for="id_password1" class="block text-sm font-medium text-gray-700 mb-2">Password</label>
                    {{ form.password1 }}
                    {% if form.password1.errors %}
                    <p class="text-red-600 text-sm mt-1">{{ form.password1.errors.0 }}</p>
                    {% endif %}
                </div>

                <div>
                    <label for="id_password2" class="block text-sm font-medium text-gray-700 mb-2">Confirm Password</label>
                    {{ form.password2 }}
                    {% if form.password2.errors %}
                    <p class="text-red-600 text-sm mt-1">{{ form.password2.errors.0 }}</p>
                    {% endif %}
                </div>

                <button type="submit" class="w-full bg-gradient-to-r from-purple-600 to-pink-600 text-white py-3 rounded-lg hover:from-purple-700 hover:to-pink-700 transition font-semibold">
                    Create Account
                </button>
            </form>

            <p class="text-center text-sm text-gray-600 mt-6">
                Already have an account?
                <a href="{% url 'account_login' %}" class="text-purple-600 hover:text-purple-700 font-semibold">
                    Sign in
                </a>
            </p>
        </div>
    </div>
</div>

<style>
input[type="email"], input[type="password"] {
    @apply w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-600;
}
</style>
{% endblock %}
```

### 3. src/templates/account/logout.html
```html
{% extends 'base.html' %}

{% block title %}Logout - LaptopXplorer{% endblock %}

{% block content %}
<div class="min-h-screen bg-gradient-to-br from-purple-50 to-pink-50 flex items-center justify-center py-12 px-4">
    <div class="max-w-md w-full">
        <div class="bg-white rounded-2xl shadow-2xl p-8 text-center">
            <i class="fas fa-sign-out-alt text-6xl text-purple-600 mb-4"></i>
            <h2 class="text-2xl font-bold text-gray-900 mb-4">Sign Out</h2>
            <p class="text-gray-600 mb-8">Are you sure you want to sign out?</p>

            <form method="post" class="space-y-4">
                {% csrf_token %}
                <button type="submit" class="w-full bg-gradient-to-r from-purple-600 to-pink-600 text-white py-3 rounded-lg hover:from-purple-700 hover:to-pink-700 transition font-semibold">
                    Yes, Sign Out
                </button>
                <a href="{% url 'core:home' %}" class="block w-full text-center border border-gray-300 text-gray-700 py-3 rounded-lg hover:bg-gray-50 transition font-medium">
                    Cancel
                </a>
            </form>
        </div>
    </div>
</div>
{% endblock %}
```

### 4. src/templates/account/password_reset.html
```html
{% extends 'base.html' %}

{% block title %}Reset Password - LaptopXplorer{% endblock %}

{% block content %}
<div class="min-h-screen bg-gradient-to-br from-purple-50 to-pink-50 flex items-center justify-center py-12 px-4">
    <div class="max-w-md w-full">
        <div class="bg-white rounded-2xl shadow-2xl p-8">
            <div class="text-center mb-8">
                <h2 class="text-3xl font-bold bg-gradient-to-r from-purple-600 to-pink-600 bg-clip-text text-transparent">
                    Reset Password
                </h2>
                <p class="text-gray-600 mt-2">Enter your email to receive reset instructions</p>
            </div>

            <form method="post" class="space-y-6">
                {% csrf_token %}
                
                <div>
                    <label for="id_email" class="block text-sm font-medium text-gray-700 mb-2">Email</label>
                    {{ form.email }}
                </div>

                <button type="submit" class="w-full bg-gradient-to-r from-purple-600 to-pink-600 text-white py-3 rounded-lg hover:from-purple-700 hover:to-pink-700 transition font-semibold">
                    Send Reset Link
                </button>
            </form>

            <p class="text-center text-sm text-gray-600 mt-6">
                Remember your password?
                <a href="{% url 'account_login' %}" class="text-purple-600 hover:text-purple-700 font-semibold">
                    Sign in
                </a>
            </p>
        </div>
    </div>
</div>

<style>
input[type="email"] {
    @apply w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-600;
}
</style>
{% endblock %}
```

## Installation Instructions

1. Run `setup_auth.bat` to install dependencies and create directories
2. Copy the template code above into the corresponding files
3. Run migrations: `python manage.py makemigrations accounts && python manage.py migrate`
4. Start server: `python manage.py runserver`
5. Visit: http://localhost:8000/accounts/login/
