from trimmed_match.estimator import TrimmedMatch

#####################################################################
# Reports the estimate of incremental return on ad spend (iROAS)
# using geo experimental data from a matched pairs design (5 geo pairs)
#####################################################################

delta_response = [
    1, 10, 3, 8, 5
]  # response difference between treatment and control in each geo pair
delta_spend = [1, 5, 2, 5, 3]      # spend difference between treatment and control in each geo pair
confidence_level = 0.80            # for the two-sided confidence interval
tm = TrimmedMatch(delta_response, delta_spend)
report = tm.Report(confidence=confidence_level)
print('iroas=%.2f, ci=(%.2f, %.2f)' % (
      report.estimate, report.conf_interval_low, report.conf_interval_up))

# iroas=1.60, ci=(1.52, 1.66)