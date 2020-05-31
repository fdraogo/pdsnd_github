import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    #Getting user input for city (new york city, chicago, washington)
    while True:
      city = input("\nWhich city would you like to see the data for?\n").lower()
      if city in ('new york city', 'washington', 'chicago'):
         break
      else:
      # Requesting that "Invalid Input" be returned if not the city listed.
         print("Invalid Input")
    time_frame = input("\nWould you like to filter the data by month, day or none\n").lower()
    month = 'all'
    day = 'all'
    if time_frame == 'month':
       # Getting user input for month (january, February, march, april, may, june)
       while True:
         month = input("\nWhich month data would you like to look at?\n").lower()
         if month in ('january', 'february', 'march', 'april', 'may', 'june'):
           break
         else:
           print("Please input the fullname of the month")
    elif time_frame == 'day':
        #Getting user input for day of the week (Sunday = 1, Monday = 2, ...)
        while True:
          day = int(input("\nWhich day? Please type your response as an integer (e.g, 1 = Sunday)\n"))
          days = [1, 2, 3, 4, 5, 6, 7]
          if day in days:
            break
          else:
            print("Invalid response. Please enter enteger values from 1 to 7")
    print('-'*40)
    return city, month, day

def load_data(city, month, day):
  df = pd.read_csv(CITY_DATA[city])
  df['Start Time'] = pd.to_datetime(df['Start Time'])
  df['month'] = df['Start Time'].dt.month
  df['day_of_week'] = df['Start Time'].dt.weekday
  if month != 'all':
     months = ['january', 'february', 'march', 'april', 'may', 'june']
     month = months.index(month) +1
     df = df[df['month'] == month]
  if day != 'all':
     days = [1, 2, 3, 4, 5, 6, 7]
     day = days.index(day)
     df = df[df['day_of_week'] == day]
  return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #Displaying the most common month
    popular_month = df['month'].mode()[0]
    print('Most Common Month:', popular_month)

    #Displaying the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Common day:', popular_day)

    #Displaying the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Common Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #Displaying most commonly used start station
    Start_Station = df['Start Station'].value_counts().idxmax()
    print('Most Commonly used start station:', Start_Station)

    #Displaying most commonly used end station
    End_Station = df['End Station'].value_counts().idxmax()
    print('\nMost Commonly used end station:', End_Station)

    #Displaying most frequent combination of start station and end station trip
    Combination_Station = df.groupby(['Start Station', 'End Station']).count()
    print('\nMost Commonly used combination of start station and end station trip:', Start_Station, " & ", End_Station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #Displaying total travel time
    Total_Travel_Time = sum(df['Trip Duration'])
    print('Total travel time:', Total_Travel_Time/86400, " Days")

    #Displaying mean travel time
    Mean_Travel_Time = df['Trip Duration'].mean()
    print('Mean travel time:', Mean_Travel_Time/60, " Minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #Displaying counts of user types
    user_types = df['User Type'].value_counts()
    print('User Types:\n', user_types)

    #Displaying counts of gender
    try:
      gender_types = df['Gender'].value_counts()
      print('\nGender Types:\n', gender_types)
    except KeyError:
      print("\nGender Types:\nNo data available for this month.")

    #Displaying earliest, most recent, and most common year of birth
    try:
      Earliest_Year = df['Birth Year'].min()
      print('\nEarliest Year:', Earliest_Year)
    except KeyError:
      print("\nEarliest Year:\nNo data available for this month.")

    try:
      Most_Recent_Year = df['Birth Year'].max()
      print('\nMost Recent Year:', Most_Recent_Year)
    except KeyError:
      print("\nMost Recent Year:\nNo data available for this month.")

    try:
      Most_Common_Year = df['Birth Year'].value_counts().idxmax()
      print('\nMost Common Year:', Most_Common_Year)
    except KeyError:
      print("\nMost Common Year:\nNo data available for this month.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
