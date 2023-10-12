f ← (
  dump∘
  ⇡10 # Generate numbers up to 10
  ↘2  # Filter first two elements. It is now 2,3,4 etc
  ◿   # Modulo everything
  = 0 # Is it equal to 0?
  /+  # Sum
  = 1 # Check if equal to one match (itself)
)

⇡64 # Create numbers up to 64
↘1  # Remove first one
f   # Add f to stack
∵|  # Function on all elements
