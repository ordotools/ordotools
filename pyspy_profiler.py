#!/usr/bin/env python3
"""
py-spy macOS compatibility script with multiple fallback approaches
"""

import subprocess
import sys
import os
import time
from datetime import datetime


def try_pyspy_variants(script_path, duration=15):
    """Try different py-spy configurations to work around macOS issues"""
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base_name = f"profile_{os.path.splitext(os.path.basename(script_path))[0]}_{timestamp}"
    
    # Different py-spy configurations to try
    variants = [
        {
            'name': 'Native mode (bypass some macOS restrictions)',
            'cmd': ['py-spy', 'record', '-o', f'{base_name}_native.svg', 
                   '-d', str(duration), '-r', '100', '-n', '--', 
                   sys.executable, script_path]
        },
        {
            'name': 'Subprocess mode (follow child processes)',
            'cmd': ['py-spy', 'record', '-o', f'{base_name}_subprocess.svg', 
                   '-d', str(duration), '-r', '100', '-s', '--', 
                   sys.executable, script_path]
        },
        {
            'name': 'Lower rate sampling',
            'cmd': ['py-spy', 'record', '-o', f'{base_name}_lowrate.svg', 
                   '-d', str(duration), '-r', '50', '--', 
                   sys.executable, script_path]
        },
        {
            'name': 'System python (bypass venv issues)',
            'cmd': ['py-spy', 'record', '-o', f'{base_name}_system.svg', 
                   '-d', str(duration), '-r', '100', '--', 
                   '/usr/bin/python3', script_path]
        },
        {
            'name': 'Short duration test',
            'cmd': ['py-spy', 'record', '-o', f'{base_name}_short.svg', 
                   '-d', '5', '-r', '200', '--', 
                   sys.executable, script_path]
        }
    ]
    
    for i, variant in enumerate(variants, 1):
        print(f"\n{'='*60}")
        print(f"🔄 Attempt {i}/{len(variants)}: {variant['name']}")
        print(f"{'='*60}")
        print(f"Command: {' '.join(variant['cmd'])}")
        
        try:
            result = subprocess.run(variant['cmd'], 
                                  capture_output=True, 
                                  text=True, 
                                  timeout=duration + 10)
            
            if result.returncode == 0:
                output_file = variant['cmd'][3]  # The -o parameter value
                if os.path.exists(output_file):
                    print(f"✅ SUCCESS! Profile saved to: {output_file}")
                    print(f"📊 File size: {os.path.getsize(output_file)} bytes")
                    
                    # Try to open it
                    try:
                        subprocess.run(['open', output_file])
                        print(f"🌐 Opened in browser")
                    except:
                        print(f"💡 Manually open: {os.path.abspath(output_file)}")
                    
                    return output_file
                else:
                    print(f"⚠️ Command succeeded but no file created")
            else:
                print(f"❌ Failed with return code: {result.returncode}")
                if result.stderr:
                    print(f"Error: {result.stderr}")
                if result.stdout:
                    print(f"Output: {result.stdout}")
                    
        except subprocess.TimeoutExpired:
            print(f"⏰ Timeout after {duration + 10} seconds")
        except Exception as e:
            print(f"❌ Exception: {e}")
    
    print(f"\n❌ All py-spy variants failed. Trying alternative approaches...")
    return None


