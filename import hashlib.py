import hashlib

# The target MD5 hash
target_hash = "388fead5c64d1b4093bb74a3363fada1"

# Loop through possible values of X from 1 to 200
for X in range(1, 201):
    # Construct the code in the format CTF{CARROTX}
    code = f"CTF{{CARROT{X}}}"
    
    # Calculate the MD5 hash of the code
    code_hash = hashlib.md5(code.encode()).hexdigest()
    
    # Check if the calculated hash matches the target hash
    if code_hash == target_hash:
        print(f"The matching code is: {code}")
        break
else:
    print("No matching code found in the range.")