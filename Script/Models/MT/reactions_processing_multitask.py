import os
import pandas as pd
from GNN_workflow_multitask import (run_multitask_training_multi_seed,,load_best_params_multitask)
from GNN_workflow import FeatureConfig

ROOT_PATH   = r'C:\Users\Studenti\Desktop\alessio\Multitask'
SDF_DIR     = r'C:\Users\Studenti\Desktop\alessio\Multitask\Multitask'        # cartella SDF canonici
CSV_PATH    = r'C:\Users\Studenti\Desktop\alessio\Multitask\y-som\y_som_Multitask_match.csv' # y_som multitask
SPLIT_DIR   = r'C:\Users\Studenti\Desktop\alessio\Multitask\Risultati-sottoclassi\Multitask\rdkit-split-corretto-AM\data-split'     # {task}_train/val/test.csv
DUPL_PATH   = r"C:\Users\Studenti\Desktop\alessio\Multitask\Risultati-sottoclassi\Multitask\rdkit-split-corretto-AM\mappa_multitask.csv"   # mappa duplicati

def run_all():
    all_metrics = []

    GLOBAL_CONFIG = FeatureConfig(
        elem_list     = [6, 7, 8, 9, 14, 15, 16, 17, 35, 53],
        chirality     = ['CHI_UNSPECIFIED', 'CHI_TETRAHEDRAL_CW', 'CHI_TETRAHEDRAL_CCW'],
        degree        = [1, 2, 3, 4],
        hybridization = ['SP', 'SP2', 'SP3'],
        bond_types    = ["SINGLE", "DOUBLE", "TRIPLE", "AROMATIC"],
        stereo        = ['STEREONONE', 'STEREOZ', 'STEREOE']
    )

    task_names = [
        'match_Dealkylation',
        'match_Glucuronidation',
        'match_GlutathioneConjugation',
        'match_Hydrolysis',
        'match_Oxidation',
        'match_Reduction',
        'match_Sulfonation'
    ]

    tuning_dir = os.path.join(ROOT_PATH, 'Risultati-sottoclassi', 'Multitask', 'rdkit-split-corretto-AM')

    save_dir = os.path.join(ROOT_PATH, 'Risultati-sottoclassi', 'Multitask', 'rdkit_seeds')

    best_params = load_best_params_multitask(tuning_dir)

    df_all, agg = run_multitask_training_multi_seed(
        sdf_dir             = SDF_DIR,
        multitask_csv_path  = CSV_PATH,
        split_dir           = SPLIT_DIR,
        duplicate_csv_path  = DUPL_PATH,
        task_names          = task_names,
        cfg                 = GLOBAL_CONFIG,
        save_dir            = save_dir,
        hyperparams         = best_params,
        seeds               = [23, 30, 42, 18, 56]
    )

    df_all.to_csv(os.path.join(ROOT_PATH, "GNN_multitask_metrics_all_seeds.csv"), index=False)
    print("\nReport globale (tutti i seed) salvato.")


if __name__ == "__main__":
    run_all()