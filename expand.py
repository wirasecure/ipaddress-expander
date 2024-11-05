import ipaddress
import os

def expand_ip_ranges(input_ranges):
    # Split the input string by commas to get individual ranges
    ranges = input_ranges.split(',')
    expanded_ips = set()  # Use a set to avoid duplicates

    for r in ranges:
        r = r.strip()  # Remove any leading or trailing whitespace
        try:
            # Check if the range is in CIDR notation
            if '/' in r:
                network = ipaddress.ip_network(r, strict=False)
                # Add all IP addresses in the network to the set
                expanded_ips.update(str(ip) for ip in network.hosts())
            elif '-' in r:  # Handle IP range
                start_ip, end_ip = r.split('-')
                start_ip = ipaddress.ip_address(start_ip.strip())
                end_ip = ipaddress.ip_address(end_ip.strip())
                # Add all IP addresses in the range to the set
                for ip in range(int(start_ip), int(end_ip) + 1):
                    expanded_ips.add(str(ipaddress.ip_address(ip)))
            else:  # Handle single IP address
                single_ip = ipaddress.ip_address(r)
                expanded_ips.add(str(single_ip))

        except ValueError as e:
            print(f"Invalid IP range or CIDR notation '{r}': {e}")

    # Sort the expanded IPs for ordered output
    return sorted(expanded_ips)

# Example usage
input_ranges = "192.168.1.1-192.168.1.5, 10.0.0.0/24, 172.16.0.1-172.16.0.10, 10.192.64.204"
expanded_ips = expand_ip_ranges(input_ranges)

# Print current working directory
print("Current working directory:", os.getcwd())

# Write the expanded IP addresses to a text file
with open('expanded_ips.txt', 'w') as file:
    for ip in expanded_ips:
        file.write(f"{ip}\n")

print("Expanded IP addresses have been written to 'expanded_ips.txt'.")
