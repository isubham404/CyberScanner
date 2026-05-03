import os 
import argparse
from datetime import datetime

OUTPUT_DIR = "outputs"
REPORT_DIR = "reports"
WORDLIST = "wordlists/common.txt"



def clean_target(target):
    return target.replace("http://", "").replace("https://", "").strip("/")


def create_dirs():
    os.makedirs(OUTPUT_DIR,exist_ok=True)
    os.makedirs(REPORT_DIR,exist_ok=True)


def run_command(command,output_file):
    print(f"[+] running : {command} ")
    os.system(f"{command} > {output_file}")



#scanners

def run_nmap(target):
    output = f"{OUTPUT_DIR}/nmap.txt"
    clean = clean_target(target)
    cmd = f"nmap -sV {clean}"
    run_command(cmd,output)
    return output

def run_gobuster(target):
    output = f"{OUTPUT_DIR}/gobuster.txt"
    cmd = f"gobuster dir -u {target} -w {WORDLIST} "
    run_command(cmd,output)
    return output

def run_nikto(target):
    output = f"{OUTPUT_DIR}/nikto.txt"
    cmd = f"nikto -h {target}"
    run_command(cmd , output)
    return output


#Parses 

def parse_nmap(file):
    ports = []
    with open(file,"r",errors="ignore") as f:
        for line in f:
            if "/tcp" in line and "opne" in line:
                ports.append(line.strip())

    return ports

def parse_gobuster(file):
    dirs =[]
    with open(file , "r",errors="ignore") as f:
        for line in f:
            if "/" in line:
                dirs.append(line.strip())
    return dirs

def parse_nikto(file):
    vuln = []
    with open(file ,"r",errors="ignore") as f:
        for line in f:
            if "+" in line:
                vuln.append(line.strip())
    return vuln


#Reports

def generate_report(target,ports , dirs , vuln ):
    timestmp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_file = f"{REPORT_DIR}/report_{timestmp}.md"

    with open(report_file,"w") as f:
        f.write(f"Scan Report\n\n")
        f.write(f"## Target\n{target}\n\n")

        f.write(f"## Open Ports\n")
        for p in ports:
            f.write(f"- {p}\n")

        f.write("\n## Directories Found\n")
        for d in dirs:
            f.write(f"- {d}\n")

        f.write("\n## Vulnerabilities (Nikto)\n")
        for i in vuln:
            f.write(f"- {i}\n")

    print(f"[+] Report saved: {report_file}")


#Main 

def main():
    parser = argparse.ArgumentParser(description="Mini Cybersecurity Scanner")
    parser.add_argument("--target", required=True, help="Target URL or IP")

    args = parser.parse_args()
    target = args.target

    print(f"[+] Starting scan on {target}")

    create_dirs()

    nmap_file = run_nmap(target)
    gobuster_file = run_gobuster(target)
    nikto_file = run_nikto(target)

    print("[+] Parsing results...")

    ports = parse_nmap(nmap_file)
    dirs = parse_gobuster(gobuster_file)
    vuln = parse_nikto(nikto_file)

    generate_report(target, ports, dirs, vuln)

    print("[+] Scan Completed!")


if __name__ == "__main__":
    main()

