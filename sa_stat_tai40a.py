from numpy import array, amin, argmin, mean, std, median
from matplotlib.pyplot import boxplot, ylim, title, xlabel, xticks, ylabel, grid, savefig
from scipy.stats import shapiro, friedmanchisquare


results_1098 = array([3268704, 3274892, 3293460, 3266694, 3268044, 3272620, 3292020, 3275258, 3271440, 3288232, 3291968])
errors_1098 = array([4.11974377, 4.31685338, 4.90830963, 4.05571819, 4.09872044, 4.24448217, 4.86244055, 4.32851177, 4.20689501, 4.7417794,  4.86078417])
times_1098 = array([182.64795876, 167.84539962, 177.69486237, 172.80163646, 173.20843053, 193.00867534, 216.6245923,  211.19770432, 181.57724905, 181.94851875, 193.26028562])

print()
print("tai40a - 10 98")
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

results_1099 = array([3253178, 3228264, 3265292, 3250016, 3265314, 3271566, 3235984, 3251876, 3278680, 3288246, 3264018])
errors_1099 = array([3.62518594, 2.83158723, 4.01105954, 3.5244651,  4.01176032, 4.21090856, 3.07749644, 3.58371266, 4.43751453, 4.74222535, 3.97047815])
times_1099 = array([150.09163642, 149.79984474, 147.3422513,  148.4137342,  150.88004088, 147.20056295, 147.77353168, 149.70119572, 147.34176826, 149.91602564, 149.31318331])

print()
print("tai40a - 10 99")
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

results_1598 = array([3269910, 3266762, 3274056, 3277744, 3217020, 3286430, 3236798, 3271756, 3299374, 3274452, 3288122])
errors_1598 = array([4.15815912, 4.05788423, 4.29022383, 4.40769963, 2.4734262,  4.68437935, 3.10342521, 4.21696073, 5.09669137, 4.30283783, 4.73827551])
times_1598 = array([242.98920488, 224.97570515, 212.79025412, 212.59479713, 213.25216174, 214.2736063,  215.66748118, 214.1646564,  214.10181904, 215.45460701, 211.74827814])

print()
print("tai40a - 15 98")
print()

best_result_1598 = amin(results_1598)
best_error_1598 = amin(errors_1598)
best_time_1598 = times_1598[argmin(results_1598)]

mean_error_1598 = mean(errors_1598)
std_error_1598 = std(errors_1598)

median_error_1598 = median(errors_1598)

mean_time_1598 = mean(times_1598)
std_time_1598 = std(times_1598)

print("Best result: ", best_result_1598)
print("Best error: ", best_error_1598)
print("Best time: ", best_time_1598)
print("Mean error: ", mean_error_1598)
print("Std error: ", std_error_1598)
print("Median error: ", median_error_1598)
print("Mean time: ", mean_time_1598)
print("Std time: ", std_time_1598)

results_1599 = array([3245906, 3267168, 3259926, 3269494, 3286180, 3264928, 3210038, 3250262, 3251642, 3242154, 3246474])
errors_1599 = array([3.39354711, 4.07081676, 3.84013353, 4.14490805, 4.67641597, 3.99946486, 2.25102489, 3.53230107, 3.57625893, 3.27403269, 3.41163992])
times_1599 = array([216.42308378, 213.38647556, 213.65262771, 214.60933208, 213.81370187, 214.72449303, 212.68700552, 212.30555534, 214.86905193, 214.48910713, 213.00346518])

print()
print("tai40a - 15 99")
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
ylim(bottom=-0.2)
title("Error porcentual - tai40a")
xlabel("Modelo")
xticks([1, 2, 3, 4], ('E: 10 F: 98%', 'E: 10 F: 99%', 'E: 15 F: 98%', 'E: 15 F: 99%'))
ylabel("Error [%]")
grid(axis='y')
savefig("box_tai40a.png", dpi=200)

print()


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
