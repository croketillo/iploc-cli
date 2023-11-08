"""
This file is (or part of) IPLOC v1.1
Copyright 2023- Croketillo <croketillo@gmail.com> https://github.com/croketillo

DESCRIPTION:
IPLOC is a CLI script to geolocate an IP

LICENSE - GNU GPL-3

This software is protected by the GNU General Public License version 3 (GNU GPL-3).
You are free to use, modify, and redistribute this software in accordance with the
terms of the GNU GPL-3. You can find a copy of the license at the following link:
https://www.gnu.org/licenses/gpl-3.0.html.

This software is provided as-is, without any warranties, whether express or implied.
Under no circumstances shall the authors or copyright holders be liable for any claims,
damages, or liabilities arising in connection with the use of this software.
If you make modifications to this software and redistribute it, you must comply with
the terms of the GNU GPL-3, which includes the obligation to provide the source code
for your modifications. Additionally, any derived software must also be under the
GNU GPL-3.

For more information about the GNU GPL-3 and its terms, please carefully read the full
license or visit https://www.gnu.org/licenses/gpl-3.0.html
"""

import re
import argparse
import requests
from colorama import Fore, Style, Back

def geolocate_ip(ip):
    url = f"https://ipinfo.io/{ip}/json"

    try:
        response = requests.get(url)
        data = response.json()
        country = data.get('country', 'Unknown')
        city = data.get('city', 'Unknown')
        region = data.get('region', 'Unknown')
        location = data.get('loc', 'Unknown')
        org = data.get('org', 'Unknown')
        zip_code = data.get('postal', 'Unknown')
        timezone = data.get('timezone', 'Unknown')

        return country, region, city, location, org, zip_code, timezone
    except requests.exceptions.RequestException as e:
        return f'Error geolocating IP {ip}: {str(e)}'

def validate_ip(ip):
    ip_pattern = r'^(\d{1,3}\.){3}\d{1,3}$'

    return bool(re.match(ip_pattern, ip))

def main():
    parser = argparse.ArgumentParser(description="DESCRIPTION: Geolocate an IP address.")
    parser.add_argument("IP", help="The IP address you want to geolocate.")
    args = parser.parse_args()

    is_valid = validate_ip(args.IP)
    if is_valid:
        result = geolocate_ip(args.IP)

        print("\n" + Style.BRIGHT + "{:<10} {}".format("", Back.RED +
                                                            Fore.WHITE + "  [" + args.IP + "] ") +
                                                            Fore.LIGHTBLACK_EX +
                                                            Style.NORMAL +
                                                            Back.RESET)
        print("----------------------------------------")
        print("{:<12}: {}".format("COUNTRY", Fore.YELLOW +
                                            Style.BRIGHT +
                                            result[0] +
                                            Style.NORMAL +
                                            Fore.LIGHTBLACK_EX))
        print("{:<12}: {}".format("REGION", Fore.YELLOW +
                                            Style.BRIGHT +
                                            result[1] +
                                            Style.NORMAL +
                                            Fore.LIGHTBLACK_EX))
        print("{:<12}: {}".format("CITY", Fore.YELLOW +
                                            Style.BRIGHT +
                                            result[2] +
                                            Style.NORMAL +
                                            Fore.LIGHTBLACK_EX))
        print("{:<12}: {}".format("LOCATION", Fore.YELLOW +
                                            Style.BRIGHT +
                                            result[3] +
                                            Style.NORMAL +
                                            Fore.LIGHTBLACK_EX))
        print("{:<12}: {}".format("ORGANIZATION", Fore.YELLOW +
                                                Style.BRIGHT +
                                                result[4] +
                                                Style.NORMAL +
                                                Fore.LIGHTBLACK_EX))
        print("{:<12}: {}".format("ZIP CODE", Fore.YELLOW +
                                            Style.BRIGHT +
                                            result[5] +
                                            Style.NORMAL +
                                            Fore.LIGHTBLACK_EX))
        print("{:<12}: {}".format("TIMEZONE", Fore.YELLOW +
                                            Style.BRIGHT +
                                            result[6] +
                                            Style.NORMAL +
                                            Fore.LIGHTBLACK_EX))
        print("----------------------------------------")
        print("{:<29} {}".format("", Fore.LIGHTBLACK_EX + "IPLOC v1.0\n"))
    else:
        print("The specified IP is not valid. Please try again with a valid IP.")

if __name__ == "__main__":
    main()
