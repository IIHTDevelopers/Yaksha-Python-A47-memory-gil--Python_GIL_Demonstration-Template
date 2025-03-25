""" Boundary tests for Python GIL Analysis solution. Tests edge cases and limits of the implementation. """
import pytest
from python_gil_demonstration import (
    is_prime, cpu_intensive_task, io_intensive_task,
    run_sequential, run_threading, run_multiprocessing
)

class TestBoundary:
    """Test class for boundary tests of the GIL analysis solution."""
    
    def test_combined_boundary_cases(self):
        """Combined boundary cases test."""
        # Prime edge cases
        assert is_prime(0) == False
        assert is_prime(1) == False
        assert is_prime(2) == True  # Smallest prime
        assert is_prime(997) == True  # A known large prime
        
        # CPU task with small values
        assert cpu_intensive_task(0) == 0
        assert cpu_intensive_task(1) == 0
        assert cpu_intensive_task(2) == 0
        assert cpu_intensive_task(3) == 5  # Sum of 2+3
        
        # IO task with zero delay
        assert "0 seconds" in io_intensive_task(0)
        
        # Empty args list for all execution methods
        assert run_sequential(cpu_intensive_task, [])[0] == []
        assert run_threading(cpu_intensive_task, [], 2)[0] == []
        assert run_multiprocessing(cpu_intensive_task, [], 2)[0] == []
        
        # Single worker vs many workers
        args_list = [5]
        single_thread = run_threading(cpu_intensive_task, args_list, 1)[0]
        multi_thread = run_threading(cpu_intensive_task, args_list, 5)[0]
        assert single_thread == multi_thread == [10]
        
        mp_single = run_multiprocessing(cpu_intensive_task, args_list, 1)[0]
        mp_multi = run_multiprocessing(cpu_intensive_task, args_list, 5)[0]
        assert mp_single == mp_multi == [10]