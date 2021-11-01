import os
import json

from git import Repo
from rmgpy.molecule.molecule import *
from rmgpy.species import *
from rmgpy.data.rmg import RMGDatabase
from rmgpy.species import Species
from rmgpy import settings


def save_sensitivity(family):
    """
    Function to compute partial sensitivities once 
    """
    templateRxnMap = family.get_reaction_matches(
        thermo_database=database.thermo,
        remove_degeneracy=True,
        get_reverse=True,
        exact_matches_only=False,
        fix_labels=True
    )
    family.compute_sensitivities(templateRxnMap)
    family.check_tree()
    family.save(os.path.join(settings['database.directory'], 'kinetics', 'families', family_name))


database = RMGDatabase()

database.load(
    path=settings['database.directory'],
    thermo_libraries=['primaryThermoLibrary'],
    transport_libraries=[],
    reaction_libraries=[],
    seed_mechanisms=[],
    kinetics_depositories=['training'],
    kinetics_families='all',
    depository=False,
)

auto_generated_families = []
for family_name in database.kinetics.families.keys():
    if database.kinetics.families[family_name].auto_generated:
        auto_generated_families.append(family_name)


repo_dir = os.path.dirname(os.path.dirname(__file__))
os.chdir(repo_dir)
ref_commit_hash = ''
with open(os.path.join(repo_dir, 'scripts', 'sensitivity_ref_commit.txt'), 'r') as f:
    ref_commit_hash = f.readline()
repo = Repo(repo_dir)
hcommit = repo.head.commit
ref_commit = repo.commit(ref_commit_hash)


for i, family_name in enumerate(auto_generated_families):
    # generate the rules.py file name
    rules_path = os.path.join(settings['database.directory'], 'kinetics', 'families', family_name, 'rules.py')

    if not os.path.exists(rules_path):
        # TODO log this as a warning
        print(f'Rules path {rules_path} does not exist')
        continue

    diff = hcommit.diff(other=ref_commit, paths=rules_path)
    if diff:
        print(f'Rules file for {family_name} has changed since reference {ref_commit_hash}. Updating sensitivities...')
        save_sensitivity(database.kinetics.families[family_name])
        print(diff)


# save the new reference commit hash
with open(os.path.join(repo_dir, 'scripts', 'sensitivity_ref_commit.txt'), 'w') as f:
    ref_commit_hash = f.write(str(repo.head.commit))
