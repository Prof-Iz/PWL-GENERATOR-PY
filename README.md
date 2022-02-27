# Making a Digital Input Sequence

So there I was when my physical lab had failed and then my lecturer asked me to simulate my circuit instead. It was my first time using LTSpice and I had to make a Digital input sequence. In LTSpice XVII this is achieved via a PWL source. However, this source has to be manually input and I am a lazy person. So, I decided to code a short python script to generate my PWL source given a sequence and frequency.

## Pre Requisites

- engineering_notation module by `pip install engineering_notation`

## Main Code

```python
from engineering_notation import EngNumber
def make_pwl(sequence:str,bit_rate:float,filename="pwl.txt",voltage_level = 5):
    """Python Function to generate digital input voltage sequence
    given bit sequence and datarate. Output waveform
    at 5V voltage level by default and saved to a
    text file.

    Args:
        sequence (str): Sequence of bits ex: "1011001"
        bit_rate (float): data rate in Hz ex: 1e3 for 1 Kbps
        filename (str, optional): File to save the generated PWL. Defaults to "pwl.txt".
        voltage_level (int, optional): Peak Voltage level in PWL. Defaults to 5.
    """ 
    bit_period = 1/bit_rate
    half = bit_period/2
    mid = bit_period/2
    with open(filename,"w") as f:
        for bit in sequence:
            f.write(f"{EngNumber(mid - half)}\t{int(bit) * voltage_level}\n")
            f.write(f"{EngNumber(mid + half - half/10 )}\t{int(bit) * voltage_level}\n")
            mid = bit_period + mid
            
    f.close()
```

## Example usage

For an example sequence `10110001` at a data rate of `1.5 Kbps` the code would be as follows. 

```python
if __name__ == "__main__":
    # Example Sequence
    sequence = "10110001"
    frequency = 1.5e3
    make_pwl(sequence,frequency) 
```

Running the above code generates a `pwl.txt` file in the specified directory.

<img title="" src="https://raw.githubusercontent.com/Prof-Iz/PWL-GENERATOR-PY/main/assets/2022-02-27-16-07-45-image.png" alt="" data-align="center">

Taking the **PWL** file into an LTSpice Circuit for testing we end up confirming that the result is as expected.

![](https://raw.githubusercontent.com/Prof-Iz/PWL-GENERATOR-PY/main/assets/2022-02-27-16-12-38-image.png)
