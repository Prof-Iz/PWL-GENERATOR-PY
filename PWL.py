from engineering_notation import EngNumber
def make_pwl(sequence:str,frequency:float,filename="pwl.txt",voltage_level = 5):
    """Python Function to generate digital input voltage sequence
    given bit sequence and datarate. Output waveform
    at 5V voltage level by default and saved to a
    text file.

    Args:
        sequence (str): Sequence of bits ex: "1011001"
        frequency (float): data rate in Hz ex: 1e3 for 1Khz
        filename (str, optional): File to save the generated PWL. Defaults to "pwl.txt".
        voltage_level (int, optional): Peak Voltage level in PWL. Defaults to 5.
    """ 
    bit_period = 1/frequency
    half = bit_period/2
    mid = bit_period/2
    with open(filename,"w") as f:
        for i, bit in enumerate(sequence):
            f.write(f"{EngNumber(mid - half)}\t{int(bit) * voltage_level}\n")
            f.write(f"{EngNumber(mid + half - half/10 )}\t{int(bit) * voltage_level}\n")
            mid = bit_period + mid
            
    f.close()
    
    
    
if __name__ == "__main__":
    # Example Sequence
    sequence = "10110001"
    frequency = 1.5e3
    make_pwl(sequence,frequency)
    