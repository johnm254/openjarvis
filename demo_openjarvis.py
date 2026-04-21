#!/usr/bin/env python3
"""
OpenJarvis Demo Script
This demonstrates how to use OpenJarvis programmatically
"""

from openjarvis import Jarvis

# Initialize Jarvis
jarvis = Jarvis()

# Simple question
print("=" * 60)
print("Demo 1: Simple Question")
print("=" * 60)
response = jarvis.ask("What is the capital of France?")
print(f"Answer: {response}")

# Math question
print("\n" + "=" * 60)
print("Demo 2: Math Question")
print("=" * 60)
response = jarvis.ask("Calculate 15 * 23 + 47")
print(f"Answer: {response}")

# Code explanation
print("\n" + "=" * 60)
print("Demo 3: Code Explanation")
print("=" * 60)
code = """
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
"""
response = jarvis.ask(f"Explain this code:\n{code}")
print(f"Answer: {response}")

print("\n" + "=" * 60)
print("Demo Complete!")
print("=" * 60)
