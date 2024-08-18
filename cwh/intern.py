import pandas as pd
# import maths
import os

# Function to process each CSV file
def process_csv(file_path):
    # Read CSV file
    df = pd.read_csv(file_path)

    # Define columns and their alternatives
    columns_to_process = {
        "Corrected Velocity.X(cm/s)": ["Corrected Velocity.X (cm/s)", "Corrected Velocity.X (m/s)"],
        "Corrected Velocity.Y(cm/s)": ["Corrected Velocity.Y (cm/s)", "Corrected Velocity.Y (m/s)"],
        "Corrected Velocity.Z(cm/s)": ["Corrected Velocity.Z (cm/s)", "Corrected Velocity.Z (m/s)"]
    }

    # Dictionary to store deviation means
    deviation_means = {}

    # Calculate mean of deviations for each column or its alternative
    for col, alternatives in columns_to_process.items():
        found_col = False
        for alt_col in alternatives:
            if alt_col in df:
                found_col = True
                if alt_col.endswith("(m/s)"):
                    df[alt_col] *= 100
                temp_mean = df[alt_col].mean()
                deviation_mean_col = col + '_deviation_mean'
                df[col + '_deviation'] = abs(df[alt_col] - temp_mean)
                deviation_means[deviation_mean_col] = df[col + '_deviation'].mean()
                temp_col = deviation_mean_col + '_mean'
                deviation_means[temp_col] = temp_mean
                break
        if not found_col:
            deviation_mean_col = col + '_deviation_mean'
            deviation_means[deviation_mean_col] = None

    # Calculate mean of 'Raw Pressure (in H20)' column
    if "Raw Pressure (m H₂O)" in df:
        pressure_mean = df["Raw Pressure (m H₂O)"].mean()
        deviation_means["Raw Pressure (m H₂O)_mean"] = pressure_mean
    elif "Raw Pressure (dbar)" in df:
        pressure_mean = df["Raw Pressure (dbar)"].mean()
        deviation_means["Raw Pressure (m H₂O)_mean"] = pressure_mean

    # Append results to a list
    results.append({'File': os.path.basename(file_path), **deviation_means})

    return df

# Path to the directory containing CSV files
directory_path = "C:\Users\admin\Desktop"

# List to store results
results = []

# Iterate through each file in the directory
for filename in os.listdir(directory_path):
    if filename.endswith(".csv"):
        file_path = os.path.join(directory_path, filename)
        df = process_csv(file_path)

        # Write processed DataFrame to a new CSV file
        output_file_path = os.path.join(directory_path, f"processed_{filename}")
        # df.to_csv(output_file_path, index=False)

# Create a DataFrame from the results list
results_df = pd.DataFrame(results)

# Write results to a new CSV file
results_df.to_csv(os.path.join("C:\Users\admin\Desktop"), index=False)

print("Processing completed!")

#line53 and 72 path location change, install module pandas in pycharm.