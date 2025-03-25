""" Functional tests for Python GIL Analysis solution. Tests the correctness of the implementation logic. """
import pytest
from python_gil_demonstration import (
    is_prime, cpu_intensive_task, io_intensive_task,
    run_sequential, run_threading, run_multiprocessing
)

class TestFunctional:
    """Test class for functional tests of the GIL analysis solution."""
    
    def test_prime_functions(self):
        """Test that prime detection functions work correctly."""
        # Prime numbers
        assert is_prime(2) == True
        assert is_prime(3) == True
        assert is_prime(5) == True
        assert is_prime(11) == True
        assert is_prime(997) == True  # Large prime
        
        # Non-prime numbers
        assert is_prime(0) == False
        assert is_prime(1) == False
        assert is_prime(4) == False
        assert is_prime(9) == False
    
    def test_cpu_task(self):
        """Test CPU-bound task functionality."""
        # Edge cases
        assert cpu_intensive_task(0) == 0
        assert cpu_intensive_task(1) == 0
        assert cpu_intensive_task(2) == 0
        
        # Normal cases
        assert cpu_intensive_task(3) == 5  # 2+3
        assert cpu_intensive_task(10) == 17  # 2+3+5+7
        assert cpu_intensive_task(15) == 41  # Sum of primes up to 15
    
    def test_io_task(self):
        """Test I/O-bound task functionality."""
        # Test with zero delay
        result_zero = io_intensive_task(0)
        assert "0 seconds" in result_zero
        
        # Test with small delay
        result = io_intensive_task(0.01)
        assert "Completed I/O operation" in result
        assert "0.01 seconds" in result
    
    def test_sequential_execution(self):
        """Test sequential execution method."""
        # Normal case
        args_list = [5, 10, 15]
        results, time = run_sequential(cpu_intensive_task, args_list)
        assert results == [10, 17, 41]
        assert time > 0
        
        # Empty list
        empty_results, _ = run_sequential(cpu_intensive_task, [])
        assert empty_results == []
    
    def test_threading_execution(self):
        """Test threading execution method."""
        # Normal case with multiple workers
        args_list = [5, 10, 15]
        results, time = run_threading(cpu_intensive_task, args_list, 2)
        assert sorted(results) == [10, 17, 41]
        assert time > 0
        
        # Empty list
        empty_results, _ = run_threading(cpu_intensive_task, [], 2)
        assert empty_results == []
        
        # Single worker
        single_results, _ = run_threading(cpu_intensive_task, args_list, 1)
        assert sorted(single_results) == [10, 17, 41]
        
        # More workers than tasks
        many_results, _ = run_threading(cpu_intensive_task, [5], 5)
        assert many_results == [10]
    
    def test_multiprocessing_execution(self):
        """Test multiprocessing execution method."""
        # Normal case with multiple workers
        args_list = [5, 10, 15]
        results, time = run_multiprocessing(cpu_intensive_task, args_list, 2)
        assert sorted(results) == [10, 17, 41]
        assert time > 0
        
        # Empty list
        empty_results, _ = run_multiprocessing(cpu_intensive_task, [], 2)
        assert empty_results == []
        
        # Single worker
        single_results, _ = run_multiprocessing(cpu_intensive_task, args_list, 1)
        assert sorted(single_results) == [10, 17, 41]
        
        # More workers than tasks
        many_results, _ = run_multiprocessing(cpu_intensive_task, [5], 5)
        assert many_results == [10]