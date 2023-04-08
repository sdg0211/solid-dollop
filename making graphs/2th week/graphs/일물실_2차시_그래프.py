# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

#The constants
ALUMINIUM = 2.4e-05
IRON = 1.2e-05
COPPER = 1.6e-05
#

plt.rcParams['font.family'] = 'AppleGothic'

filename = '/Users/nyh211/Desktop/CAU/1-1/일반물리실험/일반물리실험 2차시(선팽창계수 측정)/일반물리실험 2차시(선팽창계수 측정표).xlsx'

df_first_sheet = pd.read_excel(filename, sheet_name='알루미늄', engine='openpyxl')
df_second_sheet = pd.read_excel(filename, sheet_name='철', engine='openpyxl')
df_final_sheet = pd.read_excel(filename, sheet_name='구리', engine='openpyxl')

########################################
al_initial_temperature_at_heating = df_first_sheet.at[6, 'Unnamed: 1'] #가열 전 알루미늄 온도: 24.2
al_final_temperature_at_heating = df_first_sheet.at[6, 'Unnamed: 2'] #가열 후알루미늄 온도: 94.8

al_initial_temperature_at_cooling = df_first_sheet.at[8, 'Unnamed: 1'] #냉각 전 알루미늄 온도: 94.8
al_final_temperature_at_cooling = df_first_sheet.at[8, 'Unnamed: 2'] #냉각 후 알루미늄 온도: 36.5

al_initial_length_at_heating = df_first_sheet.at[6, 'Unnamed: 4'] #가열 전 알루미늄 길이: 713
al_final_length_at_heating = df_first_sheet.at[6, 'Unnamed: 5'] #가열 후 알루미늄 길이: 714.24

al_initial_length_at_cooling = df_first_sheet.at[8, 'Unnamed: 4'] #냉각 시 알루미늄 길이: 714.24
al_final_length_at_cooling = df_first_sheet.at[8, 'Unnamed: 5'] #냉각 후 알루미늄 길이: 713.22
########################################
fe_initial_temperature_at_heating = df_second_sheet.at[6, 'Unnamed: 1'] #가열 전 철 온도: 24.2
fe_final_temperature_at_heating = df_second_sheet.at[6, 'Unnamed: 2'] #가열 철 온도: 94.8

fe_initial_temperature_at_cooling = df_second_sheet.at[8, 'Unnamed: 1'] #냉각 전 철 온도: 94.8
fe_final_temperature_at_cooling = df_second_sheet.at[8, 'Unnamed: 2'] #냉각 후 철 온도: 36.5

fe_initial_length_at_heating = df_second_sheet.at[6, 'Unnamed: 4'] #가열 전 철 길이: 715
fe_final_length_at_heating = df_second_sheet.at[6, 'Unnamed: 5'] #가열 후 철 길이: 714.24

fe_initial_length_at_cooling = df_second_sheet.at[8, 'Unnamed: 4'] #냉각 시 철 길이: 714.24
fe_final_length_at_cooling = df_second_sheet.at[8, 'Unnamed: 5'] #냉각 후 철 길이: 713.22
########################################
cu_initial_temperature_at_heating = df_final_sheet.at[6, 'Unnamed: 1'] #가열 전 구리 온도: 24.2
cu_final_temperature_at_heating = df_final_sheet.at[6, 'Unnamed: 2'] #가열 구리 온도: 94.8

cu_initial_temperature_at_cooling = df_final_sheet.at[8, 'Unnamed: 1'] #냉각 구리 철 온도: 94.8
cu_final_temperature_at_cooling = df_final_sheet.at[8, 'Unnamed: 2'] #냉각 후 구리 온도: 36.5

cu_initial_length_at_heating = df_final_sheet.at[6, 'Unnamed: 4'] #가열 전 구리 길이: 715
cu_final_length_at_heating = df_final_sheet.at[6, 'Unnamed: 5'] #가열 후 구리 길이: 714.24

cu_initial_length_at_cooling = df_final_sheet.at[8, 'Unnamed: 4'] #냉각 시 구리 길이: 714.24
cu_final_length_at_cooling = df_final_sheet.at[8, 'Unnamed: 5'] #냉각 후 구리 길이: 713.22

########################################

plt.plot([fe_initial_temperature_at_cooling, fe_final_temperature_at_cooling], [fe_initial_length_at_cooling, fe_final_length_at_cooling], 'ro', label='철')
plt.plot([fe_initial_temperature_at_cooling, fe_final_temperature_at_cooling], [fe_initial_length_at_cooling, fe_final_length_at_cooling], 'b-', linestyle='--', label='실험값\n추세선')

title_font = {
    'size': 23
} #fontdict of title

body_font = {
    'size': 15,
    'color': 'b'
} #fontdict of body

plt.title("철 시료 냉각", fontdict=title_font, pad=10)

plt.ylabel("L(mm)", labelpad=2, fontdict={'size': 15})
plt.xlabel("T(°C)", labelpad=5, fontdict={'size': 15})

#alpha

#body
delta_t = fe_initial_temperature_at_cooling - fe_final_temperature_at_cooling
delta_l = fe_initial_length_at_cooling - fe_final_length_at_cooling

m = round(delta_l/delta_t, 4)

n = round(fe_final_length_at_cooling - m * fe_final_temperature_at_cooling, 4)

experimental_line = 'y = ' + str(m) + 'x+' + str(n)

real_alpha = round(fe_initial_length_at_cooling * IRON, 4)
#
#line
plt.text(40, 713.05, experimental_line, rotation = 23.5, fontdict={'color': 'b', 'size': 13})
#
#body
plt.text(17, 713.9, '선팽창계수 참값: '+str(real_alpha), fontdict={'color': 'g', 'size': 13})
plt.text(17, 713.8, '선팽창계수 실험값: '+str(m), fontdict={'color': 'b', 'size': 13})
#
plt.axis([15, 110, 712.5, 714])

plt.legend()
plt.show()