def try_alternative_profilers(script_path):
    """Try alternative profiling methods"""
    print(f"\n{'='*60}")
    print(f"🔄 TRYING ALTERNATIVE PROFILERS")
    print(f"{'='*60}")
    
    # 1. Austin profiler
    try:
        print(f"🔍 Trying austin profiler...")
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'austin-python'], 
                      capture_output=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        austin_out = f"austin_profile_{timestamp}.txt"
        
        cmd = ['austin', '-i', '1000', '-t', '10000', 'python3', script_path]
        with open(austin_out, 'w') as f:
            result = subprocess.run(cmd, stdout=f, stderr=subprocess.PIPE, text=True)
        
        if result.returncode == 0 and os.path.getsize(austin_out) > 0:
            print(f"✅ Austin profile saved: {austin_out}")
            
            # Try to convert to flame graph
            try:
                subprocess.run([sys.executable, '-m', 'pip', 'install', 'austin2flamegraph'], 
                              capture_output=True)
                svg_file = austin_out.replace('.txt', '.svg')
                subprocess.run(['austin2flamegraph', austin_out, svg_file])
                if os.path.exists(svg_file):
                    print(f"🔥 Flame graph: {svg_file}")
                    subprocess.run(['open', svg_file])
                    return svg_file
            except:
                pass
            
            return austin_out
            
    except Exception as e:
        print(f"⚠️ Austin failed: {e}")
    
    # 2. cProfile with snakeviz
    try:
        print(f"🔍 Falling back to cProfile + SnakeViz...")
        
        # Create a wrapper script that profiles the target
        wrapper_content = f"""
import cProfile
import pstats
import sys
import os

# Profile the target script
pr = cProfile.Profile()

# Read and execute the script
with open('{script_path}', 'r') as f:
    script_content = f.read()

script_globals = {{
    '__file__': '{script_path}',
    '__name__': '__main__'
}}

pr.enable()
exec(script_content, script_globals)
pr.disable()

# Save profile
timestamp = '{datetime.now().strftime("%Y%m%d_%H%M%S")}'
prof_file = f'cprofile_{{timestamp}}.prof'
pr.dump_stats(prof_file)

print(f"Profile saved to: {{prof_file}}")
print(f"View with: snakeviz {{prof_file}}")
"""
        
        wrapper_file = 'profile_wrapper.py'
        with open(wrapper_file, 'w') as f:
            f.write(wrapper_content)
        
        # Run the wrapper
        result = subprocess.run([sys.executable, wrapper_file], 
                              capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"✅ cProfile completed")
            if result.stdout:
                print(result.stdout)
            
            # Try to start snakeviz
            try:
                print("📦 Installing/updating SnakeViz...")
                subprocess.run([sys.executable, '-m', 'pip', 'install', 'snakeviz'], 
                              capture_output=True, check=True)
                
                # Find the profile file
                prof_files = [f for f in os.listdir('.') if f.startswith('cprofile_') and f.endswith('.prof')]
                if prof_files:
                    latest_prof = max(prof_files, key=os.path.getmtime)
                    print(f"🚀 Starting SnakeViz for {latest_prof}")
                    print(f"🌐 This should open your browser automatically...")
                    print(f"💡 If not, manually go to: http://localhost:8080")
                    
                    # Start SnakeViz and wait
                    snakeviz_process = subprocess.Popen([
                        sys.executable, '-m', 'snakeviz', 
                        latest_prof, '--server'
                    ])
                    
                    print(f"\n{'='*50}")
                    print(f"🔥 SNAKEVIZ RUNNING")
                    print(f"{'='*50}")
                    print(f"Profile: {latest_prof}")
                    print(f"URL: http://localhost:8080")
                    print(f"Press Ctrl+C to stop")
                    print(f"{'='*50}")
                    
                    try:
                        snakeviz_process.wait()
                    except KeyboardInterrupt:
                        print(f"\n🛑 Stopping SnakeViz...")
                        snakeviz_process.terminate()
                        print(f"✅ SnakeViz stopped")
                    
                    return latest_prof
                else:
                    print(f"⚠️ No profile files found")
            except Exception as e:
                print(f"⚠️ SnakeViz failed: {e}")
                print(f"💡 Try manually: pip install snakeviz && snakeviz cprofile_*.prof")
        else:
            print(f"❌ cProfile failed: {result.stderr}")
            
    except Exception as e:
        print(f"⚠️ cProfile approach failed: {e}")
    
    return None


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print(f"  {sys.argv[0]} <script.py> [duration]")
        print()
        print("Example:")
        print(f"  {sys.argv[0]} extendedRun.py 15")
        sys.exit(1)
    
    script_path = sys.argv[1]
    duration = int(sys.argv[2]) if len(sys.argv) > 2 else 15
    
    if not os.path.exists(script_path):
        print(f"❌ File not found: {script_path}")
        sys.exit(1)
    
    print(f"🔍 macOS-Compatible Profiling for: {script_path}")
    print(f"⏱️ Duration: {duration} seconds")
    print(f"🐍 Python: {sys.executable}")
    
    # First try py-spy variants
    result = try_pyspy_variants(script_path, duration)
    
    # If py-spy fails completely, try alternatives
    if result is None:
        result = try_alternative_profilers(script_path)
    
    if result:
        print(f"\n✅ Profiling successful!")
        print(f"📁 Result: {result}")
    else:
        print(f"\n❌ All profiling methods failed")
        print(f"💡 Try running your script directly to see if there are any issues:")
        print(f"   python3 {script_path}")


if __name__ == "__main__":
    main()
