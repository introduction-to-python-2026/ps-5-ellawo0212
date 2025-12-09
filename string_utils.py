def split_before_each_uppercases(formula):
  split_formula = []
  start = 0
  end = 1
  if formula != "":
    for i in range(1, len(formula)):
      if formula[i].isupper():
        end = i
        split_formula.append(formula[start:end])
        start = i
    split_formula.append(formula[start:len(formula)])
    return split_formula
  else:
    return []

def split_at_first_digit(formula):
  digit_location = 1
  for i in range(1, len(formula)):
    if formula[i].isdigit() == True:
      break
    else:
      digit_location += 1
  if digit_location == len(formula):
    return formula, 1
  else:
    prefix = formula[:digit_location]
    numeric = int(formula[digit_location::])
    return prefix,numeric

def count_atoms_in_molecule(molecular_formula):
    """Takes a molecular formula (string) and returns a dictionary of atom counts.
    Example: 'H2O' → {'H': 2, 'O': 1}"""
    atom_count = {}
    for i in split_before_each_uppercases(molecular_formula):
      atom , count= split_at_first_digit(i)
      atom_count[atom] = count
    return atom_count

def parse_chemical_reaction(reaction_equation):
    """Takes a reaction equation (string) and returns reactants and products as lists.  
    Example: 'H2 + O2 -> H2O' → (['H2', 'O2'], ['H2O'])"""
    reaction_equation = reaction_equation.replace(" ", "")  # Remove spaces for easier parsing
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")

def count_atoms_in_reaction(molecules_list):
    """Takes a list of molecular formulas and returns a list of atom count dictionaries.  
    Example: ['H2', 'O2'] → [{'H': 2}, {'O': 2}]"""
    molecules_atoms_count = []
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(molecule))
    return molecules_atoms_count
