""" Exceptional tests for Python GIL Analysis solution. Tests error handling and exception cases. """
import pytest
from python_gil_demonstration import (
    run_sequential, run_threading, run_multiprocessing,
    compare_performance
)

class TestExceptional:
    """Test class for exceptional tests of the GIL analysis solution."""
    
    def test_combined_exception_handling(self):
        """Combined exception handling test."""
        # Invalid function type
        invalid_func = "not a function"
        args_list = [1, 2, 3]
        
        # Should raise TypeError for all execution methods
        with pytest.raises(TypeError):
            run_sequential(invalid_func, args_list)
        
        with pytest.raises(TypeError):
            run_threading(invalid_func, args_list, 2)
        
        with pytest.raises(TypeError):
            run_multiprocessing(invalid_func, args_list, 2)
        
        # Invalid worker counts
        def dummy_func(x):
            return x
        
        # Zero workers
        with pytest.raises(ValueError):
            run_threading(dummy_func, args_list, 0)
        
        with pytest.raises(ValueError):
            run_multiprocessing(dummy_func, args_list, 0)
        
        # Negative workers
        with pytest.raises(ValueError):
            run_threading(dummy_func, args_list, -1)
        
        with pytest.raises(ValueError):
            run_multiprocessing(dummy_func, args_list, -2)
        
        # Invalid task_type
        with pytest.raises(ValueError):
            compare_performance("INVALID_TYPE", dummy_func, args_list, 2)