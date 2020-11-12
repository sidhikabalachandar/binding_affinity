import pandas as pd

def main():
    df = pd.read_csv("BindingDB_Ki.csv")
    prots = []
    for prot in df['Target Name Assigned by Curator or DataSource'].unique():
        prot_df = df[df['Target Name Assigned by Curator or DataSource'] == prot]
        # index 0 is prot name, index 1 is number of distinct structures in binding db, index 2 is number of distinct
        # structures in pdb
        prots.append((prot, len(prot_df), len(prot_df['PDB ID(s) for Ligand-Target Complex'].unique()),
                      len(prot_df['PubChem CID'].unique())))

    sorted_prots = sorted(prots, key=lambda x: x[3], reverse=True)

    # change the number down here to get more/less structures
    print(sorted_prots[:5])
    top = sorted_prots[0]
    top_df = df[df['Target Name Assigned by Curator or DataSource'] == top[0]]
    df = top_df.drop_duplicates(subset='PubChem CID', keep="first")
    df.to_csv('serotonin_all.csv')

if __name__ == "__main__":
    main()