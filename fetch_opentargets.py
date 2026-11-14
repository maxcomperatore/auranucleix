import requests
import json

def fetch_glp1r_target_validation():
    # ENSG00000112164 is human GLP1R
    query = """
    query targetDetails($ensemblId: String!) {
      target(ensemblId: $ensemblId) {
        id
        approvedSymbol
        approvedName
        biotype
        geneticConstraint {
          constraintType
          score
        }
        tractability {
          label
          modality
          value
        }
        associatedDiseases(page: {size: 10, index: 0}) {
          count
          rows {
            disease {
              id
              name
            }
            score
          }
        }
      }
    }
    """
    variables = {"ensemblId": "ENSG00000112164"}
    r = requests.post("https://api.platform.opentargets.org/api/v4/graphql", json={"query": query, "variables": variables})
    if r.status_code == 200:
        data = r.json()
        with open("d:/crew/experiment/reitwave/auranucleix/opentargets_glp1r_associations.json", "w") as f:
            json.dump(data, f, indent=2)
        print("OpenTargets GLP1R data saved successfully!")
        return data
    else:
        print(f"Error: {r.status_code}")
        return None

if __name__ == "__main__":
    fetch_glp1r_target_validation()
