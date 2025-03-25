"""
Python and Memory - Global Interpreter Lock (GIL) Analysis

This module demonstrates the impact of Python's Global Interpreter Lock (GIL)
on concurrent execution of CPU-bound and I/O-bound tasks.
"""

import time
import threading
import multiprocessing
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from typing import List, Callable, Any, Dict, Tuple, Union


def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    # TODO: Implement the is_prime function
    pass


def cpu_intensive_task(n: int) -> int:
    """
    CPU-bound task that calculates the sum of prime numbers up to n.
    
    Args:
        n: Upper limit for prime number calculation
    
    Returns:
        Sum of all prime numbers from 2 to n
        
    Example:
        >>> cpu_intensive_task(10)
        17  # 2 + 3 + 5 + 7 = 17
        
    Note: 
        Special handling required for n ≤ 2, where there are no primes in range
    """
    # TODO: Implement the CPU intensive task
    # Hint: Use the is_prime function and sum primes from 2 up to n (inclusive)
    pass


def io_intensive_task(seconds: float) -> str:
    """
    I/O-bound task that simulates waiting for I/O operations.
    
    Args:
        seconds: Time to wait in seconds
    
    Returns:
        Confirmation message with the time waited
        
    Example:
        >>> io_intensive_task(0.1)
        'Completed I/O operation that took 0.1 seconds'
    """
    # TODO: Implement the I/O intensive task
    pass


def run_sequential(func: Callable, args_list: List) -> Tuple[List[Any], float]:
    """
    Run tasks sequentially and measure execution time.
    
    Args:
        func: The function to execute
        args_list: List of arguments to pass to the function
    
    Returns:
        Tuple containing results list and execution time in seconds
        
    Example:
        >>> run_sequential(cpu_intensive_task, [100, 200, 300])
    """
    # TODO: Implement sequential execution and timing
    pass


def run_threading(func: Callable, args_list: List, num_threads: int) -> Tuple[List[Any], float]:
    """
    Run tasks using threading and measure execution time.
    
    Args:
        func: The function to execute
        args_list: List of arguments to pass to the function
        num_threads: Number of threads to use
    
    Returns:
        Tuple containing results list and execution time in seconds
        
    Example:
        >>> run_threading(io_intensive_task, [0.1, 0.2, 0.3], 3)
    """
    # TODO: Implement threading execution and timing
    pass


def run_multiprocessing(func: Callable, args_list: List, num_processes: int) -> Tuple[List[Any], float]:
    """
    Run tasks using multiprocessing and measure execution time.
    
    Args:
        func: The function to execute
        args_list: List of arguments to pass to the function
        num_processes: Number of processes to use
    
    Returns:
        Tuple containing results list and execution time in seconds
        
    Example:
        >>> run_multiprocessing(cpu_intensive_task, [100, 200, 300], 3)
    """
    # TODO: Implement multiprocessing execution and timing
    pass


def compare_performance(task_type: str, task_func: Callable, args_list: List, 
                       num_workers: int) -> Dict[str, float]:
    """
    Compare different execution approaches for a given task.
    
    Args:
        task_type: Type of task ('CPU-bound' or 'I/O-bound')
        task_func: The function to execute
        args_list: List of arguments to pass to the function
        num_workers: Number of threads/processes to use
    
    Returns:
        Dictionary with execution times for each approach
        
    Example:
        >>> compare_performance('CPU-bound', cpu_intensive_task, [10000, 20000], 4)
    """
    # TODO: Implement performance comparison
    pass


def demonstrate_gil_contention() -> None:
    """
    Demonstrate GIL contention with a simple experiment.
    
    This function creates threads that increment a counter and shows
    how the GIL prevents true parallel execution.
    """
    # TODO: Implement GIL contention demonstration
    pass


def main() -> None:
    """
    Main function to demonstrate GIL effects on different task types.
    """
    print("Python GIL Analysis")
    print("=================")
    
    # TODO: Implement the main function to demonstrate all other functions
    pass


if __name__ == "__main__":
    main()