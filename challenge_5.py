def missing_char(s, n):
    # Extract the substring before index n and the substring after index n+1
    return s[:n] + s[n+1:]

# Test cases
print(missing_char('kitten', 1))  # Output: 'ktten'
print(missing_char('kitten', 0))  # Output: 'itten'
print(missing_char('kitten', 4))  # Output: 'kittn'
