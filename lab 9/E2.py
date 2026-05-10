import re


input_file = "contamination_analysis.txt"
output_dir = "."

levels = ['Level_0', 'Level_1', 'Level_2', 'Level_3', 'Level_4']
categorized = {level: [] for level in levels}

with open(input_file, 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        match = re.match(r'^(\S+)\s+(\S+)$', line)
        if not match:
            continue

        chemical_name = match.group(1)
        formula = match.group(2)

        elements = {}
        for token in formula.split('-'):
            token_match = re.match(r'([A-Z][a-z]*)(\d*)', token)
            if token_match:
                symbol = token_match.group(1)
                count = int(token_match.group(2)) if token_match.group(2) else 1
                elements[symbol] = elements.get(symbol, 0) + count

        remaining = dict(elements)
        matched_levels = []

        if remaining.get('S', 0) >= 1 and remaining.get('O', 0) >= 4 and remaining.get('Na', 0) >= 1:
            matched_levels.append('Level_1')
            for symbol, count in {'S': 1, 'O': 4, 'Na': 1}.items():
                remaining[symbol] -= count
                if remaining[symbol] == 0:
                    del remaining[symbol]

        if remaining.get('S', 0) >= 1 and remaining.get('O', 0) >= 3 and remaining.get('Mg', 0) >= 1:
            matched_levels.append('Level_2')
            for symbol, count in {'S': 1, 'O': 3, 'Mg': 1}.items():
                remaining[symbol] -= count
                if remaining[symbol] == 0:
                    del remaining[symbol]

        if remaining.get('O', 0) >= 2 and remaining.get('Cl', 0) >= 3:
            matched_levels.append('Level_3')

        if len(matched_levels) > 1:
            category = 'Level_4'
        elif len(matched_levels) == 1:
            category = matched_levels[0]
        else:
            category = 'Level_0'

        categorized[category].append(chemical_name)

for level in levels:
    with open(f"{output_dir}/{level}.txt", 'w') as f:
        for name in categorized[level]:
            f.write(name + '\n')
