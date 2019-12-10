import time
import pandas as pd
import numpy as np
import datetime

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS = ['All', 'January', 'February', 'March', 'April', 'May', 'June']
DAYS = ['All', 'Monday', 'Tuesday','Wednesday','Thursday','Friday', 'Saturday','Sunday']

# ----------------------------------
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\033[7mBIKESHARE DATA ANALYSIS\033[0m')
    print('\033[1mHello! Let\'s explore some US bikeshare data!\033[0m')
    # get user input for city (chicago, new york city, washington).
    while True:
        cityInput = input("Which city do you like to explore (Chicago, New York City, or Washington)': ").lower()
        if cityInput in CITY_DATA.keys():
            city = cityInput
            break
        else:
            print("\033[31mOops, Please enter one of the three cities!\033[0m")

    while True:
        # get user input for month (all, january, february, ... , june)
        monthInput = input('Now, choose which month (january, february, ... , june) or type "all" for no filters: ').lower().capitalize()
        if monthInput in MONTHS:
            month = monthInput
            break
        else:
            print("\033[31mOops, Please enter a valid month!\033[0m")
    while True:
        # get user input for day of week (all, monday, tuesday, ... sunday)
        dayInput = input('and choose which day (monday, tuesday, ... sunday) or type "all" for no filters: ').lower().capitalize()
        if dayInput in DAYS:
            day = dayInput
            break
        else:
            print("\033[31mOops, Please enter a valid day!\033[0m")

    print('-'*40)
    print('STATISTICS FOR', city.upper(), 'DATA FOR MONTH:', month.upper(), 'AND DAY:', day.upper())
    return city, month, day

# ----------------------------------
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
    
    # convert Start Time column to datetime
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["year"] = df["Start Time"].dt.year
    df["month"] = df["Start Time"].dt.month
    df["day"] = df["Start Time"].dt.weekday_name
    df["hour"] = df["Start Time"].dt.hour

    if month != "All":
        month = MONTHS.index(month)
        df = df[df["month"] == month]

    if day != "All":
        df = df[df["day"] == day]

    return df

# ----------------------------------
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print("\033[1mTIME STATICS\033[0m")
    print('\n\033[92mCalculating The Most Frequent Times of Travel...\n\033[0m')
    start_time = time.time()
    
    
      # display the most common month
    common_month = int(df["month"].mode())
    print("\033[1mMost Common Month: \033[0m", MONTHS[common_month])
    
    # display the most common day of week
    common_day = df["day"].mode()[0]
    print("\033[1mMost Common Day: \033[0m", common_day)


    # display the most common start hour
    common_hour = df["hour"].mode()[0]
    print("\033[1mMost Common Hour: \033[0m", common_hour)

    print("\n\033[92mThis took %s seconds.\033[0m" % (time.time() - start_time))
    print('-'*40)

# ----------------------------------
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print("\033[1mSTATION STATICS\033[0m")
    print('\n\033[92mCalculating The Most Popular Stations and Trip...\n\033[0m')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df["Start Station"].mode()[0]
    print("\033[1mMost commonly used start station: \033[0m", common_start_station)

    # display most commonly used end station
    common_end_station = df["End Station"].mode()[0]
    print("\033[1mMost commonly used end station: \033[0m", common_end_station)

    # display most frequent combination of start station and end station trip
    common_combination = df[['Start Station', 'End Station']].apply(lambda x: '/'.join(x), axis=1)
    common_combination = common_combination.mode()
    common_combination = str(common_combination[0]).split("/")    
    print("\033[1mMost frequent combination of start and end station trip: \033[0m")
    print("\033[1mFrom: \033[0m", common_combination[0], "\n\033[1mTo: \033[0m", common_combination[1])


    print("\n\033[92mThis took %s seconds.\033[0m" % (time.time() - start_time))
    print('-'*40)

# ----------------------------------
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print("\033[1mTRIP DURATION STATICS\033[0m")
    print('\n\033[92mCalculating Trip Duration...\033[0m\n')
    start_time = time.time()

    # display total travel time
    total_travel = df["Trip Duration"].sum()
    print("\033[1mTotal travel time: \033[0m", str(datetime.timedelta(seconds=int(total_travel))))

    # display mean travel time
    mean_travel = df["Trip Duration"].mean()
    print("\033[1mMean travel time: \033[0m", str(datetime.timedelta(seconds=int(mean_travel))))
    
    # display maximum travel time
    max_travel = df["Trip Duration"].max()
    print("\033[1mMaximum travel time: \033[0m", str(datetime.timedelta(seconds=int(max_travel))))
    
    #display minimum travel time
    min_travel = df["Trip Duration"].min()
    print("\033[1mMinimum travel time: \033[0m", str(datetime.timedelta(seconds=int(min_travel))))

    print("\n\033[92mThis took %s seconds.\033[0m" % (time.time() - start_time))
    print('-'*40)

# ----------------------------------
def user_stats(df):
    """Displays statistics on bikeshare users."""
    print("\033[1mUSER STATICS\033[0m")
    print('\n\033[92mCalculating User Stats...\n\033[0m')
    start_time = time.time()

    # Display counts of user types
    user_types = df["User Type"].value_counts().to_frame("")
    print("\033[1mCounts of user types \033[0m", user_types)
    print()

    # Display counts of gender
    if "Gender" in df.columns:
        gender = df["Gender"].value_counts().to_frame("")
        print("\033[1mCounts of gender \033[0m", gender)
        print()

    # Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
        earliest_birth = int(df["Birth Year"].min())
        recent_birth = int(df["Birth Year"].max())
        common_birth = int(df["Birth Year"].mode()[0])
        print("\033[1mThe earliest birth year: \033[0m", earliest_birth)
        print("\033[1mThe most recent birth year: \033[0m", recent_birth)
        print("\033[1mThe most common birth year: \033[0m", common_birth)
    
    print("\n\033[92mThis took %s seconds.\033[0m" % (time.time() - start_time))
    print('-'*40)

# ----------------------------------
def table_states(df):
    """Displays statistics on bikeshare tables."""
    print("\033[1mTABLE STATICS\033[0m")
    print('\n\033[92mCalculating Dataset Stats...\n\033[0m')
    start_time = time.time()

    # count number of rows 
    print("\033[1mThis table has\033[0m",len(df.index),"\033[1mdata entries.\033[0m")

    # display columns
    print("\033[1mThe columns inclue: \033[0m")
    for col in df.columns:
        print(col)

    # get year(s) of data 
    years = df["year"].value_counts().index.tolist()
    print("\033[1mEntries are in year(s): \033[0m", years)

    raw_data = input('\n\033[1mDo you wish to view the first five raw data of this table?\033]0m')
    if raw_data.lower() == "yes":
        print(df.iloc[:5])

    print("\n\033[92mThis took %s seconds.\033[0m" % (time.time() - start_time))
    print('-'*40)

# ----------------------------------
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        table_states(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\n\033[1mWould you like to restart? Enter yes or no.\n\033[0m')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
