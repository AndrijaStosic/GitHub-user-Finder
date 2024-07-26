import tkinter as tk
from tkinter import messagebox
import requests


def get_github_info(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def show_info():
    username = entry.get()
    user_info = get_github_info(username)
    repos_info = get_repos(username)
    
    if user_info:
        user_text = f"Username: {user_info['login']}\n"
        user_text += f"Name: {user_info['name']}\n"
        user_text += f"Bio: {user_info['bio']}\n"
        user_text += f"Public Repos: {user_info['public_repos']}\n"
        user_text += f"Followers: {user_info['followers']}\n"
        user_text += f"Following: {user_info['following']}\n"
        
        repo_text = "\nRepositories:\n"
        for repo in repos_info:
            repo_text += f"- {repo['name']}: {repo['description']}\n"
        
        info_label.config(text=user_text + repo_text)
    else:
        messagebox.showerror("Error", "User not found")


root = tk.Tk()
root.title("GitHub User Info")


tk.Label(root, text="Enter GitHub username:").pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=5)
tk.Button(root, text="Get Info", command=show_info).pack(pady=10)

info_label = tk.Label(root, text="", justify=tk.LEFT)
info_label.pack(pady=10)


root.mainloop()