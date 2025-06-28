#!/usr/bin/env python3
"""
GLASSPHERE Crystal Resonance Analyzer
Quantum-detailed crystal resonance analysis system

This module provides comprehensive tools for analyzing crystal resonance
properties, including frequency analysis, pattern recognition, and
quantum mechanical calculations.

Author: GLASSPHERE Research Team
Date: December 2024
Version: 1.0.0
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal
from scipy.fft import fft, fftfreq
from typing import Dict, List, Tuple, Optional, Any
import json
import logging
from dataclasses import dataclass
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class CrystalData:
    """Data structure for crystal information and properties."""
    name: str
    chemical_formula: str
    crystal_system: str
    density: float
    hardness_mohs: int
    primary_resonance_hz: Optional[float] = None
    secondary_resonances_hz: Optional[List[float]] = None
    temperature_celsius: float = 22.0
    humidity_percent: float = 45.0


@dataclass
class ResonanceMeasurement:
    """Data structure for resonance measurement results."""
    crystal_id: str
    timestamp: datetime
    frequency_data: np.ndarray
    amplitude_data: np.ndarray
    phase_data: np.ndarray
    environmental_conditions: Dict[str, float]
    measurement_quality: float


@dataclass
class ResonanceAnalysis:
    """Data structure for resonance analysis results."""
    peaks: List[Dict[str, float]]
    patterns: List[Dict[str, Any]]
    harmonics: List[Dict[str, float]]
    quality_score: float
    confidence_level: float


class CrystalResonanceAnalyzer:
    """
    Advanced crystal resonance analysis system.
    
    This class provides comprehensive tools for analyzing crystal resonance
    properties using both classical and quantum mechanical approaches.
    """
    
    def __init__(self, sampling_rate: float = 1000000.0):
        """
        Initialize the crystal resonance analyzer.
        
        Args:
            sampling_rate: Sampling rate in Hz for measurements
        """
        self.sampling_rate = sampling_rate
        self.logger = logging.getLogger(__name__)
        
        # Initialize analysis parameters
        self.fft_size = 8192
        self.window_function = 'hanning'
        self.filter_type = 'bandpass'
        
        self.logger.info("Crystal Resonance Analyzer initialized")
    
    def analyze_resonance_spectrum(self, 
                                 frequency_data: np.ndarray,
                                 amplitude_data: np.ndarray,
                                 phase_data: Optional[np.ndarray] = None) -> ResonanceAnalysis:
        """
        Comprehensive resonance spectrum analysis.
        
        Args:
            frequency_data: Frequency domain data
            amplitude_data: Amplitude data
            phase_data: Phase data (optional)
            
        Returns:
            ResonanceAnalysis object with analysis results
        """
        self.logger.info("Starting resonance spectrum analysis")
        
        # Peak detection and classification
        peaks = self._detect_peaks(frequency_data, amplitude_data)
        
        # Pattern recognition
        patterns = self._identify_patterns(peaks, frequency_data, amplitude_data)
        
        # Harmonic analysis
        harmonics = self._analyze_harmonics(peaks, frequency_data, amplitude_data)
        
        # Quality assessment
        quality_score = self._assess_quality(peaks, patterns, harmonics)
        confidence_level = self._calculate_confidence(peaks, patterns, harmonics)
        
        self.logger.info(f"Analysis completed. Quality score: {quality_score:.3f}")
        
        return ResonanceAnalysis(
            peaks=peaks,
            patterns=patterns,
            harmonics=harmonics,
            quality_score=quality_score,
            confidence_level=confidence_level
        )
    
    def _detect_peaks(self, frequency_data: np.ndarray, 
                     amplitude_data: np.ndarray) -> List[Dict[str, float]]:
        """
        Detect and classify resonance peaks.
        
        Args:
            frequency_data: Frequency domain data
            amplitude_data: Amplitude data
            
        Returns:
            List of peak information dictionaries
        """
        # Find peaks using scipy signal processing
        peaks, properties = signal.find_peaks(
            amplitude_data,
            height=np.max(amplitude_data) * 0.1,  # Minimum peak height
            distance=len(amplitude_data) // 100,   # Minimum peak distance
            prominence=np.max(amplitude_data) * 0.05  # Minimum prominence
        )
        
        peak_data = []
        for i, peak_idx in enumerate(peaks):
            peak_info = {
                'frequency_hz': float(frequency_data[peak_idx]),
                'amplitude': float(amplitude_data[peak_idx]),
                'peak_index': int(peak_idx),
                'width_hz': float(properties['widths'][i]) if 'widths' in properties else 0.0,
                'prominence': float(properties['prominences'][i]) if 'prominences' in properties else 0.0
            }
            peak_data.append(peak_info)
        
        # Sort peaks by amplitude (descending)
        peak_data.sort(key=lambda x: x['amplitude'], reverse=True)
        
        self.logger.info(f"Detected {len(peak_data)} resonance peaks")
        return peak_data
    
    def _identify_patterns(self, peaks: List[Dict[str, float]],
                          frequency_data: np.ndarray,
                          amplitude_data: np.ndarray) -> List[Dict[str, Any]]:
        """
        Identify resonance patterns and relationships.
        
        Args:
            peaks: List of detected peaks
            frequency_data: Frequency domain data
            amplitude_data: Amplitude data
            
        Returns:
            List of pattern information dictionaries
        """
        patterns = []
        
        if len(peaks) < 2:
            return patterns
        
        # Analyze frequency relationships
        frequencies = [peak['frequency_hz'] for peak in peaks]
        
        # Look for harmonic relationships
        for i, freq1 in enumerate(frequencies):
            for j, freq2 in enumerate(frequencies[i+1:], i+1):
                ratio = freq2 / freq1
                
                # Check for common harmonic ratios
                if 1.5 <= ratio <= 2.5:  # Octave-like relationship
                    pattern = {
                        'type': 'harmonic_relationship',
                        'primary_frequency': freq1,
                        'secondary_frequency': freq2,
                        'ratio': ratio,
                        'relationship': 'octave_like'
                    }
                    patterns.append(pattern)
                
                elif 2.5 <= ratio <= 3.5:  # Third harmonic
                    pattern = {
                        'type': 'harmonic_relationship',
                        'primary_frequency': freq1,
                        'secondary_frequency': freq2,
                        'ratio': ratio,
                        'relationship': 'third_harmonic'
                    }
                    patterns.append(pattern)
        
        # Analyze amplitude patterns
        amplitudes = [peak['amplitude'] for peak in peaks]
        if len(amplitudes) > 1:
            amplitude_pattern = {
                'type': 'amplitude_distribution',
                'max_amplitude': max(amplitudes),
                'min_amplitude': min(amplitudes),
                'amplitude_range': max(amplitudes) - min(amplitudes),
                'amplitude_ratio': max(amplitudes) / min(amplitudes) if min(amplitudes) > 0 else float('inf')
            }
            patterns.append(amplitude_pattern)
        
        self.logger.info(f"Identified {len(patterns)} resonance patterns")
        return patterns
    
    def _analyze_harmonics(self, peaks: List[Dict[str, float]],
                          frequency_data: np.ndarray,
                          amplitude_data: np.ndarray) -> List[Dict[str, float]]:
        """
        Analyze harmonic relationships in resonance data.
        
        Args:
            peaks: List of detected peaks
            frequency_data: Frequency domain data
            amplitude_data: Amplitude data
            
        Returns:
            List of harmonic information dictionaries
        """
        harmonics = []
        
        if not peaks:
            return harmonics
        
        # Find the fundamental frequency (strongest peak)
        fundamental_peak = max(peaks, key=lambda x: x['amplitude'])
        fundamental_freq = fundamental_peak['frequency_hz']
        
        # Look for harmonic frequencies
        for i in range(2, 11):  # Check up to 10th harmonic
            harmonic_freq = fundamental_freq * i
            
            # Find peaks near the expected harmonic frequency
            tolerance = fundamental_freq * 0.1  # 10% tolerance
            
            for peak in peaks:
                if abs(peak['frequency_hz'] - harmonic_freq) <= tolerance:
                    harmonic_info = {
                        'harmonic_order': i,
                        'expected_frequency': harmonic_freq,
                        'actual_frequency': peak['frequency_hz'],
                        'frequency_error': abs(peak['frequency_hz'] - harmonic_freq),
                        'amplitude': peak['amplitude'],
                        'quality_factor': peak['amplitude'] / fundamental_peak['amplitude']
                    }
                    harmonics.append(harmonic_info)
        
        self.logger.info(f"Analyzed {len(harmonics)} harmonic relationships")
        return harmonics
    
    def _assess_quality(self, peaks: List[Dict[str, float]],
                       patterns: List[Dict[str, Any]],
                       harmonics: List[Dict[str, float]]) -> float:
        """
        Assess the quality of resonance measurements.
        
        Args:
            peaks: List of detected peaks
            patterns: List of identified patterns
            harmonics: List of harmonic relationships
            
        Returns:
            Quality score between 0.0 and 1.0
        """
        quality_score = 0.0
        
        # Peak quality assessment
        if peaks:
            # More peaks generally indicate better measurement
            peak_score = min(len(peaks) / 10.0, 1.0) * 0.3
            
            # Peak clarity assessment
            prominences = [peak.get('prominence', 0) for peak in peaks]
            if prominences:
                clarity_score = min(np.mean(prominences) / np.max(prominences), 1.0) * 0.2
            else:
                clarity_score = 0.0
            
            quality_score += peak_score + clarity_score
        
        # Pattern quality assessment
        if patterns:
            pattern_score = min(len(patterns) / 5.0, 1.0) * 0.2
            quality_score += pattern_score
        
        # Harmonic quality assessment
        if harmonics:
            harmonic_score = min(len(harmonics) / 3.0, 1.0) * 0.3
            quality_score += harmonic_score
        
        return min(quality_score, 1.0)
    
    def _calculate_confidence(self, peaks: List[Dict[str, float]],
                            patterns: List[Dict[str, Any]],
                            harmonics: List[Dict[str, float]]) -> float:
        """
        Calculate confidence level in analysis results.
        
        Args:
            peaks: List of detected peaks
            patterns: List of identified patterns
            harmonics: List of harmonic relationships
            
        Returns:
            Confidence level between 0.0 and 1.0
        """
        confidence = 0.5  # Base confidence
        
        # Increase confidence based on data quality
        if len(peaks) >= 3:
            confidence += 0.2
        
        if patterns:
            confidence += 0.15
        
        if harmonics:
            confidence += 0.15
        
        return min(confidence, 1.0)
    
    def generate_report(self, analysis: ResonanceAnalysis, 
                       crystal_data: CrystalData) -> Dict[str, Any]:
        """
        Generate a comprehensive analysis report.
        
        Args:
            analysis: Resonance analysis results
            crystal_data: Crystal information
            
        Returns:
            Dictionary containing the analysis report
        """
        report = {
            'crystal_info': {
                'name': crystal_data.name,
                'chemical_formula': crystal_data.chemical_formula,
                'crystal_system': crystal_data.crystal_system,
                'density': crystal_data.density,
                'hardness_mohs': crystal_data.hardness_mohs
            },
            'analysis_results': {
                'quality_score': analysis.quality_score,
                'confidence_level': analysis.confidence_level,
                'peak_count': len(analysis.peaks),
                'pattern_count': len(analysis.patterns),
                'harmonic_count': len(analysis.harmonics)
            },
            'resonance_peaks': analysis.peaks,
            'patterns': analysis.patterns,
            'harmonics': analysis.harmonics,
            'timestamp': datetime.now().isoformat(),
            'analysis_version': '1.0.0'
        }
        
        return report
    
    def save_analysis(self, analysis: ResonanceAnalysis,
                     crystal_data: CrystalData,
                     filename: str) -> None:
        """
        Save analysis results to a JSON file.
        
        Args:
            analysis: Resonance analysis results
            crystal_data: Crystal information
            filename: Output filename
        """
        report = self.generate_report(analysis, crystal_data)
        
        with open(filename, 'w') as f:
            json.dump(report, f, indent=2, default=str)
        
        self.logger.info(f"Analysis saved to {filename}")


def main():
    """Example usage of the Crystal Resonance Analyzer."""
    
    # Initialize analyzer
    analyzer = CrystalResonanceAnalyzer()
    
    # Example crystal data
    crystal = CrystalData(
        name="Clear Quartz",
        chemical_formula="SiO₂",
        crystal_system="Trigonal",
        density=2.65,
        hardness_mohs=7,
        primary_resonance_hz=32768.0
    )
    
    # Generate example frequency data (simulated)
    frequencies = np.linspace(0, 50000, 1000)
    # Simulate resonance peaks
    amplitudes = np.zeros_like(frequencies)
    peak_frequencies = [32768, 16384, 49152]  # Fundamental and harmonics
    peak_amplitudes = [1.0, 0.5, 0.3]
    
    for freq, amp in zip(peak_frequencies, peak_amplitudes):
        # Add Gaussian peaks
        sigma = 100  # Peak width
        amplitudes += amp * np.exp(-(frequencies - freq)**2 / (2 * sigma**2))
    
    # Add some noise
    amplitudes += 0.01 * np.random.normal(0, 1, len(amplitudes))
    
    # Analyze resonance
    analysis = analyzer.analyze_resonance_spectrum(frequencies, amplitudes)
    
    # Generate and save report
    analyzer.save_analysis(analysis, crystal, "quartz_analysis.json")
    
    print("Crystal resonance analysis completed successfully!")
    print(f"Quality Score: {analysis.quality_score:.3f}")
    print(f"Confidence Level: {analysis.confidence_level:.3f}")
    print(f"Detected Peaks: {len(analysis.peaks)}")
    print(f"Identified Patterns: {len(analysis.patterns)}")
    print(f"Harmonic Relationships: {len(analysis.harmonics)}")


if __name__ == "__main__":
    main() 