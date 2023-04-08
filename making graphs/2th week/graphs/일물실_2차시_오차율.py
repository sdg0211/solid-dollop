import 일물실_2차시_그래프 as p

INITIAL_LENGTH = 715
REAL_COPPER_HEATING = round(p.COPPER * INITIAL_LENGTH, 6)
REAL_COPPER_COOLING = round(p.COPPER * p.cu_initial_length_at_cooling, 6)

##############
h_delta_t = p.cu_final_temperature_at_heating - p.cu_initial_temperature_at_heating
h_delta_l = p.cu_final_length_at_heating - p.cu_initial_length_at_heating

h_alpha = round(h_delta_l/h_delta_t, 6)
##############
c_delta_t = p.cu_initial_temperature_at_cooling - p.cu_final_temperature_at_cooling
c_delta_l = p.cu_initial_length_at_cooling - p.cu_final_length_at_cooling

c_alpha = round(c_delta_l/c_delta_t, 6)
##############
# y-axis = alpha, x-axis=1, 2, 3
error_hr = 100*abs(h_alpha-REAL_COPPER_HEATING)/REAL_COPPER_HEATING
error_cr = 100*abs(c_alpha-REAL_COPPER_COOLING)/REAL_COPPER_COOLING
##############
p.plt.ylim([0, 6])
p.plt.plot(['가열', '냉각'], [error_hr, error_cr], 'ro', label='오차율') #error_hr, error_cr

p.plt.title("구리 시료 오차율", fontdict=p.title_font, pad=10)
p.plt.ylabel("오차율(%)", labelpad=3, fontdict={'size': 15})

p.plt.legend()
p.plt.show()