# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 23:45:45 2021

@author: hp
"""

import pandas as pd
import numpy as np
hb=pd.read_csv('C:/Users/hp/Desktop/HB.csv')
hb.head()
hb.columns
reservation_status=[]
for i in (hb['reservation_status']):
    if i == 'Canceled':
        x=0
    if i == 'Check-Out':
        x=1
    if i == 'No-Show':
        x=2
    reservation_status.append(x)
hb['reservation_status']=pd.Series(reservation_status)
bivariate=[]
bins=[10,20,30,40,50,60,70,80,90,100]
for i in bins:
    pp=np.percentile(hb['total_of_special_requests'],i)
    bivariate.append(pp)
band_lead_time=[]
for i in (hb['lead_time']):
    if i>0 and i<3:
        x='0.0 to 3'
    if i > 3 and i < 11:
        x= '1.3 to 11'
    if i > 11 and i < 26:
        x = '2.11 to 26'
    if i > 26 and i < 45:
        x = '3.26 to 45'
    if i > 45 and i < 69:
        x = '4.45 to 69'
    if i > 69 and i < 99:
        x = '5.69 to 99'
    if i > 99 and i < 138:
        x = '6.99 to 138'
    if i > 138 and i < 184:
        x = '7.138 to 184'
    if i > 184 and i < 265:
        x = '8.184 to 265'
    if i > 265 and i < 737:
        x = '9.265 to 737'
    band_lead_time.append(x)
hb['band_lead_time']=pd.Series(band_lead_time)
hb['band_lead_time']=pd.Series(band_lead_time)
cnt=hb.groupby('band_lead_time')['reservation_status'].count()
churn_rate=hb.groupby('band_lead_time')['reservation_status'].mean()
cnt.to_csv('C:/Users/hp/Desktop/hb/band_lead_time_count.csv')
churn_rate.to_csv('C:/Users/hp/Desktop/hb/band_lead_time_churn_rate.csv')
band_adr=[]
for i in (hb['adr']):
    if i>0 and i<50:
        x='0.0 to 50'
    if i > 50 and i < 64:
        x= '1.50 to 64'
    if i > 64 and i < 75:
        x = '2.64 to 75'
    if i > 75 and i < 85:
        x = '3.75 to 85'
    if i > 85 and i < 94.575:
        x = '4.85 to 94.575'
    if i > 94.575 and i < 105.0:
        x = '5.94.575 to 105.0'
    if i > 105.0 and i < 118.15:
        x = '6.105.0 to 118.15'
    if i > 118.15 and i < 135.0:
        x = '7.118.15 to 135.0'
    if i > 135.0 and i < 164.0:
        x = '8.135 to 164.0'
    if i > 164.0 and i < 5400.0:
        x = '9.164.0 to 5400.0'
    band_adr.append(x)
hb['band_adr']=pd.Series(band_adr)
hb['band_adr']=pd.Series(band_adr)
cnt=hb.groupby('band_adr')['reservation_status'].count()
churn_rate=hb.groupby('band_adr')['reservation_status'].mean()
cnt.to_csv('C:/Users/hp/Desktop/hb/band_adr_count.csv')
churn_rate.to_csv('C:/Users/hp/Desktop/hb/band_adr_churn_rate.csv')


cnt=hb.groupby('hotel')['reservation_status'].count()
churn_rate=hb.groupby('hotel')['reservation_status'].mean()
cnt.to_csv('C:/Users/hp/Desktop/HB/hotel_count.csv')
churn_rate.to_csv('C:/Users/hp/Desktop/HB/hotel_churn_rate.csv')
cnt=hb.groupby('is_canceled')['reservation_status'].count()
churn_rate=hb.groupby('is_canceled')['reservation_status'].mean()
cnt.to_csv('C:/Users/hp/Desktop/HB/is_canceled_count.csv')
churn_rate.to_csv('C:/Users/hp/Desktop/HB/is_canceled_churn_rate.csv')
cnt=hb.groupby('arrival_date_year')['reservation_status'].count()
churn_rate=hb.groupby('arrival_date_year')['reservation_status'].mean()
cnt.to_csv('C:/Users/hp/Desktop/HB/arrival_date_year_count.csv')
churn_rate.to_csv('C:/Users/hp/Desktop/HB/arrival_date_year_churn_rate.csv')
cnt=hb.groupby('arrival_date_month')['reservation_status'].count()
churn_rate=hb.groupby('arrival_date_month')['reservation_status'].mean()
cnt.to_csv('C:/Users/hp/Desktop/HB/arrival_date_month_count.csv')
churn_rate.to_csv('C:/Users/hp/Desktop/HB/arrival_date_month_churn_rate.csv')
cnt=hb.groupby('arrival_date_week_number')['reservation_status'].count()
churn_rate=hb.groupby('arrival_date_week_number')['reservation_status'].mean()
cnt.to_csv('C:/Users/hp/Desktop/HB/arrival_date_week_number_count.csv')
churn_rate.to_csv('C:/Users/hp/Desktop/HB/arrival_date_week_number_churn_rate.csv')
cnt=hb.groupby('arrival_date_day_of_month')['reservation_status'].count()
churn_rate=hb.groupby('arrival_date_day_of_month')['reservation_status'].mean()
cnt.to_csv('C:/Users/hp/Desktop/HB/arrival_date_day_of_month_count.csv')
churn_rate.to_csv('C:/Users/hp/Desktop/HB/arrival_date_day_of_monthl_churn_rate.csv')
cnt=hb.groupby('arrival_date_day_of_month')['reservation_status'].count()
churn_rate=hb.groupby('arrival_date_day_of_month')['reservation_status'].mean()
cnt.to_csv('C:/Users/hp/Desktop/HB/arrival_date_day_of_month_count.csv')
churn_rate.to_csv('C:/Users/hp/Desktop/HB/arrival_date_day_of_monthl_churn_rate.csv')
cnt=hb.groupby('stays_in_weekend_nights')['reservation_status'].count()
churn_rate=hb.groupby('stays_in_weekend_nights')['reservation_status'].mean()
cnt.to_csv('C:/Users/hp/Desktop/HB/stays_in_weekend_nights_count.csv')
churn_rate.to_csv('C:/Users/hp/Desktop/HB/stays_in_weekend_nights_churn_rate.csv')
cnt=hb.groupby('stays_in_week_nights')['reservation_status'].count()
churn_rate=hb.groupby('stays_in_week_nights')['reservation_status'].mean()
cnt.to_csv('C:/Users/hp/Desktop/HB/stays_in_week_nights_count.csv')
churn_rate.to_csv('C:/Users/hp/Desktop/HB/stays_in_week_nights_churn_rate.csv')
cnt=hb.groupby('adults')['reservation_status'].count()
churn_rate=hb.groupby('adults')['reservation_status'].mean()
cnt.to_csv('C:/Users/hp/Desktop/hb/adults_count.csv')
churn_rate.to_csv('C:/Users/hp/Desktop/hb/adults_churn_rate.csv')
cnt=hb.groupby('children')['reservation_status'].count()
churn_rate=hb.groupby('children')['reservation_status'].mean()
cnt.to_csv('C:/Users/hp/Desktop/hb/children_count.csv')
churn_rate.to_csv('C:/Users/hp/Desktop/hb/children_churn_rate.csv')
cnt=hb.groupby('babies')['reservation_status'].count()
churn_rate=hb.groupby('babies')['reservation_status'].mean()
cnt.to_csv('C:/Users/hp/Desktop/hb/babies_count.csv')
churn_rate.to_csv('C:/Users/hp/Desktop/hb/babies_churn_rate.csv')
cnt=hb.groupby('meal')['reservation_status'].count()
churn_rate=hb.groupby('meal')['reservation_status'].mean()
cnt.to_csv('C:/Users/hp/Desktop/hb/meal_count.csv')
churn_rate.to_csv('C:/Users/hp/Desktop/hb/meal_churn_rate.csv')
cnt=hb.groupby('country')['reservation_status'].count()
churn_rate=hb.groupby('country')['reservation_status'].mean()
cnt.to_csv('C:/Users/hp/Desktop/hb/country_count.csv')
churn_rate.to_csv('C:/Users/hp/Desktop/hb/country_churn_rate.csv')
cnt=hb.groupby('market_segment')['reservation_status'].count()
churn_rate=hb.groupby('market_segment')['reservation_status'].mean()
cnt.to_csv('C:/Users/hp/Desktop/hb/market_segment_count.csv')
churn_rate.to_csv('C:/Users/hp/Desktop/hb/market_segment_churn_rate.csv')
cnt=hb.groupby('distribution_channel')['reservation_status'].count()
churn_rate=hb.groupby('distribution_channel')['reservation_status'].mean()
cnt.to_csv('C:/Users/hp/Desktop/hb/distribution_channel_count.csv')
churn_rate.to_csv('C:/Users/hp/Desktop/hb/distribution_channel_churn_rate.csv')
cnt=hb.groupby('is_repeated_guest')['reservation_status'].count()
churn_rate=hb.groupby('is_repeated_guest')['reservation_status'].mean()
cnt.to_csv('C:/Users/hp/Desktop/hb/is_repeated_guest_count.csv')
churn_rate.to_csv('C:/Users/hp/Desktop/hb/is_repeated_guest_churn_rate.csv')
cnt=hb.groupby('previous_cancellations')['reservation_status'].count()
churn_rate=hb.groupby('previous_cancellations')['reservation_status'].mean()
cnt.to_csv('C:/Users/hp/Desktop/hb/previous_cancellations_count.csv')
churn_rate.to_csv('C:/Users/hp/Desktop/hb/previous_cancellations_churn_rate.csv')
cnt=hb.groupby('previous_bookings_not_canceled')['reservation_status'].count()
churn_rate=hb.groupby('previous_bookings_not_canceled')['reservation_status'].mean()
cnt.to_csv('C:/Users/hp/Desktop/hb/previous_bookings_not_canceled_count.csv')
churn_rate.to_csv('C:/Users/hp/Desktop/hb/previous_bookings_not_canceled_churn_rate.csv')
cnt=hb.groupby('reserved_room_type')['reservation_status'].count()
churn_rate=hb.groupby('reserved_room_type')['reservation_status'].mean()
cnt.to_csv('C:/Users/hp/Desktop/hb/reserved_room_type_count.csv')
churn_rate.to_csv('C:/Users/hp/Desktop/hb/reserved_room_type_churn_rate.csv')
cnt=hb.groupby('assigned_room_type')['reservation_status'].count()
churn_rate=hb.groupby('assigned_room_type')['reservation_status'].mean()
cnt.to_csv('C:/Users/hp/Desktop/hb/assigned_room_type_count.csv')
churn_rate.to_csv('C:/Users/hp/Desktop/hb/assigned_room_type_churn_rate.csv')
cnt=hb.groupby('booking_changes')['reservation_status'].count()
churn_rate=hb.groupby('booking_changes')['reservation_status'].mean()
cnt.to_csv('C:/Users/hp/Desktop/hb/booking_changes_count.csv')
churn_rate.to_csv('C:/Users/hp/Desktop/hb/booking_changes_churn_rate.csv')
cnt=hb.groupby('deposit_type')['reservation_status'].count()
churn_rate=hb.groupby('deposit_type')['reservation_status'].mean()
cnt.to_csv('C:/Users/hp/Desktop/hb/deposit_type_count.csv')
churn_rate.to_csv('C:/Users/hp/Desktop/hb/deposit_type_churn_rate.csv')
cnt=hb.groupby('agent')['reservation_status'].count()
churn_rate=hb.groupby('agent')['reservation_status'].mean()
cnt.to_csv('C:/Users/hp/Desktop/hb/agent_count.csv')
churn_rate.to_csv('C:/Users/hp/Desktop/hb/agent_churn_rate.csv')
cnt=hb.groupby('company')['reservation_status'].count()
churn_rate=hb.groupby('company')['reservation_status'].mean()
cnt.to_csv('C:/Users/hp/Desktop/hb/company_count.csv')
churn_rate.to_csv('C:/Users/hp/Desktop/hb/company_churn_rate.csv')
cnt=hb.groupby('days_in_waiting_list')['reservation_status'].count()
churn_rate=hb.groupby('days_in_waiting_list')['reservation_status'].mean()
cnt.to_csv('C:/Users/hp/Desktop/hb/days_in_waiting_list_count.csv')
churn_rate.to_csv('C:/Users/hp/Desktop/hb/days_in_waiting_list_churn_rate.csv')
cnt=hb.groupby('customer_type')['reservation_status'].count()
churn_rate=hb.groupby('customer_type')['reservation_status'].mean()
cnt.to_csv('C:/Users/hp/Desktop/hb/customer_type_count.csv')
churn_rate.to_csv('C:/Users/hp/Desktop/hb/customer_type_churn_rate.csv')
cnt=hb.groupby('required_car_parking_spaces')['reservation_status'].count()
churn_rate=hb.groupby('required_car_parking_spaces')['reservation_status'].mean()
cnt.to_csv('C:/Users/hp/Desktop/hb/required_car_parking_spaces_count.csv')
churn_rate.to_csv('C:/Users/hp/Desktop/hb/required_car_parking_spaces_churn_rate.csv')
cnt=hb.groupby('required_car_parking_spaces')['reservation_status'].count()
churn_rate=hb.groupby('required_car_parking_spaces')['reservation_status'].mean()
cnt.to_csv('C:/Users/hp/Desktop/hb/required_car_parking_spaces_count.csv')
churn_rate.to_csv('C:/Users/hp/Desktop/hb/required_car_parking_spaces_churn_rate.csv')
cnt=hb.groupby('total_of_special_requests')['reservation_status'].count()
churn_rate=hb.groupby('total_of_special_requests')['reservation_status'].mean()
cnt.to_csv('C:/Users/hp/Desktop/hb/total_of_special_requests_count.csv')
churn_rate.to_csv('C:/Users/hp/Desktop/hb/total_of_special_requests_churn_rate.csv')
cnt=hb.groupby('reservation_status')['reservation_status'].count()
churn_rate=hb.groupby('reservation_status')['reservation_status'].mean()
cnt.to_csv('C:/Users/hp/Desktop/hb/reservation_status_count.csv')
        churn_rate.to_csv('C:/Users/hp/Desktop/hb/reservation_status_churn_rate.csv')
cnt=hb.groupby('reservation_status_date')['reservation_status'].count()
churn_rate=hb.groupby('reservation_status_date')['reservation_status'].mean()
cnt.to_csv('C:/Users/hp/Desktop/hb/reservation_status_date_count.csv')
churn_rate.to_csv('C:/Users/hp/Desktop/hb/reservation_status_date_churn_rate.csv')


band_previous_bookings_not_canceled_coarse=[]
for i in (hb['previous_bookings_not_canceled']):
    if i > 0 and i < 50000:
        x='0.0 to 50000'
    if i > 50000 and i < 100000:
        x = '1.50000 to 100000'
    if i > 100000 and i < 150000:
        x = '1.100000 to 150000'
    band_previous_bookings_not_canceled_coarse.append(x)
hb['band_previous_bookings_not_canceled_coarse']=pd.Series(band_previous_bookings_not_canceled_coarse)
hb['band_previous_bookings_not_canceled_coarse']=pd.Series(band_previous_bookings_not_canceled_coarse)
cnt=hb.groupby('band_previous_bookings_not_canceled_coarse')['reservation_status'].count()
churn_rate=hb.groupby('band_babies_coarse')['reservation_status'].mean()
cnt.to_csv('C:/Users/hp/Desktop/hb/band_previous_bookings_not_canceled_coarse_count.csv')
churn_rate.to_csv('C:/Users/hp/Desktop/hb/band_previous_bookings_not_canceled_coarse_churn_rate.csv')





