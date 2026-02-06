"""
Script to create authentication templates automatically
Run: python create_auth_templates.py
"""
import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).parent / 'src' / 'templates'

# Create directories
(BASE_DIR / 'account').mkdir(exist_ok=True)
(BASE_DIR / 'accounts').mkdir(exist_ok=True)

print("✅ Created template directories")

# Template files
TEMPLATES = {
    'account/login.html': '''{% extends 'base.html' %}
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
                    <p class="font-medium">Please check your credentials and try again.</p>
                </div>
                {% endif %}

                <div>
                    <label for="id_login" class="block text-sm font-medium text-gray-700 mb-2">Email</label>
                    <input type="email" name="login" id="id_login" required class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-600" placeholder="you@example.com">
                </div>

                <div>
                    <label for="id_password" class="block text-sm font-medium text-gray-700 mb-2">Password</label>
                    <input type="password" name="password" id="id_password" required class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-600" placeholder="••••••••">
                </div>

                <div class="flex items-center justify-between">
                    <label class="flex items-center">
                        <input type="checkbox" name="remember" class="w-4 h-4 text-purple-600 border-gray-300 rounded focus:ring-purple-500">
                        <span class="ml-2 text-sm text-gray-700">Remember me</span>
                    </label>
                    <a href="{% url 'account_reset_password' %}" class="text-sm text-purple-600 hover:text-purple-700">
                        Forgot password?
                    </a>
                </div>

                <button type="submit" class="w-full bg-gradient-to-r from-purple-600 to-pink-600 text-white py-3 rounded-lg hover:from-purple-700 hover:to-pink-700 transition font-semibold shadow-lg">
                    <i class="fas fa-sign-in-alt mr-2"></i>Sign In
                </button>
            </form>

            <p class="text-center text-sm text-gray-600 mt-6">
                Don't have an account?
                <a href="{% url 'account_signup' %}" class="text-purple-600 hover:text-purple-700 font-semibold">
                    Sign up for free
                </a>
            </p>
        </div>
    </div>
</div>
{% endblock %}
''',

    'account/signup.html': '''{% extends 'base.html' %}

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
                    <ul class="list-disc list-inside text-sm">
                    {% for field, errors in form.errors.items %}
                        {% for error in errors %}
                        <li>{{ error }}</li>
                        {% endfor %}
                    {% endfor %}
                    </ul>
                </div>
                {% endif %}

                <div>
                    <label for="id_email" class="block text-sm font-medium text-gray-700 mb-2">Email</label>
                    <input type="email" name="email" id="id_email" required class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-600" placeholder="you@example.com">
                </div>

                <div>
                    <label for="id_password1" class="block text-sm font-medium text-gray-700 mb-2">Password</label>
                    <input type="password" name="password1" id="id_password1" required class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-600" placeholder="••••••••">
                    <p class="text-xs text-gray-500 mt-1">Minimum 8 characters</p>
                </div>

                <div>
                    <label for="id_password2" class="block text-sm font-medium text-gray-700 mb-2">Confirm Password</label>
                    <input type="password" name="password2" id="id_password2" required class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-600" placeholder="••••••••">
                </div>

                <button type="submit" class="w-full bg-gradient-to-r from-purple-600 to-pink-600 text-white py-3 rounded-lg hover:from-purple-700 hover:to-pink-700 transition font-semibold shadow-lg">
                    <i class="fas fa-user-plus mr-2"></i>Create Account
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
{% endblock %}
''',

    'account/logout.html': '''{% extends 'base.html' %}

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
                <a href="/" class="block w-full text-center border border-gray-300 text-gray-700 py-3 rounded-lg hover:bg-gray-50 transition font-medium">
                    Cancel
                </a>
            </form>
        </div>
    </div>
</div>
{% endblock %}
''',

    'account/password_reset.html': '''{% extends 'base.html' %}

{% block title %}Reset Password - LaptopXplorer{% endblock %}

{% block content %}
<div class="min-h-screen bg-gradient-to-br from-purple-50 to-pink-50 flex items-center justify-center py-12 px-4">
    <div class="max-w-md w-full">
        <div class="bg-white rounded-2xl shadow-2xl p-8">
            <div class="text-center mb-8">
                <i class="fas fa-key text-5xl text-purple-600 mb-4"></i>
                <h2 class="text-3xl font-bold bg-gradient-to-r from-purple-600 to-pink-600 bg-clip-text text-transparent">
                    Reset Password
                </h2>
                <p class="text-gray-600 mt-2">Enter your email to receive reset instructions</p>
            </div>

            <form method="post" class="space-y-6">
                {% csrf_token %}
                
                <div>
                    <label for="id_email" class="block text-sm font-medium text-gray-700 mb-2">Email</label>
                    <input type="email" name="email" id="id_email" required class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-600" placeholder="you@example.com">
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
{% endblock %}
'''
}

# Create template files
for filepath, content in TEMPLATES.items():
    full_path = BASE_DIR / filepath
    full_path.write_text(content, encoding='utf-8')
    print(f"✅ Created {filepath}")

print("\n========================================")
print("✅ All authentication templates created!")
print("========================================")
print("\nNext steps:")
print("1. Run: cd src")
print("2. Run: python manage.py makemigrations accounts")
print("3. Run: python manage.py migrate")
print("4. Run: python manage.py runserver")
print("5. Visit: http://localhost:8000/accounts/login/")
