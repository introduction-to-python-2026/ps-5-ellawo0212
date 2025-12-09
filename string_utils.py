


def split_before_uppercases(formula):
    start = 0
    end = 0
    split_formula = []
    if formula != "":
      for i in range(1 , len(formula)):
        end += 1
        if formula[i].isupper() == True:
          split_formula.append(formula[start : end])
          start = end
      split_formula.append(formula[start:len(formula)] )
      return split_formula
    else:
       return []
        
def split_at_digit(formula):
    digit_location = 1
    for i in range(1,len(formula)):
      if formula[i].isdigit():
        digit_location = i
        break
      else:
        digit_location += 1

    if digit_location == len(formula):
       return formula , 1 
    else:
      prefix = formula[:digit_location]
      numeric = int(formula[digit_location::])
      return prefix , numeric
        
def count_atoms_in_molecule(molecular_formula):
    """Takes a molecular formula (string) and returns a dictionary of atom counts.  
    Example: 'H2O' → {'H': 2, 'O': 1}"""
      mol_dict={}
  for i in split_before_uppercases(molecular_formula):
    per, num =split_at_digit(i)
    mol_dict[per] = num

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
