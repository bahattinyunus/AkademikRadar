import unittest
import sys
import os

# Add src to path
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'src'))

from akademik_radar.core import AcademicRadarEngine

class TestAcademicRadar(unittest.TestCase):
    def setUp(self):
        self.engine = AcademicRadarEngine()

    def test_initialization(self):
        self.assertIsNotNone(self.engine)
        self.assertGreater(len(self.engine.modules), 0)

    def test_trend_scan_simulation(self):
        results = self.engine.scan_trends()
        self.assertIsInstance(results, dict)
        self.assertIn("Quantum Computing", results)
        
    def test_network_mapping_simulation(self):
        results = self.engine.map_network()
        self.assertEqual(results['nodes'], 14502)

if __name__ == '__main__':
    unittest.main()
