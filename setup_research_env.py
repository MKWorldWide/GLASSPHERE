#!/usr/bin/env python3
"""
GLASSPHERE Research Environment Setup Script
Initializes the research environment and installs dependencies

Author: GLASSPHERE Research Team
Date: December 2024
Version: 1.0.0
"""

import os
import sys
import subprocess
import json
from pathlib import Path
from datetime import datetime

def print_banner():
    """Print the GLASSPHERE research initiative banner."""
    banner = """
    ╔══════════════════════════════════════════════════════════════╗
    ║                    🌟 GLASSPHERE RESEARCH 🌟                  ║
    ║                                                              ║
    ║         Quantum Resonance Research in Crystalline            ║
    ║              and Glass Materials Initiative                  ║
    ║                                                              ║
    ║                    Version 1.0.0                            ║
    ╚══════════════════════════════════════════════════════════════╝
    """
    print(banner)

def check_python_version():
    """Check if Python version meets requirements."""
    print("🔍 Checking Python version...")
    
    if sys.version_info < (3, 8):
        print("❌ Error: Python 3.8 or higher is required")
        print(f"   Current version: {sys.version}")
        sys.exit(1)
    
    print(f"✅ Python {sys.version.split()[0]} detected")
    return True

def create_directories():
    """Create necessary directories for the research project."""
    print("📁 Creating project directories...")
    
    directories = [
        "RESEARCH/experiments",
        "RESEARCH/data-analysis",
        "RESEARCH/literature-review",
        "CODE/resonance-calculator",
        "CODE/data-visualization",
        "CODE/simulation-models",
        "DOCUMENTATION/methodology",
        "DOCUMENTATION/experimental-setup",
        "DOCUMENTATION/data-collection",
        "DOCUMENTATION/analysis-framework",
        "APPLICATIONS/healing-modalities",
        "APPLICATIONS/energy-harvesting",
        "APPLICATIONS/communication-systems",
        "APPLICATIONS/construction-materials",
        "RESOURCES/academic-papers",
        "RESOURCES/multimedia",
        "RESOURCES/external-links",
        "logs",
        "data",
        "config"
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"   ✅ Created: {directory}")
    
    print("✅ All directories created successfully")

def install_dependencies():
    """Install Python dependencies from requirements.txt."""
    print("📦 Installing Python dependencies...")
    
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing dependencies: {e}")
        return False
    
    return True

def create_config_files():
    """Create configuration files for the research environment."""
    print("⚙️ Creating configuration files...")
    
    # Database configuration
    db_config = {
        "database": {
            "host": "localhost",
            "port": 5432,
            "name": "glassphere_research",
            "user": "research_user",
            "password": "change_this_password"
        },
        "redis": {
            "host": "localhost",
            "port": 6379,
            "db": 0
        },
        "influxdb": {
            "url": "http://localhost:8086",
            "token": "your_influxdb_token",
            "org": "glassphere_research",
            "bucket": "crystal_data"
        }
    }
    
    with open("config/database.json", "w") as f:
        json.dump(db_config, f, indent=2)
    
    # Research configuration
    research_config = {
        "measurement": {
            "sampling_rate_hz": 1000000,
            "fft_size": 8192,
            "window_function": "hanning",
            "filter_type": "bandpass"
        },
        "environmental_controls": {
            "temperature_celsius": 22.0,
            "humidity_percent": 45.0,
            "pressure_pa": 101325,
            "electromagnetic_shielding": "Faraday_cage"
        },
        "quality_standards": {
            "frequency_precision": 0.001,
            "amplitude_accuracy": 0.1,
            "phase_resolution": 0.1,
            "temperature_stability": 0.1
        }
    }
    
    with open("config/research.json", "w") as f:
        json.dump(research_config, f, indent=2)
    
    print("✅ Configuration files created")

def create_logging_config():
    """Create logging configuration."""
    print("📝 Setting up logging configuration...")
    
    logging_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "detailed": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            },
            "simple": {
                "format": "%(levelname)s - %(message)s"
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": "INFO",
                "formatter": "simple",
                "stream": "ext://sys.stdout"
            },
            "file": {
                "class": "logging.FileHandler",
                "level": "DEBUG",
                "formatter": "detailed",
                "filename": "logs/glassphere.log",
                "mode": "a"
            }
        },
        "loggers": {
            "": {
                "level": "DEBUG",
                "handlers": ["console", "file"]
            }
        }
    }
    
    with open("config/logging.json", "w") as f:
        json.dump(logging_config, f, indent=2)
    
    print("✅ Logging configuration created")

