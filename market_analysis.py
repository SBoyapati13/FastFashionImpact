import pandas as pd
import matplotlib.pyplot as plt

def analyze_market_growth():
    years = [2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029]
    market_size = [91.23, 106.42, 122.98, 136.19, 163.21, 174.63, 186.86, 199.94, 214.24]
    
    df = pd.DataFrame({'Year': years, 'Market Size (billion USD)': market_size})
    
    plt.figure(figsize=(10, 6))
    plt.plot(df['Year'], df['Market Size (billion USD)'], marker='o')
    plt.title('Fast Fashion Market Growth (2021-2029)')
    plt.xlabel('Year')
    plt.ylabel('Market Size (billion USD)')
    plt.grid(True)
    plt.savefig('fast_fashion_market_growth.png')
    plt.close()
    
    return df

def calculate_cagr(start_value, end_value, num_years):
    return (end_value / start_value) ** (1 / num_years) - 1

def main():
    market_data = analyze_market_growth()
    cagr = calculate_cagr(market_data['Market Size (billion USD)'].iloc[0], 
                          market_data['Market Size (billion USD)'].iloc[-1], 
                          len(market_data) - 1)
    
    print(f"Fast Fashion Market Analysis (2021-2029)")
    print(f"CAGR: {cagr:.2%}")
    print(f"Market size in 2025: ${market_data['Market Size (billion USD)'].iloc[4]:.2f} billion")
    print(f"Projected market size in 2029: ${market_data['Market Size (billion USD)'].iloc[-1]:.2f} billion")
    print(f"The fast fashion market is expected to grow at a CAGR of 7% from 2025 to 2029[2].")

if __name__ == "__main__":
    main()
