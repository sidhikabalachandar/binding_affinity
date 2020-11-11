import pandas as pd

def main():
    df = pd.read_csv("BindingDB_Ki.csv")
    prots = []
    for prot in df['Target Name Assigned by Curator or DataSource'].unique():
        prot_df = df[df['Target Name Assigned by Curator or DataSource'] == prot]
        prots.append((prot, len(prot_df), len(prot_df['PDB ID(s) for Ligand-Target Complex'].unique())))

    sorted_prots = sorted(prots, key=lambda x: x[2], reverse=True)
    print(sorted_prots[:5])

if __name__ == "__main__":
    main()