"""Rulează un exercițiu individual sau toate cele 50 de exerciții."""
import argparse
import runpy
import sys
from pathlib import Path


def main():
    """Pregătește importul webtools și execută exercițiile selectate."""
    parser = argparse.ArgumentParser(description='Exerciții individuale')
    parser.add_argument('number', nargs='?', type=int, choices=range(1,51))
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    sys.path.insert(0, str(root))
    numbers = [args.number] if args.number else range(1,51)
    for number in numbers:
        path = root / f'exercises/ex{number:02d}.py'
        sys.argv = [str(path)]
        if number == 48:
            sys.argv.append('https://cybercor.org')
        print(f'=== Exercițiul {number} ===')
        runpy.run_path(str(path), run_name='__main__')


if __name__ == '__main__':
    main()
