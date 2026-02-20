#!/usr/bin/env python3
"""
Script to create a new exercise file with sequential numbering.
Asks user for exercise name and creates a file in the solution folder.
"""

import os
import re
from pathlib import Path


def get_next_exercise_number(solution_folder):
    """
    Find the highest exercise number in the solution folder and return next number.
    
    Args:
        solution_folder (Path): Path to the solution folder
        
    Returns:
        int: The next exercise number
    """
    max_number = 0
    
    # Get all Python files in the solution folder
    if solution_folder.exists():
        for file in solution_folder.glob("*.py"):
            # Extract number from filename using regex
            match = re.match(r"^(\d+)_", file.name)
            if match:
                number = int(match.group(1))
                max_number = max(max_number, number)
    
    return max_number + 1


def format_exercise_name(name):
    """
    Format exercise name for filename (lowercase, replace spaces with underscores).
    
    Args:
        name (str): Exercise name from user
        
    Returns:
        str: Formatted name for filename
    """
    # Convert to lowercase and replace spaces with underscores
    formatted = name.strip().lower().replace(" ", "_")
    # Remove any special characters except underscores
    formatted = re.sub(r"[^a-z0-9_]", "", formatted)
    return formatted


def create_exercise_file(exercise_name, solution_folder=None):
    """
    Create a new exercise file with sequential numbering.
    
    Args:
        exercise_name (str): Name of the exercise
        solution_folder (Path): Path to solution folder (default: ./solution)
    """
    if solution_folder is None:
        solution_folder = Path("solution")
    else:
        solution_folder = Path(solution_folder)
    
    # Ensure solution folder exists
    solution_folder.mkdir(exist_ok=True)
    
    # Get next exercise number
    next_number = get_next_exercise_number(solution_folder)
    
    # Format the exercise name
    formatted_name = format_exercise_name(exercise_name)
    
    # Create filename
    filename = f"{next_number:02d}_{formatted_name}.py"
    filepath = solution_folder / filename
    
    # Check if file already exists
    if filepath.exists():
        print(f"Error: File {filename} already exists!")
        return False
    
    # Create the file with a template
    template = f'''"""
Exercise {next_number}: {exercise_name}
"""


def main():
    """Main function for exercise {next_number}."""
    pass


if __name__ == "__main__":
    main()
'''
    
    with open(filepath, "w") as f:
        f.write(template)
    
    print(f"✓ Created: {filename}")
    print(f"  Path: {filepath}")
    return True


def main():
    """Main entry point for the script."""
    print("=" * 50)
    print("Exercise File Creator")
    print("=" * 50)
    
    # Get exercise name from user
    exercise_name = input("\nEnter exercise name: ").strip()
    
    if not exercise_name:
        print("Error: Exercise name cannot be empty!")
        return
    
    # Create the file
    create_exercise_file(exercise_name)
    print("\nDone!")


if __name__ == "__main__":
    main()
