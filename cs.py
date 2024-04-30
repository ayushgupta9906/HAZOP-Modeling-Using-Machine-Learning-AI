import pandas as pd
import numpy as np

# Hypothetical deviations with risk criteria
deviations_data = {
    'Node': ['Reactor R-101', 'Reactor R-101'],
    'Deviation': ['High temperature', 'Low flow rate'],
    'Guide Word': ['High', 'Low'],
    'Parameter': ['Temperature', 'Flow Rate'],
    'Design Intent': ['React chemicals A and B to form compound X', 'React chemicals A and B to form compound X'],
    'Cause': ['Failure of temperature control system', 'Blockage in the flow line'],
    'Consequence': ['Thermal runaway, potential for reactor overpressure', 'Incomplete reaction, decreased product yield'],
    'Consequence Category': ['Fire/Explosion', 'Quality/Productivity'],
    'IPL Requirement': ['Temperature sensor with alarm and automatic shutdown', 'Flow rate monitoring system with interlock'],
    'LOPA Requirement': ['Safety interlock and emergency shutdown system', 'Additional flow sensors for redundancy'],
    'PHA Recommendation': ['Regular maintenance and testing of temperature control system', 'Implement preventive maintenance for flow lines'],
    'Priority': ['High', 'Medium'],
    'Responsible Party': ['Process Engineer', 'Maintenance Team'],
    'Status': ['Open', 'Open'],
    'Comments': ['Scheduled maintenance due in two weeks', 'Flow sensors to be installed by the end of the month'],
    'Safeguard': ['Temperature emergency shutdown system', 'Flow rate alarms and interlocks'],
    'Safeguard Effectiveness': ['Highly effective', 'Effective'],
    'Risk Criteria': ['Tolerable if frequency < 1/year', 'Tolerable if production loss < 5%'],
}

# Create a DataFrame from the deviations data
deviations_df = pd.DataFrame(deviations_data)

# Risk levels mapping
risk_levels = {
    'Low': 1,
    'Medium': 3,
    'High': 5,
}

# Map consequence severity and likelihood to risk levels
deviations_df['Consequence Severity Level'] = deviations_df['Consequence'].map(risk_levels)
deviations_df['Likelihood Level'] = deviations_df['Priority'].map(risk_levels)

# Generate the risk matrix (original)
risk_matrix_data = {
    'Consequence \ Likelihood': ['Insignificant', 'Minor', 'Moderate', 'Major', 'Severe'],
    'Level 1': ['Green', 'Green', 'Green', 'Yellow', 'Yellow'],
    'Level 2': ['Green', 'Green', 'Yellow', 'Yellow', 'Orange'],
    'Level 3': ['Yellow', 'Yellow', 'Yellow', 'Orange', 'Orange'],
    'Level 4': ['Yellow', 'Orange', 'Orange', 'Orange', 'Red'],
    'Level 5': ['Orange', 'Orange', 'Red', 'Red', 'Brown'],
}

# Create a DataFrame for the risk matrix (original)
risk_matrix_df = pd.DataFrame(risk_matrix_data)

# Set the risk levels as index
risk_matrix_df.set_index('Consequence \ Likelihood', inplace=True)

# Add a row and column of zeros to the original risk matrix
zero_row = pd.Series([0] * len(risk_matrix_df.columns), name='Zero')
risk_matrix_df_with_zeros = pd.concat([zero_row, risk_matrix_df], axis=0)
risk_matrix_df_with_zeros = pd.concat([zero_row, risk_matrix_df_with_zeros], axis=1)

# Generate the mirrored risk matrix
upper_triangle = np.triu(risk_matrix_df_with_zeros.values)
mirrored_risk_matrix = np.concatenate((upper_triangle, upper_triangle.T), axis=1)

# Create a DataFrame for the mirrored risk matrix
columns = list(risk_matrix_df_with_zeros.columns)
index = list(risk_matrix_df_with_zeros.index) + list(risk_matrix_df_with_zeros.index)[1:][::-1]
mirrored_risk_matrix_df = pd.DataFrame(mirrored_risk_matrix, columns=columns, index=index)

# Save the DataFrames to Excel files
output_deviations_file = 'hazop_deviations_with_risk_matrix.xlsx'
output_risk_matrix_file = 'hazop_risk_matrix_mirrored.xlsx'
deviations_df.to_excel(output_deviations_file, index=False)
mirrored_risk_matrix_df.to_excel(output_risk_matrix_file)


