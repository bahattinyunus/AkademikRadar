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
    parser = argparse.ArgumentParser(description="Akademik Radar CLI")
    parser.add_argument('--scan', action='store_true', help='Trend taraması başlat')
    parser.add_argument('--network', action='store_true', help='Ağ analizi simülasyonu')
    parser.add_argument('--full', action='store_true', help='Tam sistem taraması')
    
    args = parser.parse_args()
    
    engine = AcademicRadarEngine()
    
    if len(sys.argv) == 1:
        engine.ignite_system()
        parser.print_help()
    else:
        if args.full or args.scan:
            engine.ignite_system()
            engine.scan_trends()
        if args.full or args.network:
            # Ignite only if not already ignited/full scan not running (logic simplified)
            if not args.full: engine.ignite_system()
            engine.map_network()

if __name__ == "__main__":
    main()
