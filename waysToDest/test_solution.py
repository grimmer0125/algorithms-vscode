from solution_fastest import solution_fastest
# from solution_permutations import start_parallel_estimation

def test_func():
    assert solution_fastest(10) == 492
    assert solution_fastest(610) == 14527490260516100855695859704819627818108010882741117227956927412305738742399171256642436462028811566617818991926058940988565927870172608545709804976244851391054850231415387973537361
    # assert start_parallel_estimation(10, num_process=1) == 492
