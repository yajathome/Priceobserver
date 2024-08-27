import streamlit as st
def fo():    
    def get_city(state):
        state_to_city = {
            "Andhra Pradesh": "Visakhapatnam",
            "Tamil Nadu": "Chennai",
            "Kerala": "Thiruvananthapuram",
            "Karnataka": "Bangalore",
        }
        return state_to_city.get(state, state)
    def get_weather(city, api_key):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_description = data['weather'][0]['description']
            temperature_fahrenheit = data['main']['temp']
            temperature_celsius = int((temperature_fahrenheit - 32) * 0.5555555)
            weather_info = f"The weather in {city} is currently {weather_description} with a temperature of {temperature_celsius}°C."
            return weather_info, temperature_celsius
        else:
            return "Sorry, I couldn't get the weather information. Please try again later.", None
    def get_crop_recommendation(month, terrain, temperature_celsius):
        month = month.lower()
        terrain = terrain.lower()
        if month in ["march", "april"] and terrain in ["plain", "plateau"]:
            return "The conditions are suitable for planting zaid crops."
        elif month in ["october", "december"]:
            if terrain == "plain" and 25 < temperature_celsius < 30:
                return "The conditions are suitable for successfully planting rabi crops."
            elif terrain == "plateau" and 25 < temperature_celsius < 30:
                return "You can plant rabi crops, but you should take extremely good care."
            elif terrain == "mountain" and 25 < temperature_celsius < 30:
                return "It is going to be very hard to farm."
            else:
                return "The conditions are not suitable for planting rabi crops."
        elif month in ["september", "october"]:
            if terrain == "plain" and 20 < temperature_celsius < 25:
                return "The conditions are suitable for successfully planting kharif crops, and the plain terrain makes it easier."
            elif terrain == "plateau" and 20 < temperature_celsius < 25:
                return "You can plant kharif crops, but it would take effort."
            elif terrain == "mountain" and 20 < temperature_celsius < 25:
                return "The conditions are good for planting kharif crops, but it is going to be very hard to farm."
            else:
                return "The conditions are not suitable for planting kharif crops."
        else:
            return "The current month is not suitable for planting either rabi or kharif crops based on the given conditions."
    def main():
        st.title("Crop Recommendation Based on Weather and Terrain")
        st.write(" ")
        st.write("Enter the details below to get crop recommendations based on the weather and terrain conditions.")
        state = st.selectbox("Select your state:", ["Andhra Pradesh", "Tamil Nadu", "Kerala", "Karnataka"])
        terrain = st.selectbox("Select your terrain:", ["Plain", "Plateau", "Mountain"])
        month = st.selectbox("Select the month:", ["March", "April", "September", "October", "November", "December"])
    
        if st.button("Get Recommendation"):
            api_key = "5cfb38f8a25bdae00a1f5984e6644063"
            city = get_city(state)
            weather_info, temperature_celsius = get_weather(city, api_key)
            if temperature_celsius is not None:
                crop_info = get_crop_recommendation(month, terrain, temperature_celsius)
                st.success(f"Weather Info: {weather_info}")
                st.success(f"Crop Recommendation: {crop_info}")
            else:
                st.error("Could not retrieve weather information.")
    if __name__ == "__main__":
        main()
fo()
st.write("farm_data = {
            'Farm Name': ['Farm A', 'Farm B', 'Farm C'],
            'Location': ['Location A', 'Location B', 'Location C'],
            'Crop': ['Wheat', 'Corn', 'Soybean'],
            'Livestock': ['Cattle', 'Pigs', 'Chickens'],
            'Area (acres)': [100, 200, 150],
            'Livestock Count': [50, 200, 150],
            'Feeding Schedule': ['Twice a day', 'Three times a day', 'Once a day'],
            'Health Status': ['Good', 'Excellent', 'Fair']
        }
# Initialize the session state if it doesn't already exist
        if 'df' not in st.session_state:
            st.session_state.df = pd.DataFrame(farm_data)
        def main():
            st.title('Farm Management App')
            st.write(" ")
    # Sidebar with options
            st.sidebar.title('Menu')
            page = st.sidebar.radio('Select a page', ['Home', 'Crop Management', 'Livestock Tracking', 'Tasks'])
            df = st.session_state.df
            if page == 'Home':
                st.subheader('Farm Overview')
                st.write(" ")
                st.write(df)  # Display farm data
            elif page == 'Crop Management':
                st.subheader('Crop Management')
                st.write(" ")
                st.write('Select a crop to manage:')
                selected_crop = st.selectbox('Select Crop', df['Crop'].unique())
                crop_info = df[df['Crop'] == selected_crop].iloc[0]
                st.write(f"*Crop Name:* {crop_info['Crop']}")
                st.write(f"*Farm Name:* {crop_info['Farm Name']}")
                st.write(f"*Location:* {crop_info['Location']}")
                st.write(f"*Area (acres):* {crop_info['Area (acres)']}")
            elif page == 'Livestock Tracking':
                st.subheader('Livestock Tracking')
                st.write(" ")
                st.write('Select a livestock to track:')
                selected_livestock = st.selectbox('Select Livestock', df['Livestock'].unique())
                livestock_info = df[df['Livestock'] == selected_livestock].iloc[0]
                st.write(f"*Livestock Type:* {livestock_info['Livestock']}")
                st.write(f"*Farm Name:* {livestock_info['Farm Name']}")
                st.write(f"*Location:* {livestock_info['Location']}")
                st.write(f"*Area (acres):* {livestock_info['Area (acres)']}")
                st.write(f"*Livestock Count:* {livestock_info['Livestock Count']}")
                st.write(f"*Feeding Schedule:* {livestock_info['Feeding Schedule']}")
                st.write(f"*Health Status:* {livestock_info['Health Status']}")
                new_health_status = st.selectbox('Change Health Status', ['Good', 'Fair', 'Poor', 'Excellent'], 
                                                 index=['Good', 'Fair', 'Poor', 'Excellent'].index(livestock_info['Health Status']))
                if st.button('Update Health Status'):
                    df.loc[df['Livestock'] == selected_livestock, 'Health Status'] = new_health_status
                    st.session_state.df = df  # Update session state
                    st.write(f"Health status of {selected_livestock} updated to {new_health_status}")
                    livestock_info = df[df['Livestock'] == selected_livestock].iloc[0]
                    st.write(f"*Health Status:* {livestock_info['Health Status']}")
            elif page == 'Tasks':
                st.subheader('Task Management')
                st.write(" ")
                st.write('Manage your farm tasks here.')
                task = st.text_area('Enter a new task')
                if st.button('Add Task'):
                    st.write(f'New task added: {task}')
        if __name__ == '__main__':
            main()")
