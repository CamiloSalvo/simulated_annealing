from numpy import array, amin, argmin, std, mean
from matplotlib.pyplot import boxplot, ylim, title, xlabel, xticks, ylabel, grid, savefig
from scipy.stats import shapiro, friedmanchisquare


results_1098 = array([691146345, 695845873, 637815035, 693750569, 668796908, 665861972, 659699018, 652837135, 654591478, 697274064, 666857130])
errors_1098 = array([8.45748401, 9.19495297, 0.08851882, 8.86614938, 4.95031982, 4.48975778, 3.52264207, 2.4458476,  2.72114621, 9.41907049, 4.645922])
times_1098 = array([145.28802848, 143.47612619, 144.17370391, 144.57052207, 143.31904864, 143.00755453, 144.00282574, 143.94699383, 142.52166843, 143.27655506, 142.68401933])

print()
print("tai40b - 10 98")
print()

best_result_1098 = amin(results_1098)
best_error_1098 = amin(errors_1098)
best_time_1098 = times_1098[argmin(results_1098)]

mean_error_1098 = mean(errors_1098)
std_error_1098 = std(errors_1098)

mean_time_1098 = mean(times_1098)
std_time_1098 = std(times_1098)

print("Best result: ", best_result_1098)
print("Best error: ", best_error_1098)
print("Best time: ", best_time_1098)
print("Mean error: ", mean_error_1098)
print("Std error: ", std_error_1098)
print("Mean time: ", mean_time_1098)
print("Std time: ", std_time_1098)

results_1099 = array([671633646, 654856020, 637443123, 660820718, 655704357, 637773868, 657056972, 673012702, 659927644, 666310939, 639321107])
errors_1099 = array([5.39547224, 2.76265921, 0.03015688, 3.69866378, 2.89578369, 0.08205872, 3.10804151, 5.61187929, 3.55851899, 4.5602115,  0.32485774])
times_1099 = array([143.58164501, 142.78680229, 142.41562939, 142.32849979, 142.93745255, 143.03001165, 143.61441493, 142.20701241, 141.28275633, 142.28067112, 142.37482524])

print()
print("tai40b - 10 99")
print()

best_result_1099 = amin(results_1099)
best_error_1099 = amin(errors_1099)
best_time_1099 = times_1099[argmin(results_1099)]

mean_error_1099 = mean(errors_1099)
std_error_1099 = std(errors_1099)

mean_time_1099 = mean(times_1099)
std_time_1099 = std(times_1099)

print("Best result: ", best_result_1099)
print("Best error: ", best_error_1099)
print("Best time: ", best_time_1099)
print("Mean error: ", mean_error_1099)
print("Std error: ", std_error_1099)
print("Mean time: ", mean_time_1099)
print("Std time: ", std_time_1099)

results_1598 = array([650223219, 661641146, 647629557, 677153884, 674604436, 650540154, 659528695, 670267588, 637336250, 651616994, 668724138])
errors_1598 = array([2.03566131, 3.82740866, 1.62865336, 6.26173035, 5.86166064, 2.08539603, 3.4959143,  5.18110489, 0.01338594, 2.25437813, 4.93890046])
times_1598 = array([217.93269539, 215.31725812, 213.60137916, 213.86833429, 213.63140202, 254.61923671, 291.9952631,  270.55364609, 279.63479757, 294.39740801, 313.80578303])

print()
print("tai40b - 15 98")
print()

best_result_1598 = amin(results_1598)
best_error_1598 = amin(errors_1598)
best_time_1598 = times_1598[argmin(results_1598)]

mean_error_1598 = mean(errors_1598)
std_error_1598 = std(errors_1598)

mean_time_1598 = mean(times_1598)
std_time_1598 = std(times_1598)

print("Best result: ", best_result_1598)
print("Best error: ", best_error_1598)
print("Best time: ", best_time_1598)
print("Mean error: ", mean_error_1598)
print("Std error: ", std_error_1598)
print("Mean time: ", mean_time_1598)
print("Std time: ", std_time_1598)

results_1599 = array([666139425, 655344372, 643451446, 666810622, 665194166, 650400598, 651194364, 650096309, 666208166, 673920287, 668392001])
errors_1599 = array([4.53329683, 2.83929338, 0.97300726, 4.63862378, 4.38496295, 2.06349634, 2.18805732, 2.01574608, 4.54408394, 5.75430121, 4.88678018])
times_1599 = array([301.16162419, 309.99846077, 288.66565037, 221.78747535, 285.89097095, 339.07971621, 306.20705223, 342.62958145, 342.17123055, 221.26675558, 231.9724772])

print()
print("tai40b - 15 99")
print()

best_result_1599 = amin(results_1599)
best_error_1599 = amin(errors_1599)
best_time_1599 = times_1599[argmin(results_1599)]

mean_error_1599 = mean(errors_1599)
std_error_1599 = std(errors_1599)

mean_time_1599 = mean(times_1599)
std_time_1599 = std(times_1599)

print("Best result: ", best_result_1599)
print("Best error: ", best_error_1599)
print("Best time: ", best_time_1599)
print("Mean error: ", mean_error_1599)
print("Std error: ", std_error_1599)
print("Mean time: ", mean_time_1599)
print("Std time: ", std_time_1599)

boxplot([errors_1098, errors_1099, errors_1598, errors_1599])
ylim(bottom=-0.5)
title("Error porcentual - tai40b")
xlabel("Modelo")
xticks([1, 2, 3, 4], ('E: 10 F: 98%', 'E: 10 F: 99%', 'E: 15 F: 98%', 'E: 15 F: 99%'))
ylabel("Error [%]")
grid(axis='y')
savefig("box_tai40b.png", dpi=200)

print()

shapiro_statistic, shapiro_p_value = shapiro(errors_1098)
print("Shapiro 1098: ", shapiro_p_value)

shapiro_statistic, shapiro_p_value = shapiro(errors_1099)
print("Shapiro 1099: ", shapiro_p_value)

shapiro_statistic, shapiro_p_value = shapiro(errors_1598)
print("Shapiro 1598: ", shapiro_p_value)

shapiro_statistic, shapiro_p_value = shapiro(errors_1599)
print("Shapiro 1599: ", shapiro_p_value)

print()

friedman_statistic, friedman_p_value = friedmanchisquare(errors_1098, errors_1099, errors_1598, errors_1599)
print("Friedman: ", friedman_p_value)
