from numpy import array, amin, argmin, std, mean
from matplotlib.pyplot import boxplot, title, xlabel, xticks, ylabel, grid, savefig
from scipy.stats import shapiro, levene, f_oneway


results_1095 = array([5433171, 5437942, 5445339, 5441334, 5432852, 5426670, 5437205, 5443350, 5437249, 5450403, 5442456])
errors_1095 = array([0.11979722, 0.20771486, 0.34402313, 0.27022096, 0.11391885, 0., 0.19413379, 0.30737082, 0.1949446, 0.43734003, 0.29089663])
times_1095 = array([67.24630547, 65.58454585, 65.19389939, 65.73885012, 64.92392921, 65.29004002, 80.58326769, 79.58089709, 76.2396419,  87.3598485, 76.66626024])

print()
print("bur26a - 10 95")
print()

best_result_1095 = amin(results_1095)
best_error_1095 = amin(errors_1095)
best_time_1095 = times_1095[argmin(results_1095)]

mean_error_1095 = mean(errors_1095)
std_error_1095 = std(errors_1095)

mean_time_1095 = mean(times_1095)
std_time_1095 = std(times_1095)

print("Best result: ", best_result_1095)
print("Best error: ", best_error_1095)
print("Best time: ", best_time_1095)
print("Mean error: ", mean_error_1095)
print("Std error: ", std_error_1095)
print("Mean time: ", mean_time_1095)
print("Std time: ", std_time_1095)

results_1098 = array([5439268, 5435652, 5436911, 5435203, 5432311, 5434198, 5434117, 5432553, 5434116, 5439153, 5426670])
errors_1098 = array([0.23214973, 0.16551587, 0.1887161, 0.15724192, 0.10394957, 0.13872227, 0.13722965, 0.10840902, 0.13721122, 0.23003057, 0.])
times_1098 = array([84.13163972, 78.49209952, 74.45893955, 79.17008686, 76.09569955, 70.24337888, 83.83253193, 72.6099112, 69.19856143, 70.18418646, 80.71088648])

print()
print("bur26a - 10 98")
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

results_1595 = array([5446255, 5438638, 5427110, 5433063, 5432357, 5435311, 5431434, 5435306, 5433155, 5438360, 5438341])
errors_1595 = array([0.36090273, 0.22054041, 0.0081081, 0.11780705, 0.10479723, 0.15923209, 0.08778864, 0.15913995, 0.11950238, 0.21541756, 0.21506744])
times_1595 = array([131.88792229, 126.9852767,  133.26705837, 143.84837818, 139.25647902, 146.59919143, 151.41694498, 126.46308517, 121.18203449, 134.26033568, 136.87608862])

print()
print("bur26a - 15 95")
print()

best_result_1595 = amin(results_1595)
best_error_1595 = amin(errors_1595)
best_time_1595 = times_1595[argmin(results_1595)]

mean_error_1595 = mean(errors_1595)
std_error_1595 = std(errors_1595)

mean_time_1595 = mean(times_1595)
std_time_1595 = std(times_1595)

print("Best result: ", best_result_1595)
print("Best error: ", best_error_1595)
print("Best time: ", best_time_1595)
print("Mean error: ", mean_error_1595)
print("Std error: ", std_error_1595)
print("Mean time: ", mean_time_1595)
print("Std time: ", std_time_1595)

results_1598 = array([5432604, 5437945, 5426670, 5443837, 5433539, 5444865, 5435393, 5427776, 5432664, 5432537, 5440677])
errors_1598 = array([0.10934883, 0.20777014, 0., 0.31634501, 0.12657855, 0.33528849, 0.16074314, 0.02038082, 0.11045448, 0.10811418, 0.25811409])
times_1598 = array([139.34465075, 138.65600634, 124.21234226, 166.28250766, 151.84660983, 164.91252255, 139.73563099, 142.11983538, 143.71995187, 136.77877498, 136.47840929])

print()
print("bur26a - 15 98")
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

boxplot([errors_1095, errors_1098, errors_1595, errors_1598])
title("Error porcentual - bur26a")
xlabel("Modelo")
xticks([1, 2, 3, 4], ('E: 10 F: 95%', 'E: 10 F: 98%', 'E: 15 F: 95%', 'E: 15 F: 98%'))
ylabel("Error [%]")
grid(axis='y')
savefig("box_bur26a.png", dpi=200)

print()

shapiro_statistic, shapiro_p_value = shapiro(errors_1095)
print("Shapiro 1095: ", shapiro_p_value)

shapiro_statistic, shapiro_p_value = shapiro(errors_1098)
print("Shapiro 1098: ", shapiro_p_value)

shapiro_statistic, shapiro_p_value = shapiro(errors_1595)
print("Shapiro 1595: ", shapiro_p_value)

shapiro_statistic, shapiro_p_value = shapiro(errors_1598)
print("Shapiro 1598: ", shapiro_p_value)

print()

levene_statistic, levene_p_value = levene(errors_1095, errors_1098, errors_1595, errors_1598)
print("Levene: ", levene_p_value)

print()

anova_statistic, anova_p_value = f_oneway(errors_1095, errors_1098, errors_1595, errors_1598)
print("ANOVA: ", anova_p_value)