def create_research_metadata():
    """Create research metadata file."""
    print("📊 Creating research metadata...")
    
    metadata = {
        "project_info": {
            "name": "GLASSPHERE Research Initiative",
            "version": "1.0.0",
            "description": "Quantum Resonance Research in Crystalline and Glass Materials",
            "start_date": datetime.now().isoformat(),
            "status": "initialization"
        },
        "research_areas": [
            "Quantum Resonance Mapping",
            "Energy Field Interactions",
            "Resonance Amplification",
            "Practical Applications"
        ],
        "crystal_categories": [
            "Quartz Family",
            "Silicate Minerals",
            "Carbonate Minerals",
            "Sulfate Minerals"
        ],
        "measurement_protocols": [
            "Frequency Analysis",
            "Amplitude Measurement",
            "Phase Analysis",
            "Environmental Controls"
        ],
        "analysis_frameworks": [
            "Quantum Simulations",
            "Statistical Analysis",
            "Pattern Recognition",
            "Predictive Modeling"
        ]
    }
    
    with open("RESEARCH/research_metadata.json", "w") as f:
        json.dump(metadata, f, indent=2)
    
    print("✅ Research metadata created")

def run_tests():
    """Run basic tests to verify the setup."""
    print("🧪 Running basic tests...")
    
    try:
        # Test basic imports
        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt
        from scipy import signal
        
        print("   ✅ Scientific computing libraries imported successfully")
        
        # Test crystal analyzer
        sys.path.append("CODE/resonance-calculator")
        from crystal_analyzer import CrystalResonanceAnalyzer, CrystalData
        
        analyzer = CrystalResonanceAnalyzer()
        print("   ✅ Crystal analyzer initialized successfully")
        
        # Test configuration files
        with open("config/research.json", "r") as f:
            config = json.load(f)
        print("   ✅ Configuration files accessible")
        
        print("✅ All tests passed successfully")
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Test error: {e}")
        return False

def print_next_steps():
    """Print next steps for the research team."""
    print("\n" + "="*60)
    print("🎯 NEXT STEPS FOR GLASSPHERE RESEARCH")
    print("="*60)
    
    steps = [
        "1. Review and customize configuration files in config/",
        "2. Set up database connections and credentials",
        "3. Prepare crystal samples for initial testing",
        "4. Calibrate measurement equipment",
        "5. Begin data collection and analysis",
        "6. Document experimental procedures",
        "7. Establish quality control protocols",
        "8. Plan research publications and collaborations"
    ]
    
    for step in steps:
        print(f"   {step}")
    
    print("\n📚 Documentation:")
    print("   - README.md: Project overview and getting started")
    print("   - ARCHITECTURE.md: System design and methodology")
    print("   - CHANGELOG.md: Version history and updates")
    print("   - RESEARCH/crystal-database.md: Crystal catalog and properties")
    
    print("\n🔬 Research Tools:")
    print("   - CODE/resonance-calculator/: Crystal analysis tools")
    print("   - CODE/data-visualization/: Data visualization tools")
    print("   - CODE/simulation-models/: Quantum simulation frameworks")
    
    print("\n🌟 Welcome to the GLASSPHERE Research Initiative!")
    print("   Advancing crystal resonance research for a quantum future")

def main():
    """Main setup function."""
    print_banner()
    
    print("🚀 Initializing GLASSPHERE Research Environment...\n")
    
    # Check Python version
    if not check_python_version():
        return
    
    # Create directories
    create_directories()
    
    # Install dependencies
    if not install_dependencies():
        print("❌ Setup failed during dependency installation")
        return
    
    # Create configuration files
    create_config_files()
    create_logging_config()
    create_research_metadata()
    
    # Run tests
    if not run_tests():
        print("❌ Setup failed during testing")
        return
    
    print("\n✅ GLASSPHERE Research Environment setup completed successfully!")
    
    # Print next steps
    print_next_steps()

if __name__ == "__main__":
    main() 