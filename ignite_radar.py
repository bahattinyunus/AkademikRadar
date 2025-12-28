import sys
import os
import argparse
from colorama import init, Fore, Style

# Add src to path to allow imports
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from akademik_radar.core import AcademicRadarEngine

# Initialize colorama
init(autoreset=True)

def main():
    parser = argparse.ArgumentParser(description="Akademik Radar - Elite Intelligence CLI")
    parser.add_argument('--scan', action='store_true', help='Initialize Trend Frequency Scanning')
    parser.add_argument('--network', action='store_true', help='Render Holographic Citation Network')
    parser.add_argument('--full', action='store_true', help='Execute Full System Diagnostics & Intelligence Gathering')
    
    args = parser.parse_args()
    
    engine = AcademicRadarEngine()
    
    # ASCII Art Splash Screen
    splash = f"""
{Fore.CYAN}
    Example ASCII Art Placeholder - Imagine a cool Radar Dish here
    :::   AKADEMIK RADAR   :::
    :::   V 2.0 (ELITE)    :::
{Style.RESET_ALL}
    """
    # Simply using a header instead of full complex art to save lines, 
    # but the core logic prints "AKADEMIK RADAR SISTEMI BAŞLATILIYOR" widely.
    
    if len(sys.argv) == 1:
        # If no arguments, just ignite the system to show it works, then print help
        engine.ignite_system()
        print("\n" + Fore.YELLOW + "Usage Hint: Try 'python ignite_radar.py --full' for the complete experience." + Style.RESET_ALL)
        # parser.print_help() # Optional: Don't show help immediately to keep it clean
    else:
        if args.full:
            engine.ignite_system()
            engine.scan_trends()
            engine.map_network()
        else:
            if args.scan:
                engine.ignite_system()
                engine.scan_trends()
            if args.network:
                if not args.scan: # If scan didn't already ignite
                     engine.ignite_system()
                engine.map_network()

if __name__ == "__main__":
    main()
