import weather
import tkinter as tk
from tkinter import messagebox

def get_weather():
    city_name = city.get().strip()
    if not city_name:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    data = weather.fetch_weather(city_name)

    if data.get("cod") != 200:
        error_msg = data.get("message", "Unknown error occurred.")
        messagebox.showerror("Error", f"City not found or error: {error_msg}")
        return

    try:
        selection = selected_option.get()

        if selection == "Temperature":
            temp = data['main']['temp']
            messagebox.showinfo("Temperature", f"Temperature in {city_name}: {temp}°C")

        elif selection == "Description":
            description = data['weather'][0]['description']
            messagebox.showinfo("Description", f"Weather in {city_name}: {description}")

        elif selection == "City Code":
            city_id = data['id']
            messagebox.showinfo("City Code", f"City Code for {city_name}: {city_id}")

        elif selection == "All":
            temp = data['main']['temp']
            description = data['weather'][0]['description']
            city_id = data['id']
            messagebox.showinfo("Weather Info",
                f"City: {city_name}\nTemperature: {temp}°C\nDescription: {description}\nCity Code: {city_id}")

        else:
            messagebox.showwarning("Selection Error", "Please select a valid option.")

    except Exception as e:
        messagebox.showerror("Error", f"Could not fetch all data.\nDetails: {e}")

# GUI setup
root = tk.Tk()
root.title("Weather App")
root.geometry("300x250")

tk.Label(root, text="Enter the name of the city:").pack(pady=5)
city = tk.Entry(root)
city.pack()

# Dropdown for user selection
options = ["Temperature", "Description", "City Code", "All"]
selected_option = tk.StringVar()
selected_option.set(options[0])  # default value

tk.Label(root, text="Select what you want to see:").pack(pady=5)
tk.OptionMenu(root, selected_option, *options).pack()

tk.Button(root, text="Get Weather", command=get_weather).pack(pady=20)

root.mainloop()