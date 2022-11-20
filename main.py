from nltk import *

flight_database = (
  '(FLIGHT M1)',
  '(FLIGHT M2)',
  '(FLIGHT M3)',
  '(FLIGHT M4)',
  '(FLIGHT M5)',
  '(FLIGHT M6)',
  '(ATIME M1 HUE 11:00HR)',
  '(DTIME M1 HCMC 10:00HR)',
  '(ATIME M2 HUE 13:30HR)',
  '(DTIME M2 HN 12:30HR)',
  '(ATIME M3 HCM 16:30HR)',
  '(DTIME M3 DANANG 15:00HR)',
  '(ATIME M4 HAIPHONG 10:30HR)',
  '(DTIME M4 DANANG 8:30HR)',
  '(ATIME M5 HN 5:45HR)',
  '(DTIME M5 HCM 3:30HR)',
  '(ATIME M6 HAIPHONG 11:30HR)',
  '(DTIME M6 HCMC 9:30HR)',
  '(RUN-TIME M1 HCMC HUE 1:00 HR)',
  '(RUN-TIME M2 HN HUE 1:00 HR)',
  '(RUN-TIME M3 DANANG HCM 1:30 HR)',
  '(RUN-TIME M4 DANANG HAIPHONG 2:00 HR)',
  '(RUN-TIME M5 HCM HN 2:15 HR)',
  '(RUN-TIME M6 HCM HAIPHONG 2:00 HR)',
)

flights = (data.replace('(', '').replace(')', '') for data in flight_database if 'FLIGHT' in data)
arrival_times = (data.replace('(', '').replace(')', '') for data in flight_database if 'ATIME' in data)
departure_times = (data.replace('(', '').replace(')', '') for data in flight_database if 'DTIME' in data)
run_times = (data.replace('(', '').replace(')', '') for data in flight_database if 'RUN-TIME' in data)
