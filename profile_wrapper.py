
import cProfile
import pstats
import sys
import os

# Profile the target script
pr = cProfile.Profile()

# Read and execute the script
with open('extendedRun.py', 'r') as f:
    script_content = f.read()

script_globals = {
    '__file__': 'extendedRun.py',
    '__name__': '__main__'
}

pr.enable()
exec(script_content, script_globals)
pr.disable()

# Save profile
timestamp = '20250703_155607'
prof_file = f'cprofile_{timestamp}.prof'
pr.dump_stats(prof_file)

print(f"Profile saved to: {prof_file}")
print(f"View with: snakeviz {prof_file}")
