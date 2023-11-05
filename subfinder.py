#!/usr/bin/python3
import requests, socket
R = '\033[91m'
G = '\033[92m'
W = '\033[00m'
print(f"""{G}

      ___________________________
    < coded by: nur muhammad wafa >
      ---------------------------
            \   ^__^
             \  (oo)\_______
              \ (__)\       )\\
                    ||----ω |
                    ||     ||
                                

    {W}""")
def get_ip(sub, domain):
    try:
        hostname = f"{sub}.{domain}"
        ip = socket.gethostbyname(hostname)
        return ip
    except socket.gaierror:
        return None
def main():
    try:
        domain = input('[+] Masukkan nama domain : ')
        subdomain = input('[+] Masukkan list subdomain : ')
        with open(subdomain) as file:
            sub_list = file.read()
        subs = sub_list.splitlines()
        valid_subdomains = []
        for sub in subs:
            if not sub.isalnum():
                continue
            url_check = f"http://{sub}.{domain}"
            try:
                response = requests.get(url_check)
                if response.ok:
                    status_code = response.status_code
                    ip = get_ip(sub, domain)
                    print(f"[{G}{status_code}{W}] : [{G}{ip}{W}] : {url_check}")
                    valid_subdomains.append(sub)
            except requests.exceptions.ConnectionError:
                pass
        print(f'[{G}{len(valid_subdomains)}{W}] Valid subdomains Found!')
    except FileNotFoundError:
        print(f"[{R}!{W}] {R}Subdomain file list not found{W}")
    except KeyboardInterrupt:
        print(f"[{R}!{W}] {R}Program cancelled by user{W}")
    except Exception as e:
        print(f"[{R}!{W}] {R}An error occurred: {str(e)}{W}")

if __name__ == "__main__":
    main()