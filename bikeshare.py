import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
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
    print('Would you like to see data for Chicago, New York, or Washington?')
    cities = ['chicago', 'new york', 'washington']
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    days = ['monday', 'tuesday','wednesday', 'thursday', 'friday','saturday', 'sunday', 'all']


    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Which city do you want to explore Chicago, New York or Washington? \n> ').lower()
        if city not in cities:
            print('Oops! invalid input')
            continue
        else:
          break





    # TO DO: get user input for month (all, january, february, ... , june)


    while True:
        month = input('Please input the month you will like to filter \n>').lower()
        if month not in months:
            print('invalid input please enter january, february, march, april or june')
            continue
        else:
            break



    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Which day will you like to see - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday \n>').lower()

        if day not in days:
            print('oops! please enter a valid input from Monday to sunday or all')

        else:
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['week_day'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['week_day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month =  df['month'].mode()[0]
    print('Most common month is {}'.format(most_common_month))



    # TO DO: display the most common day of week
    most_common_day = df['week_day'].mode()[0]
    print('Most common day of the week is {}'.format(most_common_day))




    # TO DO: display the most common start hour
    most_common_hour =  df['hour'].mode()[0]
    print('Most common hour is {}'.format(most_common_hour))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_used_start_station = df['Start Station'].mode()[0]
    print('Most used start station is {}'.format(most_used_start_station))
    # TO DO: display most commonly used end station
    most_used_end_station = df['End Station'].mode()[0]
    print('Most used end station is {}'.format(most_used_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_start_end_station = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print('Most used start end station combination is {}'.format(most_frequent_start_end_station))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    trip_duration =  df['Trip Duration'].sum()
    print('Total trip duration is {}'.format(trip_duration))


    # TO DO: display mean travel time
    mean_time_travel =  df['Trip Duration'].mean()
    print('The mean time travel is {}'.format(mean_time_travel))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)


    # TO DO: Display counts of gender
    if 'Gender'not in df.columns:
        print('Gender data is not available')
    else:
        gender = df['Gender'].value_counts()
        print(gender)



    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' not in df.columns:
        print('Birth Year data is not available')
    else:

        earliest_birth_year = df['Birth Year'].min()
        print('Earliest birth year is {}'.format(earliest_birth_year))
        most_recent_birth_year = df['Birth Year'].max()
        print('Most recent birth year is {}'.format(most_recent_birth_year))
        most_common_birth_year = df['Birth Year'].mode()[0]
        print('Most common birth year is {}'.format(most_common_birth_year))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    start = 0
    while True:
        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
        if view_data.lower() == 'yes':
            print(df[start:start+5])
            start += 5
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
