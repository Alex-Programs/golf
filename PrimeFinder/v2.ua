f ← (
  ⇡ⁿ5 4 # Generate numbers up to 1024
  ↘2    # Filter first two elements. It is now 2,3,4 etc
  ◿     # Modulo everything
  = 0   # Is it equal to 0?
  /+    # Sum
  = 1   # Check if equal to one match (itself)
)

⇡ⁿ5 4 # Create numbers up to 1024
.     # Duplicate
∵f    # Run the function on every element
▽     # Use binary list as a filter for the numbers
